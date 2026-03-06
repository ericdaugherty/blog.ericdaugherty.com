---
title: "Package Delivery Detector"
date: 2019-02-08T16:37:00Z
url: /2019/02/package-delivery-detector.html
draft: false
---
The following is an outline of how and why I built a tool to detect when packages are delivered to my front porch. If you have enough of the right infrastructure in place, this will serve as a guide to get it setup yourself. All the source code is available, so if your setup is different, you can take and modify what I've done to work for you.

This solution is built using Go, AWS, Google Vision, and Docker.

<h3>
Motivation</h3>
In November I attended Amazon's AWS re:Invent conference to catch up on the current state of the cloud. I came away from the conference inspired to leverage an area that I didn't have a ton of experience, Machine Learning. I attended several SageMaker sessions and came up with a project idea:

A tool that would use Machine Learning to detect when a new package was delivered to my home.

I already had a lot of key infrastructure in place, including a Ubiquity UniFi camera that was pointed at my front porch. I also had a Synology Diskstation with Docker that I used to run both my UniFi controller and UniFi NVR.

This project took a long time. I kicked off work in early December and I just recently got to the point where I'm happy with the results.

<h3>
Image Capture</h3>
The key to this project is to build a Machine Learning model that can determine if there is a package at my front door. To build this model, I needed a lot of input data, so I started with a small app that would take a snapshot from my camera every few minutes and save it.

Luckily, UniFi cameras make it easy to grab a JPEG of the current frame. This is what my front door looks like right now:

<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMv5UKVeEA3oLTMLwjDTG_W69LFVDhc3TfxSnZmo5hifQnLS7ftq9XbBI9Qw-509_u6HzzlScth-jgFShBlDPOBKRVV9tIbayDLCyvvm43CoI6_Wwy0rpB77IqCDT25OP0oH2Au_atbUM/s1600/snap1.jpeg" imageanchor="1"><img border="0" height="225" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMv5UKVeEA3oLTMLwjDTG_W69LFVDhc3TfxSnZmo5hifQnLS7ftq9XbBI9Qw-509_u6HzzlScth-jgFShBlDPOBKRVV9tIbayDLCyvvm43CoI6_Wwy0rpB77IqCDT25OP0oH2Au_atbUM/s400/snap1.jpeg" width="400" /></a>

I was able to grab this image with a simple HTTP GET request to the camera's IP. Example: http://192.168.1.5/snap.jpeg

In order to enable this, I did have to turn on Anonymous Snapshots directly on the camera. Navigate to&nbsp;http://192.168.1.5/camera/config and click:

<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjo3Zlp3tkIR3zdrUXm4ULVIqRtB9YN5Mhc4ZXvKFT2qjRBr6SK2XL56DvozG62MdtD134XVQqGjGtzxWA8n1gUjjJHdt32P0YxWcfZRQxB_6czJzsZCWYjr6I_NEuCXaN2RBI-YJrfvIs/s1600/Screen+Shot+2019-02-07+at+11.11.05+AM.png" imageanchor="1"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjo3Zlp3tkIR3zdrUXm4ULVIqRtB9YN5Mhc4ZXvKFT2qjRBr6SK2XL56DvozG62MdtD134XVQqGjGtzxWA8n1gUjjJHdt32P0YxWcfZRQxB_6czJzsZCWYjr6I_NEuCXaN2RBI-YJrfvIs/s400/Screen+Shot+2019-02-07+at+11.11.05+AM.png" /></a>

Since I would be running my image capture tool within my local network, I did not need to expose the camera to the Internet.

While this camera placement works well for my every-day use, it contains a lot of extra data that isn't relevant to detecting a package, so I needed to crop each image down to just the area where I thought packages might be placed. Here is the result of my crop:

<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7-LU4SP0PnthxE7S_D3q8lZWktPAOEo0LTUwLmRglBV1y0O0sb5fFY_q3B3h7GwRKsSRE4XkKVYwfpaRjDon8oRNqYfugo2xuvySkILa5TCo34fCZSMFiEMFBeIW1CekX7yfP3hIJ4TQ/s1600/2019-02-07T11%253A04%253A17-07%253A00.jpeg" imageanchor="1"><img border="0" height="301" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7-LU4SP0PnthxE7S_D3q8lZWktPAOEo0LTUwLmRglBV1y0O0sb5fFY_q3B3h7GwRKsSRE4XkKVYwfpaRjDon8oRNqYfugo2xuvySkILa5TCo34fCZSMFiEMFBeIW1CekX7yfP3hIJ4TQ/s400/2019-02-07T11%253A04%253A17-07%253A00.jpeg" width="400" /></a>

I now had everything in place to build out an app to start capturing images. I wrote the app in Go (golang) as it is perfect for this type of systems programming. The app simply polls the camera every 10 minutes, grabs the image, crops it (if desired), and stores it in an S3 bucket or on the local file system.

The source code is available on <a href="https://github.com/ericdaugherty/imagefetcher">GitHub</a>.

I wrapped the app in a Docker container and deployed it on my Synology. The Docker image is available on <a href="https://hub.docker.com/r/ericdaugherty/imagefetcher">Docker Hub</a>. Here is a sample Docker run command:

```
docker run --restart always \
 -d \
 -e TZ='America/Denver' \
 -v /volume1/imagefetcher:/img \
 --name imagefetcher \
 ericdaugherty/imagefetcher \
 -imageURL http://192.168.1.5/snap.jpeg \
 -dir /img \
 -sleepHour 22 \
 -wakeHour 7 \
 -rect 0,400,900,1080
```
This creates and runs a new Docker container that captures the images, crops them, and stores them locally.

