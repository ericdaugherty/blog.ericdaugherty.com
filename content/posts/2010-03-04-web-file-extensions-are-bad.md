---
title: "Web File Extensions are Bad"
date: 2010-03-04T19:53:00Z
url: /2010/03/web-file-extensions-are-bad.html
draft: false
---

I hate file extensions on websites.&nbsp; It is an unnecessary leaky abstraction, and is <a href="http://www.w3.org/Provider/Style/URI">discouraged by the W3C</a>.&nbsp; All file extensions are not necessarily bad, but any file extension that exposes the underlying technology implementation is.&nbsp; Any .pl, .php, .asp, .aspx, .jsp, .do, *.struts, etc extensions are B A D.<br />
<br />
I've talked about this before, and come up with <a href="http://blog.ericdaugherty.com/2010/02/excluding-content-from-url-pattern-in.html">some workarounds</a> to build extension-less java web applications before.<br />
<br />
However, I've come across what I think is a better way, thanks to a <a href="http://raibledesigns.com/rd/entry/extensionless_urls_in_java_web">post a couple years ago by Matt Raible</a>.<br />
<br />
I came across the issue using the Spring WebMVC DispatcherServlet.&nbsp; I want all dynamic URLs handled by the Spring Controllers, using Annotations.&nbsp; However, mapping the DispatcherServlet to /* means that every URL will be processed by the DispatcherServlet, including the .jsp views returned by the Controller.&nbsp; As I mentioned in <a href="http://blog.ericdaugherty.com/2010/02/excluding-content-from-url-pattern-in.html">the previous post</a>, you can 'unmap' content and have it handled by a default or jsp servlet in some app servers, but not all.<br />
<br />
You can also try to map specific subsets of URLs to spring.&nbsp; However, this is harder than it sounds.&nbsp; By default, Spring will map the wildcard portion of the URL matched, not the entire URL.&nbsp; So if you have /foo/* as your url-pattern, the controller with a mapping of /foo/one will not match /foo/one, but instead matches /foo/foo/one.<br />
<br />
It appears that you can use the property <code>alwaysUseFullPath</code> to change this behavior, but it did not seem to work as expected for me.<br />
<br />
Instead, there is a more generalized solution, as Matt suggested.&nbsp; URL Rewriting.<br />
<br />
The <a href="http://tuckey.org/urlrewrite/">URL Rewrite Filter</a> project provides a Filter that you easily define rewrite rules for, just like in Apache.&nbsp; So I setup my DispatcherServlet to match *.spring, I setup a rule to rewrite all extension-less requests to .spring, and I setup my annotations to have the .spring extension.<br />
<br />
Now my web application can handle the odd html, png, or other static files if necessary, but does not expose any implementation details in the URLs.&nbsp; Perfect.<br />
<br />
For reference, here are the relevant portions of my config:<br />
<br />
Web.xml<br />
<pre class="brush: xml">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"&gt;

  &lt;filter&gt;
    &lt;filter-name&gt;UrlRewriteFilter&lt;/filter-name&gt;
    &lt;filter-class&gt;org.tuckey.web.filters.urlrewrite.UrlRewriteFilter&lt;/filter-class&gt;
  &lt;/filter&gt;
  
  &lt;filter-mapping&gt;
    &lt;filter-name&gt;UrlRewriteFilter&lt;/filter-name&gt;
    &lt;url-pattern&gt;/*&lt;/url-pattern&gt;
  &lt;/filter-mapping&gt;
  
  &lt;servlet&gt;
    &lt;servlet-name&gt;SpringMVCServlet&lt;/servlet-name&gt;
    &lt;servlet-class&gt;org.springframework.web.servlet.DispatcherServlet&lt;/servlet-class&gt;
      &lt;init-param&gt;
        &lt;param-name&gt;contextConfigLocation&lt;/param-name&gt;
        &lt;param-value&gt;/WEB-INF/your.config.file.location.xml&lt;/param-value&gt;
      &lt;/init-param&gt;
    &lt;load-on-startup&gt;1&lt;/load-on-startup&gt;
  &lt;/servlet&gt;
  
  &lt;servlet-mapping&gt;
    &lt;servlet-name&gt;SpringMVCServlet&lt;/servlet-name&gt;
    &lt;url-pattern&gt;*.spring&lt;/url-pattern&gt;
  &lt;/servlet-mapping&gt;
  
&lt;/web-app&gt;</pre>urlrewrite.xml<br />
<pre class="brush: xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE urlrewrite PUBLIC "-//tuckey.org//DTD UrlRewrite 3.0//EN"
  "http://tuckey.org/res/dtds/urlrewrite3.0.dtd"&gt;

&lt;urlrewrite&gt;
  &lt;rule&gt;
    &lt;from&gt;/$&lt;/from&gt;
    &lt;to type="forward"&gt;home&lt;/to&gt;
  &lt;/rule&gt;

  &lt;rule&gt;
    &lt;from&gt;^([^?]*)/([^?/\.]+)(\?.*)?$&lt;/from&gt;
    &lt;to last="true"&gt;$1/$2.spring$3&lt;/to&gt;
  &lt;/rule&gt;
  
&lt;/urlrewrite&gt;</pre>Sample Controller<br />
<pre class="brush: java">@Controller
@RequestMapping("/foo")
public class SimpleDataController {

  @RequestMapping("/bar.spring")
  public ModelAndView bar() {
    ...
  }
}</pre>
