---
title: "Guice Burned By GoDaddy"
date: 2007-05-13T22:00:00Z
url: /2007/05/guice-burned-by-godaddy.html
draft: false
---
I've been working on a little app to display optimized train schedule information online in Java.  I'm writing it more to play with new libraries, etc. than because I really want the functionality, but that's irrelevant to the story...

As I mentioned in my previous post '<a href="http://www.ericdaugherty.com/blog/2007/03/juiced-about-guice.html">Juiced about Guice</a>', I wanted to play with Guice and see how it worked 'in the real world'.  So, I used it to help configure my application.

I deployed it on GoDaddy and hoped it would 'just work'.  Unfortunately it was not to be.  After a long debugging cycle (see footnote), I finally tracked it down to this error:

```
java.security.AccessControlException: access denied (java.lang.RuntimePermission accessDeclaredMembers)
 java.security.AccessControlContext.checkPermission(AccessControlContext.java:264)
 java.security.AccessController.checkPermission(AccessController.java:427)
 java.lang.SecurityManager.checkPermission(SecurityManager.java:532)
 java.lang.SecurityManager.checkMemberAccess(SecurityManager.java:1662)
 java.lang.Class.checkMemberAccess(Class.java:2125)
 java.lang.Class.getDeclaredMethods(Class.java:1762)
 sun.reflect.annotation.AnnotationType.<init>(AnnotationType.java:81)
 sun.reflect.annotation.AnnotationType.getInstance(AnnotationType.java:64)
 sun.reflect.annotation.AnnotationParser.parseAnnotation(AnnotationParser.java:202)
 sun.reflect.annotation.AnnotationParser.parseAnnotations2(AnnotationParser.java:69)
 sun.reflect.annotation.AnnotationParser.parseAnnotations(AnnotationParser.java:52)
 java.lang.Class.initAnnotationsIfNecessary(Class.java:3031)
 java.lang.Class.getAnnotation(Class.java:2989)
 java.lang.Class.isAnnotationPresent(Class.java:3001)
 com.google.inject.Scopes.isScopeAnnotation(Scopes.java:106)
 com.google.inject.BinderImpl.bindScope(BinderImpl.java:150)
 com.google.inject.BinderImpl.<init>(BinderImpl.java:111)
 com.google.inject.Guice.createInjector(Guice.java:75)
 com.google.inject.Guice.createInjector(Guice.java:53)
 com.google.inject.Guice.createInjector(Guice.java:43)
 org.apache.jsp.test_jsp._jspService(test_jsp.java:62)
```
Apparently, GoDaddy doesn't allow reflection.  This pretty much disqualifies Guice from working.  So, it looks like I'll have to rewrite it without Guice.

I just recently consolidated all my hosting on GoDaddy from my own managed box because I didn't want the hassle.  GoDaddy supports Rails and Java, so I figured I was covered for all eventualities.

However, now that my <a href="http://www.ericdaugherty.com/blog/2007/04/back-to-java.html">Rails fascination</a> is waning, maybe I should look for a better pure Java hosting environment.  Suggestions welcome. :)

Footnote:
GoDaddy only allows you to reload/restart your web application nightly when they do a global restart of Tomcat.  So, each debugging cycle takes 24 hours (or more since I don't bother with it every day).  You can get SOME stuff done by throwing up new JSP files intra day, but this cycle can be VERY frustrating and is totally unacceptable for any 'real' application needs.

