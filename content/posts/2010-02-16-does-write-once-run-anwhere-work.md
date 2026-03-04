---
title: "Does Write Once Run Anywhere Work?"
date: 2010-02-16T14:05:00.002Z
url: /2010/02/does-write-once-run-anwhere-work.html
draft: false
---

Yes, and No.<br />
<br />
Write Once, Run Anywhere, a <a href="http://en.wikipedia.org/wiki/Write_once,_run_anywhere">slogan created by Sun</a> to evangelize the virtues of the Java Platform, is a controversial approach to software development.<br />
<br />
Write Once, Run Anywhere (WORA) is accomplished through an abstraction layer between the 'compiled code' and the operating system and processor.&nbsp; This abstraction usually takes the form of a Virtual Machine or Runtime, such as the <a href="http://en.wikipedia.org/wiki/Java_Virtual_Machine">Java Virtual Machine</a> (JVM), <a href="http://en.wikipedia.org/wiki/Common_Language_Runtime">Microsoft's Common Language Runtime</a> (CLR), <a href="http://en.wikipedia.org/wiki/Flash_player">Flash Player</a> (or <a href="http://en.wikipedia.org/wiki/Adobe_Integrated_Runtime">Air runtime)</a>, or one of the many interpreted language runtimes (Perl, PHP, Ruby, etc.).&nbsp; These runtimes convert the intermediate language into device specific code that can execute on the local operating system and processor.&nbsp; While this overhead introduces extra steps, which slow down execution, they also provide features not (easily) available in native code, such as garbage collection and Just In Time (JIT) compilers which can optimize the code while it executes, as opposed to at compilation time.<br />
<br />
So does it work?&nbsp; Yes, and No.<br />
<br />
<span style="font-size: large;">Server</span> <br />
<br />
WORA languages have achieved a significant level of success on the server side.&nbsp; Code that runs on large servers and interacts with clients over HTTP or other protocols is almost always written in some form of WORA, whether it is Java, .Net, PHP, Ruby, Perl, or other interpreted languages.&nbsp; There is no advantage to using native code in these cases.&nbsp; All interactions with the user are through an intermediate protocol/interface, such as HTML over HTTP for websites, XML over HTTP for web services, or various other formats and protocols used to exchange information between servers and clients or other servers.<br />
<br />
There are certainly some applications developed for servers in native code.&nbsp; Database servers are the most common example, but LDAP servers, webservers (Apache), and others are compiled to native code.&nbsp; However, there are WORA versions of each of these examples, and many of the native applications were first written before WORA languages took off. <br />
<br />
There is no denying that WORA is a huge success on the server side.<br />
<br />
<span style="font-size: large;">Client</span><br />
<br />
Which brings us to No.<br />
<br />
Client application development has struggled on the client side.&nbsp; The biggest challenge is <a href="http://en.wikipedia.org/wiki/Human_interface_guidelines">User/Human Interface Guidelines</a> (HIG).&nbsp; User or Human interface guidelines are published by various Operating System vendors (<a href="http://msdn2.microsoft.com/en-us/library/Aa511258.aspx">Microsoft</a>, <a href="http://developer.apple.com/mac/library/documentation/UserExperience/Conceptual/AppleHIGuidelines/XHIGIntro/XHIGIntro.html">Apple</a>) that define a set of recommendations on how an application should look and interact with the user.&nbsp; Applications that follow these look like 'Windows' or 'Mac' applications.<br />
<br />
With WORA, application developers have two choices.&nbsp; Follow the guidelines of a specific platform, and ignore the others, or compromise between the various target platforms, creating an application that doesn't match any platform.&nbsp; <br />
<br />
Early Java desktop applications looked like Java applications.&nbsp; They were obviously different from the other applications that users were used to interacting with, and were often shunned.&nbsp; This has led to a negative view of WORA applications in general, as John Gruber <a href="http://daringfireball.net/linked/2010/02/15/kincaid">comments</a> on a Jason Kincaid <a href="http://techcrunch.com/2010/02/15/wholesale-applications-community-fail/">article</a>:<br />
<blockquote>Jason Kincaid nails it: “write once, run everywhere” has never worked  out. It’s a pipe dream. </blockquote>In the context of client applications, I have to (mostly) agree.<br />
<br />
There are exceptions.&nbsp; In the Java world, nearly every developer uses an Integrated Development Environment written in Java, whether it is Eclipse, IntelliJ IDEA, or NetBeans.&nbsp; But developers are a very different target audience than general computer users.<br />
<br />
Another example is Flash and Flex applications.&nbsp; Often delivered in the web browser, there are no real Human Interface Guideline that govern their interactions, other than the expected HTML experience.&nbsp; This can work, but it can also be horribly painful, as many people have discovered trying to find a menu on a Restaurant's website.&nbsp; <br />
<br />
<span style="font-size: large;">Mobile</span><br />
<br />
There is a third act to this story.&nbsp; Mobile.<br />
<br />
Apple has take the mobile market by storm with its iPhone and App Store. &nbsp; With <a href="http://www.macrumors.com/c.php?u=http%3A%2F%2Fwww.apple.com%2Fpr%2Flibrary%2F2009%2F11%2F04appstore.html&amp;t=1266226853">over 100,000 applications</a> written for the iPhone, the iPhone has become THE mobile development platform.&nbsp; And every one of these applications was compiled to native code.<br />
<br />
A consistent user experience is even more important on a mobile device with a limited display and user input capability.&nbsp; Apple's success is in part due to its consistent device design.&nbsp; Every iPod/iPod Touch/iPad version has a single home button, and a touch screen.&nbsp; There are two screen sizes, the iPod size, and the iPad size.&nbsp; While individual phone capabilities do very (memory, speed, GPS, Compas, etc.) the primary interface components are all the same. &nbsp; By using a software keyboard on the devices, the keyboard is the same across all devices and applications.&nbsp; All of this makes developing applications for the platform much more predictable and enjoyable.<br />
<br />
The Windows Mobile and Android platforms both share a wide variety of device form factors, screen sizes, physical buttons, and device features.&nbsp; This makes it much more difficult to build an application that is easy and intuitive to use across the platform.&nbsp; And I think the quality and quantity of applications on the Windows Mobile and Android platforms demonstrate this point.<br />
<br />
<span style="font-size: large;">Solution</span><br />
<br />
There is a solution, of sorts.&nbsp; HTML in the browser is the most successful WORA language and runtime for client applications since the <a href="http://www.termsys.demon.co.uk/vtansi.htm">ANSI/VT100 terminal</a>.&nbsp; By creating a common language and interface, applications could be written for all operating systems easily, without the pain of violating their human interface guidelines.&nbsp; The browser itself conformed to the local guidelines, and users expected the experience in the browser to be different from a native application.<br />
<br />
It is time to evolve this paradigm to the next level.&nbsp; <span style="font-size: small;"><a href="http://en.wikipedia.org/wiki/HTML5">HTML 5</a></span> is a good first step.&nbsp; It provide the ability to display video, store data locally, and draw 2D graphics in a standardized way.&nbsp; But to be successful, these features and more need to be implemented consistently across browsers, enabling developers to truly develop great WORA client applications.<br />
<br />
As an intermediate step, frameworks and libraries that abstract the browser differences away is a short term solution.&nbsp; JavaScript libraries such as <a href="http://www.prototypejs.org/">Prototype</a> and <a href="http://jquery.com/">jQuery</a> abstract the browser implementation differences while frameworks like <a href="http://code.google.com/webtoolkit/">Google's Web Toolkit</a> (GWT) provide a platform to develop client applications that just happen to run in the browser.<br />
<br />
Realistically, I think tools like GWT are the future.&nbsp; As a Flex developer, I enjoy the ability to quickly and easily create rich applications that will render the same on ever user's machine.&nbsp; But I would prefer that the Flex applications would compile to HTML and JavaScript, so they could be run native in the browser.<br />
<br />
In the future, we will be developing using various language and platforms, but they will all compile down to code that runs native in the browser.&nbsp; Or so I hope.
