---
title: "Integrating GraniteDS and BlazeDS with a Spring WebMVC Application"
date: 2010-02-05T20:28:00Z
url: /2010/02/integrating-graniteds-and-blazeds-with.html
draft: false
---
Both GraniteDS and BlazeDS provide support for remote calls and messaging using Adobe's AMF protocol.  However, when it comes to integrating them with a Spring application that already uses Spring's DispatchServlet, the projects start to show some differences.

In a <a href="http://blog.ericdaugherty.com/2010/01/getting-started-with-graniteds-spring.html">previous post</a>, I outlined the steps to getting GraniteDS 2.0 setup with Spring.  However, this approach results in two separate Spring contexts, so my Spring Service with the 'singleton' scope was being loaded twice.  Not good.

I found that GraniteDS 2.1 did support better Spring integration.  You can see a blog post <a href="http://graniteds.blogspot.com/2009/11/new-in-graniteds-210-rc1-simplified.html">here</a> that describes the process, or their <a href="http://www.graniteds.org/confluence/display/DOC21/2.+Spring+Services">updated documentation</a>.&nbsp; Note that the blog post seems to be somewhat out of date.&nbsp; One issue is the schema URL:&nbsp;

http://www.graniteds.org/config/granite-config-2.1.xsd in the blog instead of http://www.graniteds.org/public/dtd/2.1.0/granite-config-2.1.xsd.

The BlazeDS approach has a good overview <a href="http://ria.dzone.com/articles/introduction-spring-blazeds">here</a>, and the <a href="http://static.springsource.org/spring-flex/docs/1.0.x/reference/html/index.html">documentation</a> is pretty good too.&nbsp; In my case, I used the @RemotingDestination annotation on my service beans instead of adding:

```xml
<flex:remoting-destination />
```
to the Spring config as I'm using auto-wiring for most of my beans.

There are a couple of things that bothered me about the GraniteDS approach as opposed to the BlazeDS approach.

First, the BlazeDS approach retains a (simplified) services-config.xml file, so the traditional configuration options are still available, and the integration with Flex/Flash Builder works as well.&nbsp; Not a big deal, but it stays closer to the existing conventions.

Secondly, I was able to get BlazeDS working much faster.  The project simply seems to be more mature, and the documentation and examples are clearer.  The Granite documentation notes that they are working to achieve parity with the BlazeDS Spring integration, so it is likely that they will be able to close this gap.  But for now, it seems to be a work in progress.&nbsp; It is only available in the 2.1 version, which is currently at RC2.&nbsp; I also had to use the 2.x version of spring-security-core instead of the 3.0 version, as Spring seems to have refactored the location of the BadCredentialsException class.

All that said, GraniteDS does provide more features than BlazeDS, so the comparison may not be entirely fair.  I found the Granite ActionScript code generator (gas3) to work well, although it seemed to miss some import statements before it would compile in Flex 4.&nbsp; However, the community around BlazeDS seems larger at this point, with the expected increase in polish.&nbsp; However, competition is good, so hopefully the future versions of GraniteDS continue to improve.

Either way, it is good to see both of these projects working to provide easy integration with an existing SpringWebMVC project.  Adding new Flex functionality to existing Flex applications <b>should</b> be very painless.
