---
title: "Google cleans up URLs"
date: 2009-02-12T21:54:00.003Z
url: /2009/02/google-cleans-up-urls.html
draft: false
---
I'm a little 'uptight' about URLs.  I've blogged about my frustration with the <a href="http://www.ericdaugherty.com/blog/2007/01/java-servlet-url-pattern-exclude-me.html">Java Servlet mapping constraints before</a>, and I'm a believer in <a href="http://www.w3.org/Provider/Style/URI">W3C recommendations on URLs</a>.

Google just announced a <a href="http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html">tool for Webmasters</a> that allows users to specify a canonical URL for a single 'page', even if you can access it from multiple URLs.  This is a nice patch for systems that don't really conform to the above W3C recommendation but believe in the concept.  It also helps clean up Google's indexes, which is another good thing.

Since their approach is a simple tag added the the  section of an HTML document, hopefully the other search engines will adopt it as well.  The example from their post:
<blockquote>&lt;link rel="canonical" href="http://www.example.com/product.php?item=swedish-fish" /&gt;
</blockquote>
