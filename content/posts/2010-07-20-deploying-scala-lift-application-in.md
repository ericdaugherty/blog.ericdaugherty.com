---
title: "Deploying a Scala Lift Application in an OSGi Container"
date: 2010-07-20T12:30:00.002Z
url: /2010/07/deploying-scala-lift-application-in.html
draft: false
---

My current project involves building a <a href="http://www.liftweb.net/">Lift</a> web application and deploying it in our OSGi application container.&nbsp; I've been working with <a href="http://www.scala-lang.org/">Scala</a> on and off for a while, and I've always been interested in Lift.&nbsp; With the release of Scala 2.8 and Lift 2.0, I decided it was time to give Lift a real try on my current project.&nbsp; <br />
<br />
The easiest way to deploy a WAR file is using Pax Web's <a href="http://wiki.ops4j.org/display/paxweb/WAR+Extender">War Extender</a>.  This allows you to simply deploy a WAR file with an updated MANFIEST.MF file (making it an OSGi Bundle) in the same container as Pax Web.  In my example I will build a WAR file as a standard OSGi Plugin and build it using Eclipse, but you could also build a normal WAR file using Maven or SBT and add the OSGi attributes to the MANIFEST.MF file and deploy it with Pax Web.<br />
<br />
The following steps assume:<br />
<ul><li>Eclipse is the IDE</li>
<li><a href="http://www.scala-ide.org/">Scala-IDE</a> (Scala Plugin) is installed.</li>
<li>Scala 2.8</li>
<li>Lift 2.0 (Need the Scala 2.8 Snapshot from <a href="http://scala-tools.org/repo-snapshots/net/liftweb/">Scala-Tools</a>)</li>
</ul>The first step was to create a standard OSGi Plug-In Project.&nbsp; Then edit the project file to add the Scala Build Command

```xml
<buildcommand>
  <name>ch.epfl.lamp.sdt.core.scalabuilder</name>
</buildcommand>
```
to buildSpec, and remove the Java Builder<br />
<br />
Then add the Scala Nature

```xml
<nature>ch.epfl.lamp.sdt.core.scalanature</nature>
```
to natures.  I added both to the top of the respective sections.<br />
<br />
You will then need to reload the Project (Close/Reopen) and it should be Scala-enabled.<br />
<br />
I then merged the <a href="http://www.liftweb.net/lift.zip">Lift Template</a> project into my Eclipse Project.&nbsp; I copied the src/main/scala directory into my src directory, and src/main/webapp into the project root.<br />
<br />
At this point Eclipse should see the Scala source files, but they will not compile as the Lift libraries are not yet in the classpath.<br />
<br />
I downloaded the required dependencies from the various Maven repositories and added them to the WEB-INF/lib directory.&nbsp; For my initial project I needed:<br />
<ul><li>joda-time</li>
<li>lift-actor</li>
<li>lift-common</li>
<li>lift-json</li>
<li>lift-util</li>
<li>lift-webkit</li>
<li>paranamer-generator</li>
<li>slf4j</li>
<li>org.apache.commons.fileupload</li>
</ul>Remember, if you are using Scala 2.8 to download the 2.8.0 version of the lift libraries (which are currently under snapshots instead of releases).&nbsp; Once you have all the dependencies, the Lift sample code should compile.<br />
<br />
You can now work on deploying the bundle.<br />
<br />
You will need the Pax Web WAR Extender bundle and all its dependencies.&nbsp; They can be found in this <a href="http://repo1.maven.org/maven2/org/ops4j/pax/web/">Maven Repo</a>, and are outlined <a href="http://wiki.ops4j.org/display/paxweb/Pax+Web+-+0.7.1">here for version 0.7.1</a>.<br />
<br />
Once the Pax Web bundles are deployed, you should be able to deploy your bundle.&nbsp; The Pax Web WAR Extender will scan all bundles for a web.xml file and attempt to deploy them if it finds one.<br />
<br />
By default it uses the Bundle's Symbolic Name (Bundle-SymbolicName: xxx) as the context root, but you can specify your own by adding the following line to your MANIFEST.MF:

```
Webapp-Context: /
```
to deploy as the root context or

```
Webapp-Context: mycontext
```
to deploy as /mycontext<br />
<br />
That was all it took to get a sample Lift application up and running.  I can now use the OSGi container to reference other dependencies and continue to build the application in Eclipse.<br />
<br />
A couple of notes:<br />
You can deploy the Lift libraries and dependencies as OSGi bundles instead of in the WEB-INF/lib directory of the bundle.  At the time of this writing, the Lift OSGi Bundles were not available for 2.8 yet, but all they need are an updated MANIFEST.MF file.<br />
<br />
As I noted at the beginning, you can simply edit the MANIFEST.MF file of any WAR and deploy it this way.  If your Lift app does not depend on other OSGi bundles this may be the easiest approach.
