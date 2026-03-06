---
title: "iTunes Export 2.0 - Now Supports OS X!"
date: 2009-11-03T22:28:00.002Z
url: /2009/11/itunes-export-20-now-supports-os-x.html
draft: false
---
This release of iTunes Export marks a milestone and major transition of the development focus.  The prior releases, 1.0-1.6 were all build using the Microsoft .Net Framework, which limited deployment to Windows.  With this release, iTunes Export now fully support Windows and Mac OS X.

The Graphical User Interface version has been ported to <a href="http://www.adobe.com/products/flex/">Adobe Flex</a> and is deployed as an <a href="http://www.adobe.com/products/air/">AIR</a> desktop application.  The Command Line version is an update of the Scala version I <a href="http://www.ericdaugherty.com/blog/2009/05/itunes-export-scala-02-released.html">developed earlier this year</a>.

iTunes Export exports your iTunes playlists as M3U, WPL, ZPL, and MPL files, allowing you to setup playlists in iTunes and use them with other software or devices.

The primary focus of this release was to enable Mac OS X support.  However, in addition to this, the copy files (songs) logic has been revamped.  There are now three options:
 - FLAT - Copies all the songs into the output directory
 - ITUNES - Retains the iTunes structure (Artist/Album)
 - PLAYLIST - The 'original' copy logic that copies the songs into a directory per playlist.

The new version can be downloaded from the project homepage:  <a href="http://www.ericdaugherty.com/dev/itunesexport/">http://www.ericdaugherty.com/dev/itunesexport/</a>

As this is a major new release, please keep an eye out for any bugs or issues that may appear.  If you find any issues or have questions please email me (eric@ericdaugherty.com).  Please include which application and version (GUI or Console, 2.0 etc.) of iTunes Export and which Operating System version.
