---
title: "Getting Started with GraniteDS, Spring, and Maven"
date: 2010-01-22T21:43:00.003Z
url: /2010/01/getting-started-with-graniteds-spring.html
draft: false
---

This is a quick tutorial to get you up and running using <a href="http://www.graniteds.org/">GraniteDS</a>, Spring, and Maven.  My initial assumptions are that you already have a Spring project up and running using Spring WebMVC, and you want to add GraniteDS to the project to enable a Flex client.  This just covers using GraniteDS for a basic RPC call using AMF.  GraniteDS does much more, but this should at least get you started.<br /><br />First, you need to add the GraniteDS dependencies to your pom.  GraniteDS does not appear to be in the default Maven repository, so first you need to add a references to the Java.net Maven Repository:

```xml
<repositories>
  <repository>
    <id>Java.net</id>
    <name>Java.net Repository</name>
    <url>http://download.java.net/maven/2/</url>
  </repository>
</repositories>
```

Next, you'll need to add the dependencies:

```xml
<dependency>
  <groupId>org.graniteds</groupId>
  <artifactId>granite-core</artifactId>
  <version>2.0.0.GA</version>
</dependency>
<dependency>
  <groupId>org.graniteds</groupId>
  <artifactId>granite-spring</artifactId>
  <version>2.0.0.GA</version>
</dependency>
```
You may also want to add additional GraniteDS artifacts, such as granite-hibernate, etc.  You can see the entire list <a href="http://download.java.net/maven/2/org/graniteds/">here</a>.<br /><br />You will need two additional configuration files, services-config.xml and granite-config.xml.  The services-config.xml should be familiar to anyone who has used BlazeDS before.<br /><br />WEB-INF/flex/services-config.xml - This file contains the core of the mapping config.  The first block specifies the destination, including the beanName of the backing Spring Bean.  You will need to replace [beanName] with the name of the Spring Bean you are exposing.  You can tweak the URL and destination names, but otherwise this should be good for your simple RPC call as is.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<services-config>

  <services>
    <service
        id="granite-service"
        class="flex.messaging.services.RemotingService"
        messageTypes="flex.messaging.messages.RemotingMessage">
      <destination id="test">
        <channels>
          <channel ref="my-graniteamf"/>
        </channels>
        <properties>
          <factory>springFactory</factory>
          <source>[beanName]</source>
        </properties>
      </destination>
    </service>
  </services>

  <factories>
    <factory id="springFactory"
             class="org.granite.spring.SpringServiceFactory"/>
  </factories>

  <channels>
    <channel-definition id="my-graniteamf" class="mx.messaging.channels.AMFChannel">
      <endpoint
          uri="http://{server.name}:{server.port}/{context.root}/graniteamf/amf"
          class="flex.messaging.endpoints.AMFEndpoint"/>
    </channel-definition>
  </channels>

</services-config>
```
Note: If you are using AutoWiring in Spring, the beanName will just be the unqualified class name.  So the class com.ericdaugherty.TestService would have a beanName: testService.<br /><br />WEB-INF/granite/granite-config.xml - In this simple example, there is no configuration of real value in this file yet.  As you delve deeper into GraniteDS's features, you can add configuration here.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE granite-config PUBLIC
    "-//Granite Data Services//DTD granite-config internal//EN"
    "http://www.graniteds.org/public/dtd/1.2.0/granite-config.dtd">

  <granite-config scan="true">
</granite-config>
```
You will need to add some additional configuration to your web.xml.  In addition to your SpringMVCServlet configuration, you will need the GraniteDS Filter and Servlet:

```xml
<context-param>
  <param-name>contextConfigLocation</param-name>
  <param-value>
    /WEB-INF/config/web-application-config.xml
  </param-value>
</context-param>

<listener>
  <listener-class>
    org.springframework.web.context.ContextLoaderListener
  </listener-class>
</listener>

<filter>
  <filter-name>AMFMessageFilter</filter-name>
  <filter-class>
    org.granite.messaging.webapp.AMFMessageFilter
  </filter-class>
</filter>
<filter-mapping>
  <filter-name>AMFMessageFilter</filter-name>
  <url-pattern>/graniteamf/*</url-pattern>
</filter-mapping>

<servlet>
  <servlet-name>AMFMessageServlet</servlet-name>
  <servlet-class>
    org.granite.messaging.webapp.AMFMessageServlet
  </servlet-class>
  <load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
  <servlet-name>AMFMessageServlet</servlet-name>
  <url-pattern>/graniteamf/*</url-pattern>
</servlet-mapping>
```
I had to add the ContextLoadListener and specify the location of my web-application-config.xml file for GraniteDS to work, even though I didn't need it for Spring.<br /><br />Note: if your SpringMVCServlet is mapped to your root (/), make sure the AMFMessageServlet mapping is first in your XML file.<br /><br />Now, you simply need to create a Flex project and use RemoteObject to call your service.  In Flash Builder 4, I was able to set it up as a BlazeDS project, point it at the src/main/webapp directory in my Maven tree, and it was able to auto-configure RemoteObject.<br /><br />That's it.  This is a very simple version of what you can do with GraniteDS, but it should be enough to get you started.
