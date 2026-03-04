---
title: "Recursive Snippet Processing with Lift"
date: 2010-07-22T12:30:00.004Z
url: /2010/07/recursive-snippet-processing-with-lift.html
draft: false
---

I really like how Lift's 'template' engine works.&nbsp; In short, you define XML tags that map to a Class and Method for execution.&nbsp; For instance, a basic HTML template looks like:<br />
<pre class="brush: xml">&lt;lift:MyClass.myMethod&gt;
  &lt;div&gt;Hello, &lt;my:name/&gt;.&nbsp; Welcome to my sample web app&lt;/div&gt;
&lt;/lift:MyClass.myMethod&gt;</pre>This will result in the myMethod function on MyClass being called, which can then easily replace &lt;my:name/&gt; with a dynamic value.<br />
<br />
The real power comes from the fact that the Lift framework will continue to (re)process the XML until all Lift tags have been resolved.&nbsp; This means that a call to one snippet can produce a call to one or more snippets.<br />
<br />
I came across an example of this on a recent project.&nbsp; I wanted to produce the same HTML block for multiple snippets.&nbsp; My first effort at refactoring produced something similar to this:<br />
<pre class="brush: xml">&lt;lift:MyClass:showAttr1 eager_eval="true" name="Attribute 1"&gt;
  &lt;lift:embed what="attribute" /&gt;
&lt;/lift:MyClass&gt;</pre>My MyClass looked like:<br />
<pre class="brush: scala">class MyClass extends AttributeHelper {

  private val attributeDefinitnion = ...
  val name = S.attr("name").openOr("Unnamed Attribute")

  def showattr1(xml:NodeSeq) : NodeSeq = {
    attrHelperBind(attributeDefinition, name, xml)
  } 
}</pre>The AttributeHelper trait defined the attrHelperBind method which took the attributeDefinition and used the bind method to replace the XML tags defined in the attribute template that was embedded in the body.&nbsp; Note, I needed the eager_eval="true" attribute so that the embed tag would be executed before the showAttr1 tag.<br />
<br />
This worked well and greatly reduced the amount of boiler plate code needed for each attribute.&nbsp; However, since Lift will continue to evaluate the XML until all the tags are processed, I realized I could further improve it.&nbsp; I created a generic snippet that simply returned the following block:<br />
<pre class="brush: xml">&lt;lift:MyClass.myMethod eager_eval="true"&gt;
   &lt;lift:embed what="attribute" /&gt;
&lt;/lift:MyClass.myMethod&gt;</pre>This allowed me to have a very generic entry in my HTML:<br />
<pre class="brush: xml">&lt;lift:Myhelper.helper snippet="MyClass.myMethod"/&gt;</pre>The implementation of this Snippet is:<br />
<pre class="brush: scala">def helper(xml:NodeSeq) : NodeSeq = {
  val snippet = S.attr("snippet").openOr("Helper.default")
  new Elem("lift", snippet, Attribute("eager_eval", Text("true"), Null), TopScope,
    &lt;lift:embed what="attribute" /&gt;)
}</pre>This simply produces the original XML block, which will then be processed normally.  The Elem call produced a element named &lt;lift:{snippet}&gt; with the body <br />
&lt;lift:embed what="attribute" /&gt;.  You must use the Elem object to create the XML because you cannot have dynamic tag names in XML literals.&nbsp; IE:<br />
<pre class="brush: scala">def myXml(name:String) = {
  &lt;lift:{name}&gt;Body&lt;/lift:{name}&gt;
}</pre>is not legal as the XML literal will not be parsed correctly.<br />
<br />
This ability to 'recursively' process the Lift XML tags enables the development of easy helper methods to allow the final XHTML templates to be very concise and readable.
