---
title: "iTunes XML Parsing - .Net vs. Scala - UPDATE"
date: 2009-04-23T03:25:00.003Z
url: /2009/04/itunes-xml-parsing-net-vs-scala-update.html
draft: false
---
In an <a href="http://www.ericdaugherty.com/blog/2009/04/itunes-xml-parsing-net-vs-scala.html">earlier post</a> I compared a .Net and Scala implementation of an iTunes Music Library XML parser.  The Scala version took a long time to 'load the XML file from disk'.  Since then I realized that the default behavior of the parsers is to validate the Schema.  I had disabled this behavior in the .Net version but not the Scala/Java version. Much of the 3 seconds to 'load' the XML is really an external HTTP request to download the xsd file and perform the validation. However, using the Scala library I do not see an easy way to disable the Schema validation (Under the covers the Scala library is delegating to existing Java APIs).

