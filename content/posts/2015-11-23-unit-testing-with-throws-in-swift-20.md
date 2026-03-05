---
title: "Unit Testing with throws in Swift 2.0"
date: 2015-11-23T00:26:00.001Z
url: /2015/11/unit-testing-with-throws-in-swift-20.html
draft: false
---

I've been working very slowly on a Swift version of Playlist Export, and today I finally got around to updating the project to Swift 2.0. &nbsp;Luckily I wrote test cases for much of the logic to manage the export process, so I had some level of confidence that I would know if I broke anything.<br />
<br />
However, after I got the project to compile, only one of the test cases ran. &nbsp;No errors or other indication why all the other cases were ignored.<br />
<br />
I did finally figure out that if you your test case has a throws clause, it will be IGNORED.<br />
<br />
So:

```swift
testPlaylistNameExtension() throws {
    ...
}
```
<div class="p1">
<span class="s1"><br /></span></div>
<div class="p1">
<span class="s1">will silently be ignored, which for a test case is a pretty bad scenario. &nbsp;But if you handle the error in the function and change it to:</span></div>

```swift
testPlaylistNameExtension() {
    ...
}
```
<div class="p1">
<span class="s1"><br /></span></div>
<div class="p1">
then everything is just fine. &nbsp;So if you have test in Swift 2.0 that are ignored or not executed, check to see if you have a throws in the function declaration.</div>
<div class="p1">
<br /></div>
<div class="p1">
<br /></div>

