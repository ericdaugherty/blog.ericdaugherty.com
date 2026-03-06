---
title: "Build Tools"
date: 2009-08-20T13:21:00.002Z
url: /2009/08/build-tools.html
draft: false
---
<div>I've said it before, <a href="http://www.ericdaugherty.com/blog/2009/04/maven-versus-ant.html">I find Maven annoying</a>.  I've even explored other build tools like <a href="http://www.ericdaugherty.com/blog/2009/05/simple-build-tool.html">Simple-Build-Tool</a>, which I like, but I'm not sure I love.</div><div>
</div><div>Now Steve Ebersole from Hibernate joins the ranks of the <a href="http://in.relation.to/Bloggers/Maven2YearsAfter">frustrated Maven users</a>.  He is frustrated with Maven's module setup, something I've seen first hand on my current project.  </div><div>
</div><div>Based on the comments on his post, it seems that <a href="http://gradle.org">Gradle</a> is becoming a popular alternative, I'll have to check it out.  </div><div>
</div><div><a href="http://www.ericdaugherty.com/blog/2009/05/simple-build-tool.html">Simple-Build-Tool</a> is also mentioned, though I've only used it for Scala projects so far, I find it interesting but also a bit difficult to fully understand.  It's flexibility and use of Scala is powerful, but has the common side-effect that it isn't obvious how to accomplish something, or what a configuration line really does.  I like the fact that it leverages Maven's standard structure, allowing you to easily test Maven projects with SBT.  </div><div>
</div>I think Ant could also be salvaged, if it adopted the Maven directory conventions and then allowed configuration from there, but I'm not sure that it the best approach.  It may just be time to move on.<div>
</div><div>What do I really want?  A tool that provides simple setup for 'standard' projects, but allows the flexibility and power for fine grained control when I want to devaite from the 'norm'.</div>
