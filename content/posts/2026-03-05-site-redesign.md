+++
date = '2026-03-05T03:13:01Z'
draft = false
title = 'Site Redesign and Migration'
+++

My old site design was getting a bit old and it was time for a cleanup. Now that AI is all the rage I used Claude Code to come up with a new site design and applied it.

This is really 2 different sites... [www.ericdaugherty.com](https://www.ericdaugherty.com) and [blog.ericdaugherty.com](https://blog.ericdaugherty.com). www was hosted via GitHub Pages while blog was hosted using Google's [Blogger](https://blogger.com). I felt it was time to move to a simpler static blog setup, so I migrated that to Hugo, also hosted by GitHub Pages.

For the www site, I just had to have Claude Code come up with a new design based on my very rough descriptions, and then I iterated on it with Claude until it looked acceptable.

For the blog site, I needed to create a new repository, initialize a Hugo site, import all the blog posts, import the styling from the www site, and then throw them all together and fix any and all of the issues. When I say 'I needed', I mean 'I prompted Claude to...'. 

While this is hardly custom software development, my experience with the migration makes me more convinced that I will be using AI as my interface to all things technical. While it wasn't perfect, especially with tweaking the visual layout, I accomplished the entire process in a few hours of prompting while multi-tasking.

I realized the old site was still using FeedBurner, which has long been abandoned (although still functional), so the Subscribe link now points directly to the index.xml (Hugo's RSS Feed) as does the Meta header. The old FeedBurner link has been updated to point to that as well.

Let me know if you see any issues. I cleaned up some content and fixed some long-broken images but mostly it is just a fresh coat of paint and a new home.