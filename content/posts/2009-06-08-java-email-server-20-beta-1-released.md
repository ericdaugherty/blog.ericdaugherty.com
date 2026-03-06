---
title: "Java Email Server 2.0 Beta 1 Released"
date: 2009-06-08T02:17:00.001Z
url: /2009/06/java-email-server-20-beta-1-released.html
draft: false
---
There have been <a href="http://www.ericdaugherty.com/blog/2008/01/java-email-server-20-branch.html" target="_blank">multiple efforts</a> started over time to create a modernized version of JES (It is an 8 year old fork of an <a href="http://crsemail.sourceforge.net/" target="_blank">even older project</a>) that would incorporate features more or less expected from a up-to-date MTA/MDA. I'm happy to announce that Andreas Kyrmegalos has stepped forward and developed a heavily revised and augmented version of Java Email Server that will be released as 2.0 Beta 1. Staying true to a gui-less configuration approach hasn't prevented a host of new features to be introduced.<div class="im">
While the changes are too numerous to cover in this announcement, I wanted to highlight a few of the more important changes:
</div>
- TLS/SSL Support
- Configurable sandboxing
- Support for white/blacklisting
- Support for spam filtering/virus checking via amavisd-new using a dual MTA approach
- Data directories are now configurable (incoming/outgoing email storage)
- New Service Wrapper (Tanuki Java Service Wrapper)
- More efficient mail dispatching to multiple users at a single domain
- Cleaner shutdown process
- Mail transactions with mail servers employing reverseDNS checks (useful for JES instances on a dynamic IP)
- More efficient memory handling
- On the fly POP3/SMTP port listening switching
- Interfaces to enable extension modules
- Migration tool for JES 1.6.1
- Introduction of an automated testing framework
- Improved MIME header parsing support
- 8BITMIME, SIZE extensions support
- SASL MD5-DIGEST, GSS-API support
- and MUCH MUCH more.
<div class="im"> JES is now dependent on JDK 1.5. The existing 1.6.x branch will continue to be available to support JDK 1.4.

</div> Project management is being carried out using Maven.

JES is also getting a new license. The existing GPL license was due to the original GPL license of <a href="http://crsemail.sourceforge.net/" target="_blank">CRSMail</a>.  CRSMail has now been <a href="http://sourceforge.net/forum/forum.php?forum_id=420204" target="_blank">released into the public domain,</a> allowing JES to be re-licensed under a BSD Style license.
<div class="im">
I am also launching a new <a href="http://groups.google.com/group/java-email-server">Google Group</a> to facilitate a more open support structure. Please post all questions about JES to <a href="http://groups.google.com/group/java-email-server">this group</a>.

</div> This initial release is a Beta. It has been used in production environments, tested under Windows XP, Ubuntu and Windows Vista on single and multi core systems and should be solid, but it is possible that some issues may exist with specific configurations/environments. I encourage everyone to give this a try and provide feedback. The goal of this version is to provide a much needed step forward for JES while retaining the simplicity and ease of configuration and deployment. Let us know if this release achieves the goal.

The 2.0 Beta 1 release is available to download from the JES Home Page and a version 2 branch resides at sourceforge's subversion repository. Give it a spin and post your comments in the <a href="http://groups.google.com/group/java-email-server">Google Group</a>.
