---
title: "Scala and ActionScript"
date: 2009-12-01T02:15:00Z
url: /2009/11/scala-and-actionscript.html
draft: false
---
Like many experienced Java programmers, I've played with several other languages and platforms over time.  While most development languages are not game changing on their own, they can have an impact on the speed and level of enjoyment of a developer.  Development languages are like a carpenter's tools.  Most tools won't change they house an experienced carpenter can build, but they may make the experience more enjoyable.

With that caveat in mind, I wanted to explore my (current) preferred toolchain, <a href="http://scala-lang.org/">Scala</a> and <a href="http://www.adobe.com/devnet/actionscript/articles/actionscript3_overview.html">ActionScript</a> (Flex).  Not only are both languages powerful and enjoyable in their own right, their similar syntax and easy integration provide a powerful combination.

Scala is:
<blockquote>"... a general purpose programming language designed to express common programming patterns in a concise, elegant, and type-safe way. It smoothly integrates features of object-oriented and functional languages, enabling Java and other programmers to be more productive."</blockquote>Scala brings the benefits of a functional language, the accessibility of an object-oriented language and the power of the Java platform.  I find the concise yet familiar syntax a joy to work with.

ActionScript is a dynamic language based on <a href="http://en.wikipedia.org/wiki/ECMAScript">ECMAScript</a> used to develop Flex applications. ActionScript brings the familiarity and dynamic nature of JavaScript, with the addition of more object-oriented features, and a powerful Flex API.

While there are some major differences in these languages, their basic syntax is very similar.  To define a 'POJO' (where J is really Scala or ActionScript):

ActionScript:

```actionscript
package com.ericdaugherty.sample
{
public class Person
{

  public var firstName:String;
  public var lastName:String;
  public var middleInitial:String;
}
}
```
Scala:

```scala
package com.ericdaugherty.sample

class Person {

var firstName:String = ""
var lastName:String = ""
var middleInitial:String = ""
}
```
While they are very similar, there are a few differences:

- Scala defaults properties and functions to public, so you save on some boilerplate code.
- In Scala, every variable must be initialized, or the compiler will assume it is abstract.
- While this example provided explicit types, they can be inferred by the compiler.
In this example, the properties are still all statically typed Strings, but the explicit definition is unnecessary:

```scala
package com.ericdaugherty.sample

class Person {

var firstName = ""
var lastName = ""
var middleInitial = ""
}
```
You can leave off the types in ActionScript as well.  However, this results in an untyped variable instead of using type inference to infer the static type.  It also results in the following compiler warning (using Flex Builder):

```
1008: variable 'firstName' has no type declaration.
```
Finally, Flex Builder does not support code completion without explicit typing, so in practice ActionScript really requires explicit type definition.

In both languages, you can define explicit get/set behavior instead of a generic property.  To only define a setter in ActionScript:

```actionscript
private var _firstName:String;

public function set firstName(firstName:String) {
_firstName = firstName.toLowerCase();
}
```
In Scala:

```scala
var _firstName = ""

def firstName_=(firstName:String) {
_firstName = firstName
}
```
In Scala and ActionScript, the trailing semicolons are optional, reducing the need for superfluous characters.

While these comparisons are very superficial, they do make context switching between Scala and ActionScript a bit easer.  However, it is important to understand the differences in implementation.  Sometimes similar syntaxes can disguise vast differences.

Note: While this example makes use of 'var' definitions in Scala, in practice a functional program would use the final 'val' definitions instead.  One of my most common muscle memory issues is typing val in ActionScript instead of var.
