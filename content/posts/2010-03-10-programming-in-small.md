---
title: "Programming in the Small"
date: 2010-03-10T15:39:00Z
url: /2010/03/programming-in-small.html
draft: false
---

I believe that successful application development today is about 'tweaks and sub-features', not major functionality.&nbsp; But my thought process for this post was kicked off by an interesting post by Mike Taylor: '<a href="http://reprog.wordpress.com/2010/03/03/whatever-happened-to-programming/">Whatever happened to programming?</a>' Mike laments the evolution of programming.&nbsp; He is nostalgic for the day when writing a program was about creating something from scratch, instead of assembling the various pieces.<br />
<br />
I think his assessment of the transition is fairly accurate.&nbsp; The number of frameworks and libraries in projects today far exceeds the number used in projects 5, 10, or 20 years ago.&nbsp; This is especially true in the Java world, where build tools like Maven gained traction because they handled the dependency management.&nbsp; And now, a non-trivial Java project can easily incorporate 100 or more jar files, while a trivial 'boiler plate' web application can easily have 20 jars.<br />
<br />
In many ways this is frustrating.&nbsp; It has also given rise to what I call the cut and paste programmer.&nbsp; You can actually achieve reasonably impressive results simply by searching for the right libraries, and them assembling them together but cutting and pasting example code found via Google.<br />
<br />
From a business perspective, these are all good things.&nbsp; The level of skill required to produce results is lower, and the speed of development has greatly increased.&nbsp; We are standing on a very tall foundation.<br />
<br />
This also means that the major functionality of many applications is provided mostly by libraries and frameworks.&nbsp; The heavy lifting parts are not really heavy anymore.&nbsp; I think <a href="http://www.codinghorror.com/">Jeff Atwood</a> hits this nail on the head when he stated on a <a href="http://blog.stackoverflow.com/category/podcasts/">Stack Overflow podcast</a> episode that the major features of Stack Overflow themselves are fairly trivial.&nbsp; The real value is that it is a collection of many small features and tweaks that make the overall system successful (I can't find the reference, so I apologize if I paraphrased incorrectly).&nbsp; I think this point is right on.&nbsp; Most major 'features' are trivial to implement today using the rich set of libraries that exist.&nbsp; Building a website that has questions an answers like stack overflow is trivial.&nbsp; Making it successful is hard.&nbsp; And the difference is all in the fine print.<br />
<br />
Jeff discussed at some length the time they spent with the syntax parser (markdown) and instructions on the 'ask a question' page.&nbsp; Small changes to how the information is displayed and highlighted are much more important then the major feature of saving the question to a database and displaying it.<br />
<br />
Successful applications today are about the user experience.&nbsp; There are very few applications that are truly innovative themselves and could not be replicated by gluing together a set of frameworks.<br />
<br />
Real innovation today is in the small.&nbsp; This is also why I believe that the rise of <a href="http://blog.ericdaugherty.com/2010/02/why-ipad-will-succeed-and-rise-of.html">Appliance Computing </a>is here, and that <a href="http://blog.ericdaugherty.com/2010/02/does-write-once-run-anwhere-work.html">Write Once Run Anywhere languages are inferior to native client applications</a>.&nbsp; It is the difference between a iPhone web application and a native app.&nbsp; They both have the same features, but the experience can be very different.&nbsp; In the end, the real value is the small efficiencies in the application, not the large features.&nbsp;
