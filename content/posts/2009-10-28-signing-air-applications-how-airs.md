---
title: "Signing AIR Applications: How AIR's Certificate Requirement Complicates Open Source Development"
date: 2009-10-28T14:21:00.005Z
url: /2009/10/signing-air-applications-how-airs.html
draft: false
---
Adobe AIR is the desktop runtime environment for deploying Flex applications.  The main difference between a Flex application and an AIR application is that AIR applications are installed locally and have additional access to local resources, including the local file system, while a Flex application runs in the browser and is 'sandboxed'.<div>
</div><div>I've been developing an AIR version of my <a href="http://www.ericdaugherty.com/dev/itunesexport/">iTunes Export</a> open source application.  The original version was developed in .Net, making it Windows only.  The AIR version will work across Windows and OS X, and will replace the existing .Net GUI.</div><div>
</div><div>As I prepare to release the first Beta I ran into the question of how to sign my AIR application.  All Adobe Air applications must be signed using a digital certificate.  There are a few companies that sell certificates that are recognized by Windows and OS X by default, and they charge $300/year and up.  That is pocket change for any company selling an application but a pretty significant cost for an open source application that produces no revenue.</div><div>
</div><div>You can self-sign a certificate, but you are then presented with this dialog box:</div><div>
</div><div><img src="http://www.ericdaugherty.com/images/AIRUnknownPublisher.jpg" />
</div><div>
</div><div>If you want to avoid this dire warning, you must buy a certificate from one of the Root Certificate Authorities.</div><div>
</div><div>So what do I do?  I'm tempted to release it using a self-signed certificate.  The warning is annoying, but I've been releasing the .Net version unsigned for years, and it had as much or more 'destructive capability'.  However, the users also were not faced with this warning dialog.</div><div>
</div><div>It would be nice if there was an 'Open Source' Certificate Authority (CA), that allowed open source projects access to free certificates, but the costs involved in becoming a Root CA and managing the issuance of certificates would require a very generous patron.</div><div>
</div><div>If you are looking for step by step instructions on HOWTO sign an AIR application, check out this <a href="http://www.adobe.com/devnet/air/articles/signing_air_applications.html">tutorial</a>.</div>
