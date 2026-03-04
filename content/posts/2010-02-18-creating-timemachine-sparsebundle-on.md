---
title: "Creating a TimeMachine SparseBundle on a NAS"
date: 2010-02-18T21:40:00Z
url: /2010/02/creating-timemachine-sparsebundle-on.html
draft: false
---

I use a ReadyNAS NV+ as my backup drive and bulk storage.&nbsp; Although the newer firmware directly supports TimeMachine, I've never been able to get that to work.&nbsp; (This probably has something to do with the fact that I was upgrading and downgrading my NV+ Firmware quite a bit to debug a separate issue).<br />
<br />
However, I did find a great tool to create SparseBundles that you can use on a NAS (or any external disk).<br />
<br />
<a href="http://code.google.com/p/backmyfruitup/">BackMyFruitUp</a>.&nbsp; First, it is a great name.&nbsp; Second,&nbsp; it is a simple and easy tool.&nbsp; The Tool I actually use is 'Create Volume Backup,' a subproject of BackMyFruitUp, which you can download from <a href="http://code.google.com/p/backmyfruitup/downloads/list">this page</a>.&nbsp; <br />
<br />
You hardly need instructions.&nbsp; Unzip it, run it, and type in the size you want for the sparsebundle.&nbsp; Then just copy it to your destination share and point Time Machine at it.&nbsp; Done.<br />
<br />
Of course, I wouldn't need it now if my Time Machine SparseBundle hadn't become corrupted.&nbsp; Luckily I didn't need it.&nbsp; I also perform a seperate rsync backup on occasion to insure I have a 'basic' backup of my user directory as well.
