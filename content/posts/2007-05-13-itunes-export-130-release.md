---
title: "iTunes Export 1.3.0 Release"
date: 2007-05-13T20:50:00Z
url: /2007/05/itunes-export-130-release.html
draft: false
---
I released a new version of my iTunes Export utility.

iTunes Export exports your iTunes playlists as M3U or WPL files, allowing you to setup playlists in iTunes and use them with other software or devices.

This release is mainly due to the efforts of <a href="http://jeff.donnici.com">Jeff Donnici</a>.  He has done great work on the code base and is helping move iTunes Export forward.

The major fix in this release is for internationalization (i18n).  Apparently you need to use the m3u8 file extension instead of m3u on non-US versions of Windows for the file to be interpreted correctly.  Thanks to all the help from the many users who emailed us about this issue and helped us track it down.  It was actually <a href="http://www.wikipedia.org/">Wikipedia</a> that finally gave us the key clue in its <a href="http://en.wikipedia.org/wiki/M3U">m3u </a>article.

Jeff also added several other fixes (see the <a href="http://www.ericdaugherty.com/dev/itunesexport/changes.html">change log</a>), and is already hard at work on the next release.

<a href="http://www.ericdaugherty.com/dev/itunesexport/">http://www.ericdaugherty.com/dev/itunesexport/</a>

I have received several new feature requests and bug reports recently and I plan on getting to them soon. Don't be afraid to ask for new features (eric@ericdaugherty.com).
