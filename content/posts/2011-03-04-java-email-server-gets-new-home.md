---
title: "Java Email Server Gets a New Home"
date: 2011-03-04T03:09:00.001Z
url: /2011/03/java-email-server-gets-new-home.html
draft: false
---
Nearly 10 years ago I created a fork of the <a href="http://crsemail.sourceforge.net/">CSRMail</a> project, with the permission and encouragement of Calvin Smith, the project's founder. &nbsp;The new fork was called Java Email Server.

Java Email Server (JES) started as a 'scratch the itch' project. &nbsp;I wanted to run an email server on my home Windows computer to host a few different email domains. &nbsp;I found the available options overly confusing or expensive, so I developed a solution to meet my needs.

The initial goal of JES was to solve my problem, and that problem was: "I want an easy to setup email server to host a few small domains". &nbsp;Over time, I have worked with the community to add features and fix (many) bugs, while working to keep JES a simple and easy to use solution.

JES has also been an interesting learning experience as a developer. &nbsp;It is a project I've worked on for 10 years now, a period that has seen my experience and capabilities change significantly. &nbsp;The code base is often a useful exercise in humility. &nbsp;I appreciate all the contributions the community has made over the years, not only to JES, but to my skills as a developer.

The JES community has contributed other projects, including a <a href="http://jesplug-in.sourceforge.net/">JES Plugin for Eclipse</a>. &nbsp;JES has found a home in production systems, and as a tool for many development teams,&nbsp;assisting&nbsp;the testing process of systems that interact with email servers. &nbsp;With 50,000 downloads of the binary versions of the 1.x branch over the years, JES has reached a lot of users.

JES even spawned my first commercial software offering, <a href="http://www.goldeninnovations.com/simplemailprocessor/">Simple Mail Processor</a>. &nbsp;It provides an API to process incoming SMTP messages, useful in systems that need to act&nbsp;programmatically&nbsp;on incoming email.

Over the years, many&nbsp;contributors&nbsp;have come and gone. &nbsp;But for the past few years, one developer has picked up the ball and really run with it. Andreas Kyrmegalos developed the 2.0 branch of JES, bringing it into the modern era with the addition of many much-needed features (like SSL)!

I have decided to hand over control of the JES project to&nbsp;Andreas. &nbsp;I'm confident he will do a great job, as he has been doing for the last few years. &nbsp;And more importantly, with me out of the way, he will be able to bring releases, features, and bug fixes out much more quickly. &nbsp;The project will remain hosted at SourceForge, but the <a href="http://javaemailserver.sourceforge.net/">main HTML</a> page will also be hosted at SourceForge instead of on my site.

My site will continue to host the original 1.x branch releases and documentation, but all current (2.x and beyond) releases,&nbsp;documentation, and discussion will take place on the <a href="https://sourceforge.net/projects/javaemailserver/">SourceForge project page</a>.

I wish Andreas and the JES community the best and hope that the project continues to thrive.

I'm still happy to help any JES 1.x users with issues or critical bug fixes, but the 1.x branch is firmly in&nbsp;maintenance&nbsp;mode and no new development will be&nbsp;occurring&nbsp;on it. &nbsp;Since JES 2.0 now&nbsp;requires&nbsp;JDK 1.5, the 1.x branch also continues to serve as the JES solution for older JDKs.
