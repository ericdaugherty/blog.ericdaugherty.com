---
title: "iTunes XML Parsing - .Net vs. Scala"
date: 2009-04-15T01:15:00.004Z
url: /2009/04/itunes-xml-parsing-net-vs-scala.html
draft: false
---
As part of my <a href="http://www.ericdaugherty.com/dev/itunesexport">iTunesExport</a> utility I wrote a (C#.Net) module to parse the iTunes XML file and provide two simple collections, Playlists and Tracks.  As part of my effort to learn Scala, I rewrote this module in Scala.  While the libraries don't provide the *exact*same interface and functinality, they are effectively the same.  The stats:

<a href="http://en.wikipedia.org/wiki/Source_lines_of_code">(Physical) Line of Code</a> count:

.Net: 459
Scala: 226

The Scala version accomplished the same functionality in 1/2 the lines of code.  While LOC count is a bit arbitrary, I think it is an important point.  The Scala code is much more concise, but maintains or even improves the readability (if you have a reasonable familiarity with Scala).  In this specific case Scala's handling of public properties provided a big reduction.  Ex:

Scala:
<pre>
val trackId: Double = ...
</pre>.Net:<pre>
private string id;

public string Id
{
 get{ return id; }
}
</pre>While it may seem that this provides much of the savings, the Scala version provides a much more verbose toString method, so some of the per-property savings is actually understated in this comparison.

While developing I did find myself consistently following the pattern:

- Identify logical functionality I wanted to extract into a helper method
- Writing code for helper method
- Realize it was just a single line and moving back inline
Simply put, I found the structure and features of the Scala language very well suited to write high level understandable code that performed the same functionality in fewer lines of code, compared to C# or Java.

Performance was something else.  As a functional language Scala is well suited to be a scalable language.  It also runs on the JVM, benefiting from a significant amount of work building a high performance virtual environment.  That said, this implemenation was purely single threaded.  The initial results were somewhat surprising:

Scala 4,800 ms
.Net 650 ms

That seemed like a pretty significant difference, so I took a deeper look.  The Scala library to load the XML file from disk took nearly 3 seconds!  This is a huge hit and accounts for much of the performance difference.  The remining functionality took ~1,800 ms, nearly 3x the entire .Net solution.  Where does the time go?

~3000 ms - reading the XML file from disk using Scala's XML library
~100 ms - parsing the main library attributes.
~1700 ms - parsing the tracks
~60 ms - parsing the playlists

Clearly loading the file and parsing the tracks are the biggest targets.  I'll leave loading the XML out of scope as it is a Scala library and focus on the tracks.  For each of entities (Library, Playlist, Track) I use a Trait that parses the plist XML into a Map and then assign the properties from the map.  For each track, parsing the XML into a Map took 1 ms or less, but assigning the variables from the map (and doing any type conversions) took up to 4 ms but more commonly took 1 ms or less. At the single ms level the simple act of measuring introduces a significant impact, so I'm not sure these numbers are meaningful.

With over 2600 tracks in the library, even spending 1 ms per track is forever (and indeed the average time per track without the measurement was closer to .65 ms).  The additional complexity introduced by my Scala approach caused a significantly slower execution time.  In the end, clean code is not necessarily fast code.

That said, this test does not really hit on the strength of Scala, which is scaling multi-threaded environments.  With less than 8 hours experience writing Scala, I'm sure my code is far from efficient.

*Update: I realized that the default behavior of the parsers is to validate the Schema.  I've disabled this behavior in the .Net version but not the Scala/Java version.  Much of the 3 seconds to 'load' the XML is really an external HTTP request and the validation.  However, using the Scala library I do not see an easy way to disable the Schema validation.*
