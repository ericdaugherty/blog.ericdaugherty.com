---
title: "Java Email Server 2.0 Beta 2 Released"
date: 2009-09-26T17:25:00.001Z
url: /2009/09/java-email-server-20-beta-2-released.html
draft: false
---
<a href="http://www.ericdaugherty.com/java/mailserver">Java Email Server</a> (JES) is an open source email server (SMTP/POP3) written in Java.<div>
</div><div>This release is the second Beta version of the new 2.0 development branch.    This is an incremental update to Beta 1 and contains the following updates:</div><div><div>
- Truly decoupled dependency on log4j. See section "Logging Facility" in AdditionalNotes.txt.
- Server instance now uses a singleton pattern.
- Added an option ("testing.destination") that, when set, directs all outgoing messages to the destination (currently a folder).
- Each domain gets its own default user.
- A profile can now be set for the services to be activated at startup. The profile is broken down into Mail Transfer Mode and Mail Retrieval Mode. Resource allocation is affected, but not considerably.
<div>Please read the <a href="http://www.ericdaugherty.com/blog/2009/06/java-email-server-20-beta-1-released.html">Beta 1 Post</a> for the other 2.0 branch changes.</div><div>
</div><div>While the belief is that JES 2.0 Beta 2 is stable, we will continue with Beta releases in the 2.0 branch until we feel confident that the 2.0 code is stable and production safe.  Please provide feedback on this release in the <a href="http://groups.google.com/group/java-email-server">JES Google Group</a>, even if it is just letting us know you are using JES without any issues.</div><div>
</div><div>You can download this release from the <a href="http://www.ericdaugherty.com/java/mailserver/">project home page</a>.</div></div></div>
