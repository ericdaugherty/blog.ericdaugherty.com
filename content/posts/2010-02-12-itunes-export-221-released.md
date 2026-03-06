---
title: "iTunes Export 2.2.1 Released"
date: 2010-02-12T19:06:00Z
url: /2010/02/itunes-export-221-released.html
draft: false
---
iTunes Export exports playlists defined in your iTunes Music Library to standard .m3u, .wpl (Windows Media), .zpl (Zune), or .mpl  (Centrafuse) playlists. iTunes Export also supports copying the original music files  with the playlist to facilitate exporting to other devices.  iTunes Export is open source and freely available for use.

The 2.2.1 release features updates and bug fixes to the console and  GUI versions

In both versions:

- Enhanced the playlist name filter to include characters from the Latin 1  Supplement Block.
- Added(Console)/Changed(GUI) 'addIndex' logic.  Now uses incrementing  index instead of iTunes Song Index.  Index is in the order iTunes has  the songs in for each playlist.
For the Console version:

- Replaced ad-hoc URL decoding of file paths with URLDecode class.  Now  non-ASCII characters are handled correctly in file names.
If you find any issues or  have questions please email me (eric@ericdaugherty.com). Please include  which application and version (GUI or Console, 2.2.1 etc.) of iTunes  Export and the operating system you are using.
