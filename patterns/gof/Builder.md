---
layout: page
title: Builder
permalink: /Builder/
tag: pattern
---



### Story 

Separates the construction of a complex object from its representation so that the same construction process can create different representations.

This pattern is used by PC shops to contruct PC's.
PC is combination of various parts like CPU, motherboard, memory, storage, power supply, video card, etc.
To build a PC same construction process is used even for each part we have different variation.
Whether a customer picks a classical hard disk or SSD for storage, the construction process is the same. 



### UML 
![]({{site.baseurl}}/assets/img/builder.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/builder/Builder.java
```java 
package com.hundredwordsgof.builder;

/**
 * Builder, declares interface for creating parts of a Product object 
 * 
 */
abstract class Builder {

	public abstract Builder createProduct();
	
	public abstract Builder buildPart1(String part);
	
	public abstract Builder buildPart2(String part);
	
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/builder/ConcreteBuilder.java
```java 
package com.hundredwordsgof.builder;

/**
 * ConcreteBuilder class, constructs and assembles parts of the Product by implementing the Builder interface
 */
public class ConcreteBuilder extends Builder {

	private Product product;
		
	public Builder createProduct(){
		this.product = new Product();
		return this;
	} 
	
	public Builder buildPart1(String part) {
		product.setPart1(part);
		return this;
	}

	public Builder buildPart2(String part) {
		product.setPart2(part);
		return this;
	}
	
	public Product getResult(){
		return product;
	}

}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/builder/Director.java
```java 
package com.hundredwordsgof.builder;

/**
 * 
 * Director class, constructs an object using the Builder interface
 *
 */
public class Director {

	private Builder builder;
	
	public Director(Builder builder){
		this.builder = builder;
	}
	
	public void construct(){
		builder.createProduct().buildPart1("part1").buildPart2("part2");
	}
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/builder/Product.java
```java 
package com.hundredwordsgof.builder;


/** 
 * Product class, represents complex object
 */
public class Product {

	private String part1;
	
	private String part2;

	public void setPart1(String part1) {
		this.part1 = part1;
	}

	public void setPart2(String part2) {
		this.part2 = part2;
	}

	public String getPart1() {
		return part1;
	}

	public String getPart2() {
		return part2;
	}
	
	
}
```
