---
title: "Lamda, Go, and GotSport via API Gateway"
date: 2016-03-12T00:10:00Z
url: /2016/03/lamda-go-and-gotsport-via-api-gateway.html
draft: false
---

While I've been primarily living in the mobile world recently, I've been intrigued by a the developments in a few other areas of technology.<br />
<br />
<a href="https://golang.org/">Go</a>, or golang, has been increasingly becoming my preferred language for side projects. &nbsp;I really like the concise nature of the language, the ability to deploy on multiple platforms, and the short tool chain. &nbsp;It 'just works', and is fun to program in.<br />
<br />
AWS continues to add interesting services and features. &nbsp;I recently&nbsp;<a href="http://blog.ericdaugherty.com/2015/08/site-migration.html">moved my website from GoDaddy to host on S3</a>. &nbsp;This really started my thinking about living in a 'serverless world'. &nbsp;While practically speaking hosting on S3 isn't really all that different than virtual hosting at GoDaddy, it is really just scratching the surface. &nbsp;You can now build pretty interesting applications without running a server (virtual or otherwise).<br />
<br />
<!--more--> 
I begin to think about how you could build a full application using the AWS stack without an EC2 instance. &nbsp;Of course, a ton of thought has already been put into this. &nbsp;The <a href="https://github.com/serverless/serverless-starter">Serverless</a> tool allows you to easily configure Amazon to use the API Gateway with Lambda to deploy functional APIs. &nbsp;There is also a website dedicated to <a href="https://serverlesscode.com/">living serverless</a>.<br />
<br />
I've also been working on a few Amazon Alexa applications for the Echo, which also uses Lambda as the preferred deployment program.<br />
<br />
So I thought it was time to build something that actually works.<br />
<br />
My son plays soccer and the Colorado Soccer Association uses the event.gotsport.com website to post schedules and results. &nbsp;So I built a screen scraper in Go to parse his schedule into JSON so I could use it in my Amazon Alexa application. &nbsp;(The scraper is here:&nbsp;<a href="https://github.com/ericdaugherty/gotsport-scraper">https://github.com/ericdaugherty/gotsport-scraper</a>) &nbsp;But I hard-coded the resulting JSON into that application.<br />
<br />
I figured I could build a general API that could be used by anyone to convert the schedules into JSON. &nbsp;And I could easily deploy it on Lambda.<br />
<br />
In order to get Go running on Lambda, you need to 'work around' the fact that it isn't officially supported. &nbsp;The lambda_proc library (<a href="https://github.com/jasonmoo/lambda_proc">https://github.com/jasonmoo/lambda_proc</a>) does just that. &nbsp;It uses a node.js wrapper that invokes your Go application within the Lambda runtime. &nbsp;The repository has a good example that should you how to write and deploy a go app on Lambda.<br />
<br />
From there, I just needed a simple Go app to take the input JSON, run the gotsport-scraper I wrote, and return the resulting JSON.<br />
<br />
The final step was exposing the Lambda function as an HTTP API. &nbsp;This is where the API Gateway comes in. &nbsp;It allows you to specify an endpoint and method to trigger the Lambda function. &nbsp;The basics are pretty straightforward. &nbsp;You define a resource (/gotsport) and a method (GET), and map it to your Lambda function. &nbsp;However, the tricky part is the mapping of the HTTP Request to the Lambda function, and the result of the Lambda function to the HTTP Response.<br />
<br />
Here is the full lifecycle:<br />
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5MpIMtsnyRL0arVtmU-2Cow1tvWBSqn_dg4zbEoCH7tsjluewJWYuv3ifAHOz7IsBbrCoO_UwiqWs63pFCVrwoefYt2WaFZ-valBdUy9PA107kvu8LiydlSSFJjQKl-mXrayqRflTdOc/s1600/Screen+Shot+2016-03-11+at+4.15.37+PM.png" imageanchor="1"><img border="0" height="219" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5MpIMtsnyRL0arVtmU-2Cow1tvWBSqn_dg4zbEoCH7tsjluewJWYuv3ifAHOz7IsBbrCoO_UwiqWs63pFCVrwoefYt2WaFZ-valBdUy9PA107kvu8LiydlSSFJjQKl-mXrayqRflTdOc/s640/Screen+Shot+2016-03-11+at+4.15.37+PM.png" width="640" /></a><br />
<br />
<br />
I decided to use Query String parameters to pass data to the function, so you could just cut/paste from the URL you wanted converted. &nbsp;You can define the query strings in the Method Request section, but this just seems to allow you to use them when testing and isn't required. &nbsp;I did have to map the query parameters into the Lambda, so I created an application/json mapping (since the Lambda function consumes JSON). &nbsp;The mapping function is:

```
{
    "eventId" : "$input.params('EventID')",
    "groupId" : "$input.params('GroupID')",
    "gender"  : "$input.params('Gender')",
    "age"     : "$input.params('Age')"
}
```
This maps the Query String Parameters using their names (again, as used on gotsport.com so you can cut and paste) into JSON values that match those used by me gotsport-scraper tool. &nbsp;This is then passed to the Lambda function.<br />
<br />
The Lambda function runs, fetching the requested URL, scraping it, and returning a JSON value. &nbsp;However, the lambda_proc function returns both an error value and a data value containing the results of the Lambda function. &nbsp;I wanted to map the output to just contain the JSON representing the schedule. &nbsp;So in the Integration Response step in the lifecycle, I used the application/json mapping function:

```
#set($inputRoot = $input.path('$'))
$input.json('$.data')
```
This just extracts the data element from the JSON returned from the Lambda function and passes it back as the HTTP Response Body.<br />
<br />
The proper approach in the Integration Response step is to use a RegEx to determine if an error occurred or not, and return the proper HTTP response code and appropriate body. &nbsp;For now I'm assuming a 200 response with valid data.<br />
<br />
That's it! &nbsp;I now have an HTML-&gt;JSON screen scraper for the GotSport website deployed as an API.<br />
<br />
Want to see how this all works. &nbsp;Here are the resources:<br />
<br />
<ul>
<li><a href="https://github.com/jasonmoo/lambda_proc">lambda_proc</a> - Run GoLang apps on Lambda</li>
<li><a href="https://github.com/ericdaugherty/gotsport-scraper">gotsport-scraper</a> - Screen Scrape the event.gotsport.com site</li>
<li><a href="https://github.com/ericdaugherty/gotsport-lambda">gotsport-lambda</a> - Lamba function to execute gotsport-scraper</li>
<li><a href="http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html">Amazon API Gateway</a> - General API Gateway documentation</li>
<li><a href="http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html">Amazon API Gateway Mapping</a> - Documentation about writing mapping files.</li>
</ul>
<div>
Want to test it out? &nbsp;Grab a specific schedule from the <a href="http://events.gotsport.com/events/Default.aspx?EventID=46461">CSA Youth Advanced League 2016</a> site. &nbsp;Then cut/paste the query string parameters onto my API URL:&nbsp;https://j4p9lh1dlb.execute-api.us-east-1.amazonaws.com/prod/gotsport &nbsp;For example, the U-11 Boys Super League would be:&nbsp;<a href="https://j4p9lh1dlb.execute-api.us-east-1.amazonaws.com/prod/gotsport?EventID=46461&amp;GroupID=511424&amp;Gender=Boys&amp;Age=11">https://j4p9lh1dlb.execute-api.us-east-1.amazonaws.com/prod/gotsport?EventID=46461&amp;GroupID=511424&amp;Gender=Boys&amp;Age=11</a></div>
<div>
<br /></div>
<div>
<br /></div>
<div>
<br /></div>

