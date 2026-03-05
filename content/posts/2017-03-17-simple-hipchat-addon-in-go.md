---
title: "Simple HipChat AddOn in Go"
date: 2017-03-17T00:12:00Z
url: /2017/03/simple-hipchat-addon-in-go.html
draft: false
---

We use HipChat at work to stay connected. It works well and has some fun plugins, including Karma. I'll bet a few of you can guess what happens when you create a karma system in a company full of smart technical folks.<br />
<br />
<b>THEY GAME THE SYSTEM.</b><br />
<br />
One of the more interesting hacks they discovered is to use the 'find and replace' functionality built into HipChat to secretly give (or more likely take) karma to/from another person. The proper usage of the Find/Replace functionality&nbsp;is something like:

```
> I can typo good.
> s/typo/type
```
The first line would be a typo that you made, and the second line allows you to 'fix' the typo. The key part here is that the second line modifies the first line and is not visible to any other users.<br />
<br />
Who could let this fun discovery go unused? Not our team! Our chats were quickly filled with Karma Ninjas giving and taking karma from behind a thin veil of secrecy.<br />
<br />
Luckily&nbsp;the <a href="https://bitbucket.org/atlassianlabs/ac-koa-hipchat-karma">Karma bot is open source</a>. So I forked the source, made a fix and submitted a pull request right?<br />
<br />
<b>WRONG</b>. Karma is written in JavaScript and writing JavaScript doesn't make me happy. So I decided to create a Karma Ninja bot instead to 'out' the folks attempting to be Karma Ninjas. Since I've been exploring Go on AWS Lambda recently, I figured this would be a great excuse to write more Go!<br />
<h3>
Starting Points</h3>
There are a few options out there already that really helped accelerate&nbsp;the effort.<br />
<br />
First, the <a href="https://github.com/eawsy">eawsy</a>&nbsp;folks created a great <a href="https://github.com/eawsy/aws-lambda-go-shim">shim</a> for Lambda that allows you to deploy Go easily and it runs FAST. Their solution is much faster from a cold start than the other NodeJS shims out there.<br />
<br />
Second, Nicola Paolucci has a great post on the Atlassian Blog about <a href="https://developer.atlassian.com/blog/2015/09/easy-hipchat-addons-in-golang/">building a HipChat addon in Go</a>.<br />
<br />
Finally, there is a <a href="https://github.com/davidrjonas/hipchat-addon">HipChat Addon</a> project by David Jonas on GitHub.<br />
<br />
The eawsy&nbsp;Lambda shim is being actively developed and the team was very responsive to a few of the issues/questions I had, including one that is <a href="https://github.com/golang/go/issues/19529">apparently a bug in Go 1.8</a>.<br />
<br />
The&nbsp;Atlassian blog post does a great job of walking through how to build an add-on. This was the template I ended up using for my addon. The only note I have here is that Nicola uses the roomId to store the authentication token, but that only works for single room installations. I used the OAuthId field instead which seems to work for both single room and global installations.<br />
<br />
David's project did not compile out of the box because of changes in the JWT Token upstream project. I thought about trying to fix is, but ultimately&nbsp;I wanted to understand how it all worked so I wrote mine without the template. I may go back and try to fix that project as an alternate implementation.<br />
<h3>
State</h3>
When I was envisioning building the plug-in, I assume I could build it statelessly. I assumed you could simply register a webhook with a regex and a callback URL that would return a message. But the webhook does not appear to let you return a message, you need to make a separate call into the HipChat API to post a message. Because of this, you need to maintain some state between calls.<br />
<br />
<i>EDIT: My first guess was correct, you can return a response to the webhook call and post a message. I ended up over-complicating it but the point was to learn more about AWS so it was still time well spent. Here is info on how to <a href="https://www.hipchat.com/docs/apiv2/webhooks">pass a response to the webhook</a>.</i><br />
<br />
I explored using both DynamoDB and S3 to maintain the needed state, which is really just an OAuth Token. They both worked fine but ultimately I chose to use S3 as it was the simpler and cheaper option for this use case.<br />
<br />
Amazon does publish an <a href="http://docs.aws.amazon.com/sdk-for-go/api">AWS SDK in Go</a> which made interacting with DynamoDB and S3 pretty easy. I do think the SDK is a bit 'low level' and could probably be made a lot easier to use with some convenience functions, but I'm just happy they support Go so I shouldn't complain.<br />
<br />
The eawsy team does the necessary work to make the Lambda&nbsp;environment available from Go, meaning that you can simply use the Go SDK without any explicit authentication credentials or setup. By default, you simply inherit the IAM Role of the Lambda function. In this case, I simply needed to add permission to access DynamoDB and Se.<br />
<h3>
Code</h3>
The code itself is pretty straightforward. Like most go projects, I'm always impressed with how much you can get done in just a few lines of code across a handful of files. I published the project on GitHub:&nbsp;<span style="color: #0000ee;"><a href="https://github.com/ericdaugherty/hipchat-karmacop">ericdaugherty/hipchat-karmacop</a></span>.<br />
<h3>
AWS</h3>
This code does require some AWS setup. You need to define a Lambda function and build and upload the project using the Makefile (see the README for instructions).<br />
<br />
You also need to setup an Amazon API Gateway entry to reference your AWS Lambda function. This will give you a public URL that your AddOn will reside at.<br />
<br />
An S3 bucket is required to store the OAuth token used to post responses back to the HipChat API.<br />
<br />
Finally, you need to add permission to read and write to S3 to the Lambda IAM Role configured for the Lambda Function.<br />
<h3>
That's It</h3>
<div>
This was a fun little project and shows a good use case for using Lambda to implement add-ons to cloud applications like HipChat.</div>

