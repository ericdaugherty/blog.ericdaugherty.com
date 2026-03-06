---
title: "iTunes Export 2.1.1 Released"
date: 2009-12-07T19:52:00Z
url: /2009/12/itunes-export-211-released.html
draft: false
---
With over 4,500 downloads of the GUI version, and 1,700 downloads of the console version, the 2.0 release of iTunes Export appears to be a success.  Thank you to all who have helped out.

This release provides a few bug fixes and incremental improvements based on the feedback received so far.  Thank you to everyone who has helped out, and please reach out if you have issues or suggestions.

This release as a few fixes for both versions, including:
- iTunes uses different values for 'Type' based on the user's language.  Changed logic to match file extension instead of value of 'Type' for MP3 file matching.
- Updated processing of Playlist Name.  All characters are replaced with an underscore (_) except A-Z,a-z,0-9,.[]{}-$=.  This should resolve any issues with playlists containing illegal characters.  This may result in some characters in non-western character sets to be replaced with _.  GUI and Console versions now contain the exact same logic.
And a few changes to the GUI version:

- Resolved issue with File Separator replacement (/ \) on Windows.
- Fixed issue where scroll bars would appear with long Music Path.
- Fixed Show Songs feature to update the song list when a different playlist is selected.
- Implemented basic 'type to find' logic for Playlist list.  Only matches first character, and you must select an item before the search works.
The new version can be downloaded from the project homepage: <a href="http://www.ericdaugherty.com/dev/itunesexport/">http://www.ericdaugherty.com/dev/itunesexport/</a>

If you find any issues or have questions please email me (eric@ericdaugherty.com). Please include which application and version (GUI or Console, 2.1.1 etc.) of iTunes Export and the operating system you are using.
