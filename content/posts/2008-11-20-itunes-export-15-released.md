---
title: "iTunes Export 1.5 Released"
date: 2008-11-20T02:39:00.003Z
url: /2008/11/itunes-export-15-released.html
draft: false
---
A new version of my iTunes Export utility is available.

iTunes Export exports your iTunes playlists as M3U, WPL, or ZPL files, allowing you to setup playlists in iTunes and use them with other software or devices.

This release adds several fixes and enhancements that have build up in the last few months.  They include:

Fixed issue with invalid characters in playlist filenames. Some characters are valid in playlist names (within iTunes), but not valid in filenames for the resulting playlist files.  Thanks to <a href="http://jeff.donnici.com">Jeff Donnici</a>.

Added Multi-Language support for GUI version.  Descriptions now available in English and French.  Thanks to Ayack for the translation.

Updated the Library reader and all playlist writers to use UTF-8 encoding to allow for foreign character sets.  Thanks to Stephen JANNIN for the patch.

Changed the export routine to include audio streams (files that start with http://).  However, it will not attempt to copy them if 'copy music' is selected.

Disabled tracks (tracks that are unchecked in iTunes) are now ignored.  Thanks to Jeroen Leijen for the suggestion.

<a href="http://www.ericdaugherty.com/dev/itunesexport/">http://www.ericdaugherty.com/dev/itunesexport/</a>

Please email me with new features or bug fixes (eric@ericdaugherty.com).
