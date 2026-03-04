---
title: "Debugging Android Web Traffic"
date: 2012-02-21T21:34:00.001Z
url: /2012/02/debugging-android-web-traffic.html
draft: false
---

Normally, I would use a packet sniffer, such as <a href="http://www.wireshark.org/">WireShark</a>&nbsp;(OS X and Windows) to look at the network traffic and debug the application.<br />
<br />
However, for Android development I do my primary development on a physical Android device. &nbsp;It is faster, and provides a more realistic experience during development and debugging. &nbsp;However, since the network traffic is no longer going through my computer, WireShark doesn't help.<br />
<br />
To solve this, I use another program called <a href="http://www.charlesproxy.com/">Charles</a>. &nbsp;Charles is a 'Web Debugging Proxy Application'. &nbsp;In short, it is a tool similar to WireShark, that allows you to easily debug network traffic. &nbsp;Charles is a bit 'higher level' than WireShark, and provides a simpler view of the web requests to developers.<br />
<br />
It also has a great feature, called Reverse Proxy. &nbsp;This allows you to setup your local computer as a proxy for web traffic. &nbsp;You can set it up as follows:<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirCr0IG5D05r8PIYYh_OhTDKi5MpoTmS9VIjudkYg8ujKkcapMhwp0Bsnsw_hVi9orfUihM8xXMED4grOLC-3RnchN8TlJfJLBJOe7-FgnPiAe-Q0PY-6WquiGL6dwl9vWzEk27OZi0tA/s1600/Screen+Shot+2012-02-21+at+2.26.28+PM.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="245" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirCr0IG5D05r8PIYYh_OhTDKi5MpoTmS9VIjudkYg8ujKkcapMhwp0Bsnsw_hVi9orfUihM8xXMED4grOLC-3RnchN8TlJfJLBJOe7-FgnPiAe-Q0PY-6WquiGL6dwl9vWzEk27OZi0tA/s320/Screen+Shot+2012-02-21+at+2.26.28+PM.png" width="320" /></a></div>
<br />
If your normal Web Service host was targetwebserver.com:80, you would set it up like the image above. &nbsp;You can then change your mobile application configuration to point at the IP address of your computer, using port 64829 (or whatever you set it to).<br />
<br />
Note: Make sure your mobile devices is on the same WiFi network as your computer!<br />
<br />
Now, all traffic will be routed through your local machine, and Charles will capture all the traffic, allowing you to debug your network communications.<br />
<br />
Charles also supports HTTPS proxies, so you can use it even if the web services are over HTTPS (as they probably should be).<br />
<br />
Of course, this also works fine for iOS, although I find myself using the simulator more in iOS, which allows WireShark or normal Charles to work fine.<br />
<br />
Charles is commercial software, but I've found it to be worth the price. &nbsp;I believe you could probably setup a reverse proxy on your computer using many different approaches (you could always run your own Apache), which would enable you to use the free WireShark application as well.<br />
<br />
Does anyone have other approaches?<br />
<br />
UPDATE:<br />
And an&nbsp;intrepid&nbsp;reader&nbsp;(<a href="http://twitter.com/tehnoir">tehnoir</a>)&nbsp;points out that&nbsp;you can also just use Charles as a 'normal' Proxy server, and then configure your device to use your computer as a proxy server, which will then proxy all traffic through. &nbsp;This allows you to sniff traffic without changing anything in your application (great for testing).<br />
<br />
It would seem that simple Port Forwarding (another Charles feature) may also work as well.
