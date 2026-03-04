---
title: "Go Web Server using Lambda Function URLs"
date: 2022-05-21T18:45:00Z
url: /2022/05/go-web-server-using-lambda-function-urls.html
draft: false
---

<p>It has been possible to use Lambda Functions to host Go (Golang) Web Servers for years. I wrote about a <a href="https://blog.ericdaugherty.com/2016/03/lamda-go-and-gotsport-via-api-gateway.html">project doing this back in 2016</a>. More recently, the <a href="http://github.com/apex/gateway">github.com/apex/gateway</a> project provided a drop in replacement for net/http's ListenAndServe function that supported <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html">AWS REST APIs</a>, and later the <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html">AWS HTTP APIs</a>.</p><p>Amazon recently released the ability to access a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html">Lambda Function directly via URL</a>, without needing to configure the REST APIs or HTTP APIs. This remove an extra layer of configuration, complexity, and potentially cost, for deployments.&nbsp;</p><p>I created a fork of the <a href="http://github.com/apex/gateway">github.com/apex/gateway</a> at <a href="http://github.com/ericdaugherty/gateway">github.com/ericdaugherty/gateway</a> that supports this new approach. A trivial example of usage in the README is:</p>
<pre class="brush: text">package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/ericdaugherty/gateway"
)

func main() {
	http.HandleFunc("/", hello)
	log.Fatal(gateway.ListenAndServe(":3000", nil))
}

func hello(w http.ResponseWriter, r *http.Request) {
	// example retrieving values from the api gateway proxy request context.
	requestContext, ok := gateway.RequestContext(r.Context())
	if !ok || requestContext.Authorizer["sub"] == nil {
		fmt.Fprint(w, "Hello World from Go")
		return
	}

	userID := requestContext.Authorizer["sub"].(string)
	fmt.Fprintf(w, "Hello %s from Go", userID)
}</pre>
<p>This is effective and addresses the issue, but can make local development a challenge. I often replace the main implementation above with:</p><pre class="brush: text">func main() {

	// check and see if we are running within AWS.
	aws := len(os.Getenv("AWS_REGION")) &gt; 0&nbsp;</pre><pre class="brush: text"><span>&nbsp;&nbsp; &nbsp;</span><span>&nbsp;&nbsp; &nbsp;</span>http.HandleFunc("/", hello)

	// run using apex gateway on Lambda, or just plain net/http locally
	if aws {
		gateway.ListenAndServe(":8080", nil)
	} else {
		http.ListenAndServe(":8080", nil)
	}
}</pre>
<p>This uses the net/http implementation of ListenAndServe locally during development, and the gateway library when deployed via Lambda. No configuration is needed, as the AWS_REGION environment variable is <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html">automatically set by AWS when running as a Lambda Function</a>.</p><p>One limitation of the Lambda Function URLs is that you can only access the Lambda Function URL via the aws domain (ex: https://&lt;function id&gt;.lambda-url.&lt;aws region&gt;.on.aws/). One easy solution to this is to use <a href="https://aws.amazon.com/cloudfront/">AWS CloudFront</a>. For a simple use case, create a <a href="https://aws.amazon.com/certificate-manager/">SSL Certificate in AWS</a> for your custom domain, and then create a CloudFront distribution, using the SSL Certificate and the AWS Function URL as the default origin. If you use this approach, you should also make sure to set the <a href="https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwi74Zu5nfH3AhXWkmoFHZedCwgQFnoECAwQAQ&amp;url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FCache-Control&amp;usg=AOvVaw3ANm8tFKBCzSoAMoKZ7xZS">HTTP Cache-Control Header</a> on your cache-able responses to improve performance and reduce your Lambda invocations.&nbsp;</p><p>You can use a more complicated CloudFront approach if your project uses a lot of static assets. The static assets can be deployed via S3 and the CloudFront distribution can pull from S3 or Lambda depending on the request path, but for smaller or low traffic deployment, everything can be served from the Lambda function.<br /></p><p>From here you can build your application using any traditional tooling that is supported by the Go http/net library.<br /></p><p><br /></p>

