---
title: "GoLang Alexa SDK"
date: 2017-03-04T03:28:00.001Z
url: /2017/03/golang-alexa-sdk.html
draft: false
---

I continue to be interested in Alexa, Amazon AWS Lambda, and Go (golang), and I've found a new way to deploy Alexa apps in Go on Lambda.<br />
<br />
While Go is still not an officially supported language on Amazon Lambda, there are several ways to make it work:<br />
<br />
<ul>
<li><a href="https://github.com/jasonmoo/lambda_proc">Lambda_proc</a>&nbsp;- Node.js wrapper for your go binary</li>
<li><a href="https://github.com/gopherjs/gopherjs">GopherJS</a> - Cross-Compile your Go code to NodeJS</li>
<li><a href="https://github.com/eawsy/aws-lambda-go-shim">eawsy Lamba Go Shim</a> - Python shim for your go binary</li>
</ul>
<div>
In my previous project where I built a <a href="http://blog.ericdaugherty.com/2016/03/lamda-go-and-gotsport-via-api-gateway.html">screen scraper in Go and deployed it to Lambda</a>, I utilized Lambda_proc. &nbsp;This does work pretty well an is a solid solution.</div>
<div>
<br /></div>
<div>
I found GopherJS to be an interesting project, but a pretty indirect way to get Go onto Lambda. &nbsp;Lambda can run Go Linux binaries, so converting your Go to JavaScript seems like the wrong approach.</div>
<div>
<br /></div>
<div>
The eawsy team released their new tool earlier this year and it seems to be the cleanest approach. &nbsp;The overhead between the Python shim and your Go code is clean and fast. &nbsp;They utilize a Docker container to build the necessary bridges from Python to Go, resulting in very fast execution. &nbsp;You can write log messages to the Lambda console using log.Printf. And it is FAST. The HelloWorld skill runs in sub-millisecond times!</div>
<div>
<br /></div>
<div>
To build Alexa skills in Go on Lambda, we still need an SDK. &nbsp;Amazon publishes SDKs for <a href="https://github.com/amzn/alexa-skills-kit-java">Java</a>&nbsp;and <a href="https://github.com/amzn/alexa-skills-kit-js">JavaScript</a>&nbsp;but not for Go. &nbsp;So I ported the Java SDK into Go as <a href="https://github.com/ericdaugherty/alexa-skills-kit-golang">ericdaugherty/alexa-skills-kit-golang</a>&nbsp; While this does not (yet) have the full depth of the Amazon SDK, it does enable you to build simple Alexa skills using Go and deploy them on Lambda.</div>
<div>
<br /></div>
<div>
Take a look at the&nbsp;<a href="https://github.com/ericdaugherty/alexa-skills-kit-golang">alexa-skills-kit-golang</a>&nbsp;project for usage and samples, and give the&nbsp;<a href="https://github.com/eawsy/aws-lambda-go-shim">eawsy Lamba Go Shim</a>&nbsp;a try for your next Go project on Amazon AWS Lambda.</div>
<div>
<br /></div>
<div>
&nbsp;- Updated 3/4/2017 - updated run time based on newer stable eawsy shim speeds.</div>

