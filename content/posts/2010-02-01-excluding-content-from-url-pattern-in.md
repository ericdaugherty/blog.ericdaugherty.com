---
title: "Excluding Content from url-pattern in Java web.xml"
date: 2010-02-01T20:27:00.002Z
url: /2010/02/excluding-content-from-url-pattern-in.html
draft: false
---

A while ago I <a href="http://www.ericdaugherty.com/blog/2007/01/java-servlet-url-pattern-exclude-me.html">blogged about my frustration with my inability to exclude certain URLs from a url-pattern mapping</a>.  In short, I wanted to map everything except /static/* to a dispatch servlet.<br /><br />There is a way to do this, in some servlet servers.  Many (most, all?) servlet containers define a default servlet to handle static content.  Be default, any unmapped URLs will be handled by the default servlet.  However, you can explicitly map certain URLs to this default servlet, achieving a de-facto url-exclude pattern.<br /><br />Here is an example:<br /><pre class="brush: xml">&lt;servlet-mapping&gt;<br /> &lt;servlet-name&gt;default&lt;/servlet-name&gt;<br /> &lt;url-pattern>/static/*&lt;/url-pattern&gt;<br />&lt;/servlet-mapping&gt;<br /><br />&lt;servlet-mapping&gt;<br /> &lt;servlet-name&gt;SpringMVCServlet&lt;/servlet-name&gt;<br /> &lt;url-pattern&gt;/*&lt;/url-pattern&gt;<br />&lt;/servlet-mapping&gt;</pre>Where in this case, you have SpringMVCServlet defined in your web.xml, but not default.  The default servlet definition is inherited from the servlet container.<br /><br />The order shouldn't matter, as long as your mapping for the default servlet is more specific.<br /><br />This is known to work in at least Jetty and Tomcat.
