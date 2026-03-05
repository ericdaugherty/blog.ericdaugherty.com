---
title: "Using Comet with Lift to Dynamically Update Pages"
date: 2010-07-21T12:30:00.002Z
url: /2010/07/using-comet-with-lift-to-dynamically.html
draft: false
---

<a href="http://ww.liftweb.net/">Lift</a>, a web framework written in <a href="http://www.scala-lang.org/">Scala</a>, provides easy integration with <a href="http://en.wikipedia.org/wiki/Comet_%28programming%29">Comet</a>, a server side HTML push model. <br />
<br />
The Lift Demo site provides a <a href="http://demo.liftweb.net/chat">good overview</a> of the basic Comet usage.&nbsp; A <a href="http://scala-tools.org/mvnsites/liftweb-2.0/framework/scaladocs/net/liftweb/http/CometActor.html">CometActor</a> has two main parts.&nbsp; The render method, which is executed when the page is first requested, generates any initial content required for the page.&nbsp; The actor message method, called when the CometActor receives a message, is responsible for triggering an update on the page.<br />
<br />
The render method is similar to the render method on any snippet.&nbsp; It usually has a bind method that replaces XML tags in the template with dynamic content.&nbsp; This can be visible HTML, JavaScript methods that will be used during updates, or a combination of the two. <br />
<br />
The <a href="http://demo.liftweb.net/chat">Comet Chat example</a> has the following render method:

```scala
// display a line
private def line(c: ChatLine) = bind("list", singleLine,
                "when" -> hourFormat(c.when),
                "who" -> c.user,
                "msg" -> c.msg)

// display a list of chats
private def displayList(in: NodeSeq): NodeSeq =
chats.reverse.flatMap(line)

override def render =
  bind("chat", bodyArea,
       "name" -> userName,
       AttrBindParam("id", Text(infoId), "id"),
       "list" -> displayList _)
```
Here, the render method sets the chat:name tag to userName, and the chat:list tag is processed by the line method (via displayList).<br />
<br />
The actor methods are where it gets interesting.&nbsp; The actual method can be one of low(med/high)Priority or messageHandler.&nbsp; These methods define PartialFunctions that can be used to handle incoming messages.&nbsp; There are two basic approaches that can be used from here.&nbsp; The first approach is to update some internal state and force the render method to replace the existing content.&nbsp; This would look something like:

```scala
var messageText : List[String] = Nil

override def messageHandler = {
    case message : String => messageText ::= message; reRender(false)
}
```
Assuming you have a render method that takes the messageText and renders it out as HTML, the page will reflect the contents of messageText, and will be updated each time a message is received.&nbsp; However, if the amount of changes are small relative to the rendered block, or you are creating an ever-increasing list of content, this can be inefficient.<br />
<br />
The second approach for the actor message methods is to call a JavaScript method on the client with the updated information.&nbsp; This would look something like:

```scala
override def messageHandler = {
  case message : String => partialUpdate(OnLoad(AppendHtml("logContents", <div>{message}</div>) & JsRaw("autoScroll();")))
}
```
In this example, the partialUpdate method is used to push a string of JavaScript Commands to the web page.&nbsp; AppendHtml is a shortcut to a jQuery method to add HTML to a specific element. This is combined with a call to the autoScroll method which we assume is already defined on the page and acts on the newly updated information in some way (i.e. automatically scrolling the div to the bottom so the updated HTML is visible).&nbsp; This does not trigger a new call to the render method.<br />
<br />
Note that the appendHtml method is defined net.liftweb.http.js.jquery.JqJsCmds instead of net.liftweb.http.js.JsCmds as it is a bridge to jQuery (hence the Jq prefix).&nbsp; <br />
<br />
The combined power of server side pushes, Actors, and convenient helper methods makes it very easy to build a page that is updated in real time.
