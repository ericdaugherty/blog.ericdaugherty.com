---
title: "Parsing PList files in ActionScript"
date: 2009-10-10T01:16:00.006Z
url: /2009/10/parsing-plist-files-in-actionscript.html
draft: false
---
The PList format is not one of my favorites.  I've <a href="http://www.ericdaugherty.com/blog/2009/04/apples-plist-xml-properties-list-is.html">complained about it before</a>, but Apple continues to use it for its iTunes library information, so I continue to parse it.<div>
</div><div>I've been exploring the option of porting the iTunesExport project to Flex (Air) to provide a cross platform version.  The current version is written in .Net and therefore not usable on OS X. As such I needed to parse the PList file using ActionScript.  I adopted the Java PList Parser written by Christoffer Lerno for his <a href="http://code.google.com/p/xmlwise">XMLWise project</a>.</div><div>
</div><div>The dynamic nature of ActionScript resulted in a much smaller implementation (although I did skip over 'REAL' and 'DATA' types), and makes it easy to consume.</div><div>
</div><div>You can view or download my version <a href="http://www.ericdaugherty.com/dev/itunesexport/PListParser.as">here</a>, released under the MIT license.</div><div>
</div><div>Here is a snapshot of how it is used:</div><div>

```
actionscript
var parser:PListParser = new PListParser();
var pList:Object = parser.parsePList(xml);

playlists = pList.Playlists.filter(filterPlaylists);

```
The last line accesses the Playlist array (dynamically created when the PList is parsed), and filters it using the specified filterPlaylists method, returning a filtered list of the playlists from the original XML file.</div><div>
</div><div>It provides easy structured access to an XML file that would otherwise be difficult to access in a rational manner.</div>
