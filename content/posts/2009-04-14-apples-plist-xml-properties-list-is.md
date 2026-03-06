---
title: "Apple's plist XML (Properties List) is PAINFUL"
date: 2009-04-14T23:05:00.002Z
url: /2009/04/apples-plist-xml-properties-list-is.html
draft: false
---
I started poking around with Scala and tried to re-implement the iTunes Music Library parser <a href="http://www.ericdaugherty.com/dev/itunesexport/">I wrote in .Net</a> as a <a href="http://www.scala-lang.org/">Scala</a> library to give me a real problem to solve.  This effort reminded me of how painful Apple's plists are to work with.

Apple saves the iTunes Library information in a binary file and as well as an XML file using its <a href="http://developer.apple.com/documentation/Darwin/Reference/ManPages/man5/plist.5.html">plist format</a>.  It is great that the provide the XML data that enables tools like <a href="http://www.ericdaugherty.com/dev/itunesexport/">iTunesExport</a>, but they certainly could have made working with the XML easier.

Simply put, they store key value pairs as:
<blockquote>&lt;key&gt;Artist&lt;/key&gt;&lt;string&gt;U2&lt;/string&gt;</blockquote>Three is no clean way to associate the 'value' with a 'key' other than the order of the nodes in XML.  This makes things like XPath parsing very difficult.

For a more in depth explanation, <a href="http://www.cakoose.com/wiki/plist_xml_is_pointless">read this post</a>.

I was able to get the Scala library to parse the plist but it wasn't as clean as I hoped.  If I stay motivated I may finish up a Scala version of the tool to provide a version that will work on OS X (Scala compiles down to Java classes).
