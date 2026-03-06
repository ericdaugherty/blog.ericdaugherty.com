---
title: "OpenID Intro"
date: 2007-03-29T02:33:00Z
url: /2007/03/openid-intro.html
draft: false
---
OpenID is quickly becoming 'the next big thing', and so I had to take a closer look.

The goal of OpenID is to provide an open framework to allow end users to control their own authentication process, and use it anywhere.  This is similar to what Microsoft's Passport, or the Liberty Alliance tried to do.  These systems both failed because no one really wanted to trust their information to a single (or group of) controlling entities.

The difference with OpenID is that you can use ANY OpenID server to manage your authentication.  A simple example.  Many sites offer OpenID credentials.  You sign up there and get a URL that is YOU.  Let's say http://example.com/eric.daugherty.  Then when you log in to Digg.com, you specify http://example.com/eric.daugherty as your login.  Digg.com will then redirect you to example.com to authenticate.  Once you do, you are returned to Digg.com and are logged in.

This is pretty interesting, but I think one of the advanced features are much more interesting.  If you own your own URL (say, <a href="http://www.ericdaugherty.com/">http://www.ericdaugherty.com</a>), you can use that as your login.  All you have to do is edit the HTML page to specify what OpenID server and login to use.  So, I could edit <a href="http://www.ericdaugherty.com/">http://www.ericdaugherty.com</a> to login using http://example.com/eric.daugherty.  This allows me to maintain a single identity over time but use different OpenID servers as I see fit.

One major component is that you can't trust that just because someone has an OpenID that authenticates, that you really know anything.  It seems like it would be very easy to setup an 'open relay' server that would authenticate any URL.  So if you want to collect a 'known good' email address during registration for a website, you still have to manage that yourself.  You can't really trust any data from the OpenID server that you can't verify yourself.

It will be interesting to see how this develops, and I'm going to try to find some more time to play with it and see how hard it is to implement an OpenID server.
