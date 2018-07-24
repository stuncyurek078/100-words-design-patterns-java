'''
Created on 02 Sep 2016

Generates content for design-patterns-story site  

@author: dstar55@yahoo.com

'''

import constants
import clone  
import parser
import content
import deletedir
import publish
import decorator
import shutil 
import os
import argparse

# script for publishing design-pattern-stories.com site. User can clone a repo, generate a content, publish a content and clean data
# be aware that script expect that user follows proper orders in action: 1. clone, 2. generate, 3. publish, 4. delete
def main():
    parser = argparse.ArgumentParser(description="This is a script for publishing content for www.design-pattern-stories.com site. " \
                                     "User can clone necessary repositories, generate site content, publish content for the live site and clean all generated data." \
                                     "It is expected that user follows proper orders in action: " \
                                     "1. clone, 2. generate gh-pages, slides, fractus tutorials, 3. publish, 4. generate slide 5. delete")
    parser.add_argument("-c","--clone", action='store_true', help="clone necessary github repositories")
    parser.add_argument("-g", "--generate", action='store_true', help="generate content for site: www.design-pattern-stories.com")
    parser.add_argument("-p", "--publish", action='store_true', help="publish content to the live site: www.design-pattern-stories.com")
    parser.add_argument("-s", "--slides", action='store_true', help="generates initial slides content for https://gitpitch.com/dstar55/100-words-design-patterns-java")
    parser.add_argument("-f", "--fractus", action='store_true', help="generates content for https://fractus-io.github.io/tutorials/design-patterns/")
    parser.add_argument("-d", "--delete", action='store_true', help="clean all generated data")
    
    args = parser.parse_args()
    if args.clone:
        main_clone()
    elif args.generate:
        main_generate()    
    elif args.publish:
        main_publish()
    elif args.slides:
        main_slides()
    elif args.fractus:
        main_fractus()                 
    elif args.delete:
        main_delete()
    else:
        parser.print_help() 

# clone repos
def main_clone():
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.MASTER_BRANCH, constants.LOCAL_MASTER_REPOSITORY_PATH)
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.GH_PAGES_BRANCH, constants.LOCAL_GH_PAGES_REPOSITORY_PATH)
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.GH_PAGES_RESOURCES_BRANCH, constants.LOCAL_GH_PAGES_RESOURCES_REPOSITORY_PATH)
    
# parse readme.md from master and creates content for gh-pages branch which is in fact site: www.design-pattern-stories.com     
def main_generate():
    content.createGHPagesContent(decorator.decorateGHPagesContent(parser.parseReadme(constants.LOCAL_MASTER_REPOSITORY_PATH + constants.SLASH + constants.README_FILE_NAME)))

# parse readme.md from master and creates content https://gitpitch.com/dstar55/100-words-design-patterns-java     
def main_slides():
    content.createSlidesContent(decorator.decorateGHPagesContent(parser.parseReadme(constants.LOCAL_MASTER_REPOSITORY_PATH + constants.SLASH + constants.README_FILE_NAME)))
    
# parse readme.md from master and creates content https://gitpitch.com/dstar55/100-words-design-patterns-java     
def main_fractus():
    content.createFractusTutorialsContent(decorator.decorateGHPagesContent(parser.parseReadme(constants.LOCAL_MASTER_REPOSITORY_PATH + constants.SLASH + constants.README_FILE_NAME)))    

def main_publish():
    publish.publish()
    
def main_delete():
    deletedir.removeDirs()
    
if __name__ == '__main__':
    main()