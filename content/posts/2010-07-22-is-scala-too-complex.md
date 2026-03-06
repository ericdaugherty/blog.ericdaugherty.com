---
title: "Is Scala Too Complex?"
date: 2010-07-22T19:26:00.001Z
url: /2010/07/is-scala-too-complex.html
draft: false
---
Is Scala too complex to become the 'New Java'?&nbsp; This question has been debated before, and there are some good existing posts including:

- <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=268561">Is Scala really more complicated than Java? - Dick Wall</a> (<a href="http://www.artima.com/forums/flat.jsp?forum=106&amp;thread=268561">with discussion</a>)
- <a href="http://speaking-my-language.blogspot.com/2009/11/is-scala-more-complicated-than-java.html">Is Scala more complicated than Java? - Vassil Dichev</a>
I tend to mostly agree with their arguments that Scala is not inherently more complex, but instead is different and has complexity in different ways.&nbsp; The syntax is different, and you need to learn a few different rules, and some features like Traits (multi-inheritance) and implicit conversions can make tracking down how things work a bit more difficult.&nbsp; In the end though, I don't believe Scala is itself more complex than Java.

But I want to take a different angle on this question.&nbsp; I believe that the use of Scala to build Domain Specific Languages illustrates how some of Scala's features can be used to create code that can be complex to understand, but that may be OK.

Domain Specific Languages

<a href="http://en.wikipedia.org/wiki/Domain-specific_language">Domain Specific Languages</a>, or DSLs, provide a syntax suited to a specific problem domain.&nbsp; Scala provides a set of features that enable the development of Scala libraries that enable a DSL or pseudo-DSL.

<a href="http://ww.liftweb.net/">Lift</a> is a web framework written in Scala.&nbsp; It provides what I consider a Scala based DSL for creating web applications.&nbsp; Let's examine some sample code from a simple Lift Snippet.&nbsp; (A Lift Snippet is somewhat related to a Servlet):

```scala
class A {
  def snippet (xhtml : NodeSeq) : NodeSeq = bind("A", xhtml, "name" -> Text("The A snippet"))
}
```
This example (from Exploring Lift <a href="http://groups.google.com/group/the-lift-book">site</a> - <a href="http://the-lift-book.googlegroups.com/web/master.pdf?gda=I7oRXzwAAAAgy_Zhga4ND3jj1lY6o2DA36IMOX7KRcjdndLx4ePOY5hQBWRFAWHsPl_3piZ--U79Wm-ajmzVoAFUlE7c_fAt">pdf</a>) provides a trivial snippet implementation.&nbsp; It simply replaces the &lt;A:name /&gt; XML tag with "The A snippet" text and would be called by the following XHTML:

```xml
<lift:A.snippet>
  <p>Hello, <A:name />!</p>
</lift:A.snippet>
```
There are a few things going on here to make this work.  First, the bind method is statically imported.  The import looks like:

```scala
import net.liftweb.util.Helpers._
```

This imports all the methods defined in the Helpers class into your class, enabling bind to be called without prefix.  The <a href="http://scala-tools.org/mvnsites/liftweb-2.0/framework/scaladocs/net/liftweb/util/Helpers$object.html">Helpers</a> class itself is just a roll-up of 9 other Helper class, so you could instead:

```scala
import net.liftweb.util.BindHelpers._
```
or even:

```scala
import net.liftweb.util.BindHelpers.bind
```
if you want strict control over what you are including.&nbsp; However, the point here is not that you can do static imports, which are possible in Java as well, but that the Lift framework makes heavy use of static imports to help create its DSL.

The second part requires two important concepts, implicit functions and operator overloading.&nbsp; The bind method has a few overloaded versions, but a typical case uses the following signature:

```scala
def bind(namespace : String, xml : NodeSeq, params : BindParam*)
```
In our simple example, the first two parameters are pretty straight forward, but how does:

```scala
"name" -> Text("The A snippet")
```
Get converted to a BuildParam?&nbsp; The answer is implicit functions and operator overloading.&nbsp; The <a href="http://scala-tools.org/mvnsites/liftweb-2.0/framework/scaladocs/net/liftweb/util/BindHelpers.html">BindHelpers</a> Object (statically imported with Helpers._), contains an implicit method with the following signature:

```scala
implicit def strToSuperArrowAssoc(in : String) : SuperArrowAssoc
```
The <a href="http://scala-tools.org/mvnsites/liftweb-2.0/framework/scaladocs/net/liftweb/util/BindHelpers.SuperArrowAssoc.html">SuperArrowAssoc</a> object defines a method (operator overload) -&gt;.&nbsp; This operator/method is overloaded to take different parameters, including scala.xml.Text.  So in our simple example:

```scala
"name" -> Text("The A snippet")
```
The "name" string is implicitly converted to a SuperArrowAssoc, and the -&gt; method is executed with a scala.xml.Text instance as the parameter, and returns a BindParam, which is then passed to the statically imported bind method.

Got all that?

It is a bit complicated, and it took me a little while to track down how it all worked.&nbsp; However...&nbsp; There are two important points to make before concluding that this is 'bad'.

First, the disparity between IDE functionality for Scala and Java is enormous.&nbsp; It is reasonably easy to understand any piece of code quickly in Java, in large part because of the IDE.&nbsp; It is trivial to understand inheritance trees, all references to a method/variable,&nbsp; all subclasses, etc.&nbsp; What I would like to see in Scala is easy decoding/indication of implicit methods and static imports.&nbsp; The Scala 2.8 plugin for Eclipse still fails at handling basic Class and import statement auto-complete most of the time, let alone handling more complex values<sup>(1)</sup>.

Second, and I think more interestingly, I'm not sure it matters if you 'understand' the code.&nbsp; The point of a DSL is to make it easy to build something in a specific domain.&nbsp; Yes, you are coding Scala, but do you really need to know where/how everything is defined/wired?&nbsp; If I'm building a web site, do I care how "x" -&gt; "y" gets converted and handled by Lift?&nbsp; What you have is a case where you end up learning the DSL syntax.&nbsp; I think this is different than learning a library API in Java.&nbsp; A library API uses traditional Java syntax, so you are just learning what methods exit.&nbsp; In Lift, you have to learn syntax itself, because there is no obvious way to 'discover' what is possible with the Lift library.&nbsp; An example:

Using Java and a traditional Library, I can use auto-complete to find the 'primary' classes, and use method auto-complete to look at the methods.&nbsp; Assuming it is a reasonably designed API, I can probably figure out how to use it without much more.&nbsp; Of course reference thing JavaDoc will help and is reccomended to make sure everything works as you assume, but you can get a long way on your own.

In Lift, there is no easy way to auto-discover how to interact with the framework using the DSL.&nbsp; You must read documentation/samples to understand what is available, or dig through endless pages of ScalaDoc to deduce the possible options.

In the end, I don't believe Scala is inherently more complex than Java.&nbsp; That said, I think it is easier to write hard to understand Scala code than it is with Java.&nbsp; Writing a DSL in Scala can make for code that is nearly impossible to 'infer proper usage' from the traditional means, but that isn't surprising.&nbsp; It is a DOMAIN SPECIFIC LANGUAGE, in essence, you created a new syntax, and you have to acknowledge that that learning that is different than learning the language it is written in.

I remain a fan of Lift and Scala.&nbsp; Even with these issues, I feel that the value they deliver is worth the learning curve necessary to become proficient.&nbsp;

(1) - But I am still very appreciative that the plugin exists at all, and hope they keep up the hard work!
