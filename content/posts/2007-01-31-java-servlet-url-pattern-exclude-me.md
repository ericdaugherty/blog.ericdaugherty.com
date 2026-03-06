---
title: "Java Servlet url-pattern - Exclude Me"
date: 2007-01-31T16:30:00.001Z
url: /2007/01/java-servlet-url-pattern-exclude-me.html
draft: false
---
Recently I was investigating one of the many Java web frameworks, and came across an old frustration.  First though, I should give some background.

The Java Servlet specification provides for the ability for developers to map various URLs to specific Servlets (request handlers).  You can map '*.do' to your Struts request dispatcher to enable the framework to handle all the requests for pages that should be served by the framework.  Basic wild cards are supported, but only positive matching, no excludes.

One of the basic tenants I have adopted is that the URLs in an applications should be technology agnostic.  If I can look at your website and tell what technology you are using, that is 'bad'.  Of course, I didn't come up with this wisdom on my own, it is mostly guided by the W3C <a href="http://www.w3.org/Provider/Style/URI">Cool URLs Article</a>.  So if your app has cgi-bin, .pl, .jsp, .asp, or .aspx files, etc, I consider that bad form.  Of course, I can setup my Java application with all the pages named .aspx, but I find it much better to keep it generic to begin with.

One of the main issues I face when I use a web framework is how to integrate the main request dispatcher without manually mapping every valid URL.  What I would like is the ability to map everything EXCEPT certain URLs.

For example, I'd like to map /* to my dispatcher, with the exception of *.html, *.gif, *.jpg, *.css, and *.js.  This allows me to have all the dynamic requests served by the dispatcher, while the static content is served normally.  In a production environment, I can accomplish this using Apache to only pass through the URLs I define to Tomcat (Apache does have the 'except' logic in it's mapping).

Another common example is applying Servlet Filters.  Using Servlet Filters you can apply security or any type of logic to a large set of requests.  Maybe I would like to secure all the pages in my site except for / and /login.  Today I map the filter to all the URLs, and then in code define any URLs that should be excluded.  However, in doing this I've mixed my configuration between my web.xml file and my source code.

The ability to define a Regular Expression, or more complex rules (match 'a' except 'b') would give much greater flexibility.

A few Google searches have yielded some mildly interesting work-arounds but, nothing that I really find satisfyingly.  Let me know if you have any better solutions.

UPDATE: Thanks for the many work-arounds in the comments.  There is another option as well, see my <a style="font-weight: bold;" href="http://www.ericdaugherty.com/blog/2010/02/excluding-content-from-url-pattern-in.html">new post for details</a>.
