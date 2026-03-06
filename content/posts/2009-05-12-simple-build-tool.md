---
title: "Simple Build Tool"
date: 2009-05-12T15:04:00.003Z
url: /2009/05/simple-build-tool.html
draft: false
---
As part of my foray into Scala I came across a new build tool called <a href="http://code.google.com/p/simple-build-tool/">Simple Build Tool (sbt)</a>.  As the website states, "<tt>sbt</tt> is a simple build tool for Scala projects that aims to do the basics well."

I didn't really come across sbt, it came to me.  Tim and Mark commented on my <a href="http://www.ericdaugherty.com/blog/2009/04/maven-versus-ant.html">Maven vs. Ant</a> post and I decided to check it out.

It is similar to maven in its dependency management and configuration by convention.  If you do need explicit configuration you write it as actual scala code, which is interesting.  Obviously it is powerful.  You can do pretty much anything, but the flexibility and relative immaturity (it is version 0.4.5) of the project makes it difficult at times to determine how to do something.

sbt runs as an interactive session, so it solves the java startup overhead by just staying up.  In practice this actually worked well for me, and provided the fastest compile/package times of any of the tools I used.

For the issues and questions I did have, the support in the google group was great.  Mark especially helped me track down and solve questions and issues I had.  Some were my own learning curve, some resulted in patches to sbt.  The last issues we worked through was making an executable jar, which turned out to be a platform issue (/ versus \) that is getting patched.

If you are working with Scala I encourage you to give it a spin.  I think it has a future as it continues to develop and gain users.
