---
title: "Using Tycho to Build an OSGi Project"
date: 2010-10-22T01:00:00.001Z
url: /2010/10/using-tycho-to-build-osgi-project.html
draft: false
---

I recently migrated the build process for an application from a monolithic <a href="http://www.eclipse.org/buckminster/">Eclipse Buckminster</a> build to a <a href="http://maven.apache.org/">Maven</a> build using <a href="http://tycho.sonatype.org/">Tycho</a>.&nbsp; Our source code was componentized and runs in an OSGi container, but our build was not, making it difficult to version each component individually.<br />
<br />
Because all of our OSGi meta-data was already stored in the OSGi MANIFEST.MF files, we wanted a built process that would leverage that investment, while providing us the flexibility and functionality&nbsp; a generalized build tool provides.&nbsp; Maven and Tycho fit the bill.<br />
<br />
Tycho is only supported on Beta releases of Maven 3.&nbsp; We used Beta 2 for our build.&nbsp; Tycho is simply installed as a build plugin, so all you need to get started is the Beta release of Maven 3. <br />
<br />
The Maven/Tycho setup is pretty simple.&nbsp; We defined a parent POM that provided the Tycho dependency, the child modules to build, and the P2 Update Sites that provided any dependencies needed by the component.&nbsp; The Tycho part of the config looked like:<br />
<br />
<pre class="brush: xml">&lt;build&gt;
&lt;plugins&gt;
  &lt;plugin&gt;
    &lt;groupId&gt;org.sonatype.tycho&lt;/groupId&gt;
    &lt;artifactId&gt;tycho-maven-plugin&lt;/artifactId&gt;
    &lt;version&gt;${tycho.version}&lt;/version&gt;
    &lt;extensions&gt;true&lt;/extensions&gt;
  &lt;/plugin&gt;
  &lt;plugin&gt;
    &lt;groupId&gt;org.sonatype.tycho&lt;/groupId&gt;
    &lt;artifactId&gt;target-platform-configuration&lt;/artifactId&gt;
    &lt;version&gt;${tycho.version}&lt;/version&gt;
    &lt;configuration&gt;
      &lt;resolver&gt;p2&lt;/resolver&gt;
    &lt;/configuration&gt;
  &lt;/plugin&gt;
  &lt;plugin&gt;
    &lt;groupId&gt;org.sonatype.tycho&lt;/groupId&gt;
    &lt;artifactId&gt;maven-osgi-packaging-plugin&lt;/artifactId&gt;
    &lt;version&gt;${tycho.version}&lt;/version&gt;
    &lt;configuration&gt;
      &lt;format&gt;'${build.qualifier}'&lt;/format&gt;
    &lt;/configuration&gt;
  &lt;/plugin&gt;      
&lt;/plugins&gt;&nbsp;</pre><pre class="brush: xml">&lt;/build&gt; </pre><br />
We used Tycho version 0.9.0 for our build.&nbsp; The build.qualifier allows a Source Control revision number or other number to be used for SNAPSHOT or incremental builds.&nbsp; This value replaces the .qualifier part of the OSGi version number string.<br />
<br />
For each component we use the 'package' Maven build command, which produces an P2 Update Site.&nbsp; When other components have dependencies on a component, it references its update site in the parent pom file.&nbsp; This looks something like this:<br />
<br />
<pre class="brush: xml">&lt;repositories&gt;</pre><pre class="brush: xml">&nbsp; &lt;repository&gt;</pre><pre class="brush: xml">&nbsp;&nbsp;&nbsp; &lt;id&gt;newco-core&lt;/id&gt;
&nbsp;&nbsp;&nbsp; &lt;url&gt;http://updatesite.newco/dev/component/branch&lt;/url&gt;
&nbsp;&nbsp;&nbsp; &lt;layout&gt;p2&lt;/layout&gt;
&nbsp; &lt;/repository&gt;</pre><pre class="brush: xml">&lt;/repositories&gt;
</pre><br />
This allows us to version and build each component individually.&nbsp; We can then mix/match the P2 Update Sites that are created to produce custom aggregate sites that can be tailored as needed.&nbsp; We currently used the P2 Mirror Ant task to produce the composite sites. <br />
<br />
The pom file for each OSGi module or feature is trivial.&nbsp; It is just a reference to the parent project, and the type of OSGi module that it is.&nbsp; Here is a sample:<br />
<br />
<pre class="brush: xml">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
&nbsp;&nbsp;&nbsp; xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;
&nbsp; &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
&nbsp; &lt;parent&gt;
&nbsp;&nbsp;&nbsp; &lt;artifactId&gt;myComponent&lt;/artifactId&gt;
&nbsp;&nbsp;&nbsp; &lt;groupId&gt;com.ericdaugherty&lt;/groupId&gt;
&nbsp;&nbsp;&nbsp; &lt;version&gt;1.0.0-SNAPSHOT&lt;/version&gt;
&nbsp;&nbsp;&nbsp; &lt;relativePath&gt;../pom.xml&lt;/relativePath&gt;
&nbsp; &lt;/parent&gt;
&nbsp; &lt;groupId&gt;com.ericdaugherty&lt;/groupId&gt;
&nbsp; &lt;artifactId&gt;com.ericdaugherty.myComponent&lt;/artifactId&gt;
&nbsp; &lt;version&gt;1.1.0-SNAPSHOT&lt;/version&gt;
&nbsp; &lt;packaging&gt;eclipse-plugin&lt;/packaging&gt;
&lt;/project&gt;
</pre><br />
So now we can build each of our 'components' individually, without making a change to our development process.&nbsp; Our development teams continue to maintain the configuration and dependencies in the OSGi MANFIEST.MF files.<br />
<br />
We ran into a few bumps in the road along the way, but were always able to resolve it in a way that both Eclipse and Tycho accepted. <br />
<br />
Overall, I'm very happy with the result.&nbsp; We can now compile a wider range of projects (including Scala) that we could not build before with Buckminster, and have much more fine grained control.
