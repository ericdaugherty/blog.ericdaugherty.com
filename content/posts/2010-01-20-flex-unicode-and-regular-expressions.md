---
title: "Flex, Unicode, and Regular Expressions (RegEx)"
date: 2010-01-20T19:06:00.006Z
url: /2010/01/flex-unicode-and-regular-expressions.html
draft: false
---
The internet really helps make the world smaller, and through my open source applications I've enjoyed interacting with a user base that includes many people from outside the United States.   <a href="http://www.ericdaugherty.com/dev/itunesexport/">iTunes Export</a> has seen adoption in many countries and has challenged me to continually think about internationalization (i18n) issues, from providing the application in multiple languages (English and French today) to handling character sets not traditionally seen in American music.  Which brings me to the current challenge.

The problem is that iTunes allows users to create playlist names with characters that are illegal in the file system.  This means that I cannot simply reuse the playlist names as the file names for the output playlist files without some processing.  My earlier versions attempted to simply replace common illegal characters (such as \, /, ', ", etc.) with an _ character.  However, this was rather haphazard, and required constant updates to the filter as I found new characters to filter out.  I decided to be reverse the process, so I wrote a regex that replaced all the characters that were not explicitly legal.  I started with \s\w which included alphanumeric characters and whitespace.  I added additional characters that were legal in most file systems  - . [ ] = $ &amp; {}.  My resulting regex was: /[^\s\w\-\.\[\]=$&amp;{}]/g.  This worked really well for my many of my United States users, but many users from other countries (and some from the US) found it too limiting.  Common characters such as é, à, è, ä, ö, ü, Ä, Ö,Ü, and ß were filtered out to an _ even though they were legal characters for file names.  So I went back and took another look at the regex.

(Note: \w matches alphanumeric characters but not accented characters like é.  However, this is not a bug but matches the <a href="http://www.ecma-international.org/cgi-bin/counters/unicounter.pl?name=Ecma-262&amp;deliver=http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf">ECMA 262 spec</a>)

To aid my efforts, I wrote a simple little utility to determine the Unicode character codes for certain strings, and then test out regex patterns.  Here is the utility:
<div id="regex-util">
Flash is required.  <a href="http://www.adobe.com/go/getflashplayer">Get it here!</a>
</div>
You can type in a string and it will convert it to the Unicode character codes.  It also converts it to the regex pattern representation (simply a \x instead of \u).  For example, the character é is \ue9 or \xe9.  If you enter that as the regex pattern, and then enter the string Tést, you will see the é is matched.

Based on what I've seen, I needed to include the many of the characters from the <a href="http://www.fileformat.info/info/unicode/block/latin_supplement/list.htm">Latin-1 Supplement Unicode block</a>.  Instead of including every character, I limited it to \uc0-\uff.  I think that should cover all the normal use cases.  The resulting regex patter in: /[^\s\w\-\.\[\]=$&amp;{}\xc0-\xff]/g.  This new regex will be included in the next release of iTunes Export (both Console and GUI).  The same regex works in Java, although you will need to escape the \ characters, or in Scala use """[^\s\w\-\.\[\]=$&amp;{}\xc0-\xff]""".

Give the above utility a try and feel free to suggest improvements.

For more information on Unicode and Regex: <a href="http://www.regular-expressions.info/unicode.html">http://www.regular-expressions.info/unicode.html</a>.

<script type="text/javascript">swfobject.embedSWF('http://www.ericdaugherty.com/apps/RegexConsole.swf', 'regex-util', '420', '250', '9.0.28', 'playerProductInstall.swf');</script>
