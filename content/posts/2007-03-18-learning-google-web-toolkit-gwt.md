---
title: "Learning Google Web Toolkit (GWT)"
date: 2007-03-18T21:08:00Z
url: /2007/03/learning-google-web-toolkit-gwt.html
draft: false
---
As I mentioned my <a href="http://www.ericdaugherty.com/blog/2007/03/juiced-about-guice.html">post about Guice</a>, I'm finally motivated to start playing with code again.

Based on how cool Guice seemed, I figured I should finally take a look at GWT and see what it was all about. First, it is certainly different from writing any other web application. There is some very cool stuff. You can very quickly and easily write JavaScript style logic in actual Java. That is a great improvement over anything else.

One issue I found out of the gate was the CSS support.  I found a post documenting <a href="http://blogs.nubgames.com/code/?p=13">CSS in GWT</a> that is helpful. However, it appears that all instances of Button use the same class (gwt-Button). After a little digging I found the addStyleName and setStyleName methods. This allows you to assign a CSS class name to any object to allow it to be styled in CSS. This alleviates some of the fears I had about having too much of the look/feel in your code.

It took a little while for me to digest the fact that the Java code I was writing would be compiled down to JavaScript. When you start a GWT project, there is a x.y.z.client package, that will contain Java files that will be compiled down to JavaScript. The issue I had was that I figured I would make calls to 'real' Java files here to load my initial data for the page (just like in a Servlet, JSP, etc.). Of course, this isn't allowed. You must create a web service like class on the server and make a RPC call from your client Java to the server code. This all makes sense, but takes a bit of time to sink in when you start hacking away. It also ads a layer of indirection as any  2q objects you pass between the service and client must also live in the client package and not contain any code that can't be compiled down to JavaScript.

The biggest conclusion I've drawn, and probably the most obvious, is that GWT appears to be really good for building web applications with a very small amount of pages.  If you look at gmail or Google Reader, these are obvious model applications.  There is heavy use of AJAX, keyboard interaction, and other rich navigation.  Gmail/Google Reader are heavily data driven, but the data is all the same type (email, blog posts).  GWT is certainly something I will keep in mind for future projects, but it is a very specific 'hammer' for a very specific use.
