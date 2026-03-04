---
title: "Shared iTunes LIbrary"
date: 2007-05-26T03:32:00Z
url: /2007/05/shared-itunes-library.html
draft: false
---

I've finally found a way to setup iTunes to share write access to a single library.<br /><br />I maintain a single integrated iTunes library for my family.  However, everyone wants to maintain and edit their own playlists.  iTunes' built in sharing allows you to play from a single library, but does nothing to allow you to edit that single library remotely.<br /><br />I recently moved my entire library to my <a href="http://www.ericdaugherty.com/blog/2007/05/readynas-nv.html">NAS</a> and, inspired by a recent <a href="http://lifehacker.com/software/itunes/hack-attack-share-your-itunes-music-library-over-your-home-network-230605.php">lifehacker post</a>, I setup all the iTunes applications installed in my house to use the shared music and iTunes Library (.itl) share.<br /><br />My steps were pretty simple:<br /><br />1. Map network share on all computers to M:\<br />2. Move entire MP3 library to M:\Music<br />3. Copy iTunes files from My Music to M:\Music<br />4. Hold down the shift key while iTunes loads<br />5. Select the .itl file I copied to M:\Music<br />6. I had to go toe Edit/Preferences/Advanced and change the iTunes Music File Location from M:\Music\iTunes Music to just M:\Music.<br /><br />Now I can control my iTunes Library from any machine as a 'first class citizen'.  LifeHacker seems to be a pretty cool site that I guess I need to add to my RSS reader.
