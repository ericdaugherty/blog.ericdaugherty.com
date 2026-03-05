---
title: "Go Web Server using Lambda Function URLs"
date: 2022-05-21T18:45:00Z
url: /2022/05/go-web-server-using-lambda-function-urls.html
draft: false
---

It has been possible to use Lambda Functions to host Go (Golang) Web Servers for years. I wrote about a [project doing this back in 2016](https://blog.ericdaugherty.com/2016/03/lamda-go-and-gotsport-via-api-gateway.html). More recently, the [github.com/apex/gateway](http://github.com/apex/gateway) project provided a drop in replacement for net/http's ListenAndServe function that supported [AWS REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html), and later the [AWS HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html).

Amazon recently released the ability to access a [Lambda Function directly via URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html), without needing to configure the REST APIs or HTTP APIs. This remove an extra layer of configuration, complexity, and potentially cost, for deployments.

I created a fork of the [github.com/apex/gateway](http://github.com/apex/gateway) at [github.com/ericdaugherty/gateway](http://github.com/ericdaugherty/gateway) that supports this new approach. A trivial example of usage in the README is:

```go
package main

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
}
```

This is effective and addresses the issue, but can make local development a challenge. I often replace the main implementation above with:

```go
func main() {

	// check and see if we are running within AWS.
	aws := len(os.Getenv("AWS_REGION")) > 0

	http.HandleFunc("/", hello)

	// run using apex gateway on Lambda, or just plain net/http locally
	if aws {
		gateway.ListenAndServe(":8080", nil)
	} else {
		http.ListenAndServe(":8080", nil)
	}
}
```

This uses the net/http implementation of ListenAndServe locally during development, and the gateway library when deployed via Lambda. No configuration is needed, as the AWS_REGION environment variable is [automatically set by AWS when running as a Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html).

One limitation of the Lambda Function URLs is that you can only access the Lambda Function URL via the aws domain (ex: `https://<function id>.lambda-url.<aws region>.on.aws/`). One easy solution to this is to use [AWS CloudFront](https://aws.amazon.com/cloudfront/). For a simple use case, create a [SSL Certificate in AWS](https://aws.amazon.com/certificate-manager/) for your custom domain, and then create a CloudFront distribution, using the SSL Certificate and the AWS Function URL as the default origin. If you use this approach, you should also make sure to set the [HTTP Cache-Control Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) on your cache-able responses to improve performance and reduce your Lambda invocations.

You can use a more complicated CloudFront approach if your project uses a lot of static assets. The static assets can be deployed via S3 and the CloudFront distribution can pull from S3 or Lambda depending on the request path, but for smaller or low traffic deployment, everything can be served from the Lambda function.

From here you can build your application using any traditional tooling that is supported by the Go http/net library.
