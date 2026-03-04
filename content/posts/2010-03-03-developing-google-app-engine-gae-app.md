---
title: "Developing a Google App Engine (GAE) app using Maven"
date: 2010-03-03T14:16:00Z
url: /2010/03/developing-google-app-engine-gae-app.html
draft: false
---

If you want to develop a Google App Engine (GAE) application using Maven, you can either use the Maven plugin <a href="http://code.google.com/p/maven-gae-plugin/">maven-gae-plugin</a>, which requires non-trivial hacking on your pom.xml, or you can keep your pom clean and create a simple Ant script.<br />
<br />
My pom is a simple web application pom, with no specific GAE configuration.&nbsp; I then created a build.xml in my project root that looks like this:<br />
<pre class="brush: xml">&lt;project&gt;
  &lt;property name="sdk.dir" location="/opt/appengine-java-sdk-1.3.1" /&gt;

  &lt;import file="${sdk.dir}/config/user/ant-macros.xml" /&gt;

  &lt;target name="runserver" depends=""
      description="Starts the development server."&gt;
    &lt;dev_appserver war="target/yourappname-1.0-SNAPSHOT" /&gt;
  &lt;/target&gt;

&lt;/project&gt;</pre><br />
Using this, you can run your application in the GAE sandbox without having it take over your pom.<br />
<br />
You can also have the ant task perform a maven package to insure everything is updated by adding an exec target to the runserver task.<br />
<br />
You can read more about the <a href="http://code.google.com/appengine/docs/java/tools/ant.html">full range of Ant tasks available for GAE</a>, but I found this simple script helpful to get up and running quickly in the GAE sandbox without much effort.
