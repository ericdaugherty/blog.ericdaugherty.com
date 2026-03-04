---
title: "Be Careful with Dates"
date: 2012-05-22T23:06:00Z
url: /2012/05/be-careful-with-dates.html
draft: false
---

The year 2000 came and went, and the world went on. &nbsp;There were no horrific date rollover bugs, despite all the press. &nbsp;However, that doesn't mean that date rollover issues do not exist.<br />
<br />
I just debugged a date rollover issue. &nbsp;It manifested as follows:<br />
<br />
Our application worked fine in our local environment (of course), but when we deployed to a customer's server, the cookies didn't work. &nbsp;We took a look at the HTTP Headers using Chrome, and everything seemed fine. &nbsp;But still they didn't work.<br />
<br />
However, when I took a close look at the headers in our test environment and the server environment, the issue jumped right out at me.<br />
<br />
Here was the header from our local environment:<br />
<br />
Set-Cookie:prop1=value1;Path=/ourapp;Expires=Mon, 10-Jun-2080 00:13:42 GMT<br />
<br />
And on the customer's server:<br />
<br />
et-Cookie:prop1=value1;&nbsp;Expires=Sun, 09-Jun-80 23:59:24 GMT; Path=/ourapp<br />
<br />
Do you see it? &nbsp;It is rather obvious.<br />
<br />
It is a date roll-over issue.<br />
<br />
The problem was caused when we set the cookie expiration date to Integer.MAX_VALUE. &nbsp;This resulted in a date some time in 2080. &nbsp;In our local environment, Jetty handles this properly and uses a long date format for the year.<br />
<br />
However, the production server uses IBM WebSphere, and it takes a short cut. &nbsp;It simply renders 2080 as 80.<br />
<br />
So the browser sees the date and discards it as expired. &nbsp;Apparently it doesn't use the 'context clue' of Sun to determine which century the date is in...<br />
<br />
By setting a realistic&nbsp;expiration&nbsp;date for the cookie, it works just fine.<br />
<br />
We were distracted for a bit by IBM WebSphere adding: Cache-Control:no-cache="set-cookie, set-cookie2" &nbsp;However in the end that seems to be unrelated.<br />
<br />
Hope this can help someone else.
