---
title: "Building Flex Applications with Gradle"
date: 2009-08-26T01:07:00Z
url: /2009/08/building-flex-applications-with-gradle.html
draft: false
---
<div><div style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 3px; padding-right: 3px; padding-bottom: 3px; padding-left: 3px; width: auto; font: normal normal normal 100%/normal Georgia, serif; text-align: left; "><div>In a <a href="http://www.ericdaugherty.com/blog/2009/08/build-tools.html">recent post</a>, I touched on my frustration with Maven and my interest in other build tools.  <a href="http://gradle.org/">Gradle</a> looked interesting (Grovy DSL with Ant integration).  I've been playing with building a Flex app, so I thought I would see if I could get Gradle to build it.  Since Adobe provides custom Ant tasks as part of its SDK distribution, it should be easy.  In fact, it is.</div><div>
</div><div>Assumptions:</div><div>
- You have downloaded the Adobe SDK (or Flex Developer)
- You have a sample Flex (or Air) app to build.
- You have Gradle downloaded and installed.
<div>The first step is to create a Gradle build file (<i>build.gradle</i>) in your Flex application directory.  To test your Gradle install, put a simple Hello World task:</div><div>
</div><div><i>task hello << { </i></div><div><i>  println "Hello World"</i></div><div><i>}</i></div><div>
</div><div>You can then run <i>gradle hello</i> from your command prompt.  It should echo back:</div><div>
</div><div><div><i>:hello</i></div><div><i>Hello World</i></div><div>
</div><div>Now you need to 'install' the <a href="http://livedocs.adobe.com/flex/3/html/help.html?content=anttasks_1.html">Flex Ant Task Jar</a>.  This can be found in your Flex SDK Install under the ant directory (sdk_install/ant).  There are a couple ways to install this.  The easiest is to put it in the lib directory under your GRADLE_HOME directory.  You can also specify the classpath in the taskdef command, but I'll leave that as an exercise for the reader...</div><div>
</div><div>Once you have the Flex Ant Tasks installed, you can create your Gradle build script.  Here is a straight foward compile script:</div><div>
</div><div><div><i>ant.FLEX_HOME="c:/Program Files/Adobe/flex_sdk_3"</i></div><div><i>
</i></div><div><i>ant.taskdef(resource: "flexTasks.tasks")</i></div><div><i>
</i></div><div><i>task compile << {</i></div><div><i>  ant.mxmlc(file: "src/Main.mxml") {    </i></div><div><i>  }</i></div><div><i>}</i></div><div>
</div><div>You will need to change the <i>FLEX_HOME</i> value and <i>Main.mxml</i> to your specific environment/app, but that is it.  You can then execute <i>gradle compile</i> from your command prompt and compile the application.</div><div>
</div><div>If it is an Air app, you will need to add <i>configname: "air"</i> to the mxmlc task definition so it uses the Air configuration.  Otherwise, you will likely see: <i>Unable to locate specified base class 'mx.core.WindowedApplication'</i></div></div><div>
</div><div>To build the Air package for your application, you will also need to call the script file included with the SDK.  You can find a sample of the ANT version of this <a href="http://www.adobe.com/cfusion/communityengine/index.cfm?event=showdetails&amp;postId=12175&amp;productId=2&amp;loc=en_US">here</a>.</div><div>
</div><div>This example is more a sample of how easily Ant tasks can be used in Gradle than the overall power of Gradle.  But it does demonstrate that Gradle can be used to build anything that has Ant tasks, and that is a great start.</div></div></div></div></div>