Since packages are generally not delivered in the middle of the night, and the night images are much harder to see, I decided to only run the image fetcher (and eventually the package detector) from 7a to 10p.&nbsp; So I added parameters to the ImageFetcher tool to stop capturing images overnight.

The <i>-e TZ='America/Denver'</i> parameter sets the timezone for the Docker container. This is important so that the timestamps are correct and the logic to sleep and wake work correctly.

The <i>-v /volume1/imagefetcher:/img</i> parameter maps the directory on the Synology to /img in the container, and then later the <i>-dir /img</i> specifies that the snapshots should be written to /img in the container, which will result in them being stored in /volume1/imagefetcher on the Synology.

If you would prefer to store the images on S3, you can add these parameters:

```
    -e AWS_ACCESS_KEY_ID='<Your Access Key ID' \
    -e AWS_SECRET_ACCESS_KEY='<Your Access Key Secret>' \
```
to the docker run command and this parameter:

```
    -s3Bucket <bucket name> \
```

to the imagefetcher command. You can then drop the <i>-v /volume1/imagefetcher:/img</i>&nbsp;and <i>-dir /img</i>, or keep them both and store the images twice!

Now you wait and capture data... I started with a month's worth of images before I trained the first model, but I continue to capture images and plan on training a new model with the larger set.

<h3>
Machine Learning Model</h3>
<div>
You should now have a S3 bucket or directory full of JPEG images. Now comes the fun part, you need to manually sort the images into two different labels.&nbsp; I chose the highly descriptive 'package' and 'nopackage' labels.&nbsp;</div>
<div>

</div>
<div>
I use a MacBook, so I used finder to quickly preview the images and run through them until I saw a change of state. Then I moved all the images into either the 'package' or 'nopackage' directory. Repeat until you've processed all of the images.</div>
<div>

</div>
<div>
This is pretty labor intensive, but it did go faster than I expected it.</div>
<div>

</div>
<div>
You should end up with two folders, named 'package' and 'nopackage'.</div>
<div>

</div>
<div>
I then spent quite a while trying to figure out how to train the model using SageMaker. I found this pretty frustrating as I'm not really fluent in Python, and it turns out the Machine Learning space is pretty large and not super-obvious to pick up. Luckily, I came across a post from Jud Valeski where he was building a similar tool to <a href="http://one.valeski.org/2018/12/machine-play.html">determine when the wind blew the covers off his patio furniture</a>. He used Google Vision for his solution, so I took a look.</div>
<div>

</div>
<div>
As it turns out, using Google Vision to build a simple model is drop dead simple. I signed up for Google Cloud account, created a project, and then created a new Google Vision model. To create the model, I simply had to zip up the 2 directories and upload it. In about 10 minutes, I had a functional model!</div>
<div>

</div>
<div>
Google also provides you a HTTP Endpoint that you can use to evaluate images against your model. You simply post a JSON body including your image base64 encoded, and it gives you back what label matches, along with its confidence level.</div>
<h3>
Package Detector</h3>
With the trained model in place and a public endpoint I can hit, all that was left was to build the final tool.

The final source code is available on <a href="https://github.com/ericdaugherty/packagedetector">GitHub</a>. The Docker image is also available on <a href="https://hub.docker.com/r/ericdaugherty/packagedetector">Docker Hub</a>.

I lifted much of the logic from the imagedetector to grab and crop the JPEG image. I then wrote new code to base64 encode the image and upload it to Google Vision. Based on the response, if a package is detected, an email is sent out to notify me.

The current version supports email as the notification tool.&nbsp; I leveraged <a href="https://aws.amazon.com/ses/">Amazon's Simple Email Service (SES)</a>, but you can use any SMTP server you have appropriate access to.

This tool supports two triggers. The simple approach is to specify a simple interval, ex: <i>-interval 5</i>&nbsp;and it will check every 5 minutes. However, I realized that the Unifi NVR is already doing motion detection, so if I could trigger based on that, it would only evaluate when there was a reason to do so. I came across a cool project by mzak on the Unifi Community Forums. Here is the <a href="https://github.com/mzac/unifi-video-mqtt">GitHub Repo</a>. Mzak realized that the NVR wrote a line to a log file (motion.log) every time motion was detected or ended. I leveraged his work to <a href="https://github.com/ericdaugherty/unifi-nvr-motiondetection">build a go library</a> that would also monitor the log file. To use this, you must map the location of the motion.log file into the docker container. I do so with <i>-v /volume1/docker/unifi-video/logs:/nvr</i> and then point the packagedetector at this location with the <i>-motionLog /nvr/motion.log</i> parameter.

You can run the docker using the following command:

```
sudo docker run \
    --restart always \
    -d \
    -e TZ='America/Denver' \
    -v /volume1/packagedetector:/pd \
    -v /volume1/unifi-video/logs:/nvr \
    --name packagedetector \
    ericdaugherty/packagedetector:latest \
    -imageURL http://192.168.1.5/snap.jpeg \
    -rect 0,400,900,1080 \
    -motionLog /nvr/motion.log \
    -cameraID AABBCCDD1122 \
    -gAuthJSON /pd/google-json-auth-file.json \
    -gVisionURL https://automl.googleapis.com/v1beta1/projects/... \
    -sleepHour 22 \
    -wakeHour 7 \
    -emailFrom test@example.com \
    -emailTo test@example.com \
    -emailServer email-smtp.us-east-1.amazonaws.com \
    -emailUser <amazon ses id> \
    -emailPass "<amazon ses password>" \
    -emailOnStart true
```
I now receive an email every time a new package is delivered!

Looking ahead, I'm interested in building in support for SMS or even push notifications, although I would also need to build an iOS app for that. I also plan on continuing to refine the model with additional images until I'm confident it will be correct nearly all the time.
