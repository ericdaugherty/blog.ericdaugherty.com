---
title: "Site Migration"
date: 2015-08-05T23:34:00.001Z
url: /2015/08/site-migration.html
draft: false
---
After hosting this site on GoDaddy for many years, I've decided to migrate it to Amazon via S3. &nbsp;Amazon has some great features for hosting static websites, although I've gone 'bare bones' to start. &nbsp;I'm just hosting using an S3 bucket. &nbsp;I'm using the <a href="http://wwwizer.com/naked-domain-redirect">wwwizer Naked Redirect service</a> to redirect ericdaugherty.com to www.ericdaugherty.com, and then hosting the site out of a S3 bucket.
<div>
Amazon has a DNS server (Route 53) and CDN (CloudFront) that are easy and inexpensive to use, but I don't think I need them yet. &nbsp;For now, I'm still using GoDaddy's DNS Server and the wwwizer 'hack' instead of Route 53.</div>
<div>

</div>
<div>
The previous site utilized somewhat of a 'poor man's&nbsp;template engine'. &nbsp;I had a html file for each page on the site, but had Apache evaluate them as PHP files and I used PHP Includes to build up the page using common components.</div>
<div>

</div>
<div>
Moving to a fully static website meant I needed a real template engine. &nbsp;I selected <a href="http://jekyllrb.com/">Jekyll</a>&nbsp;and migrated the site over. &nbsp;It was a pretty straight forward migration and ended up reducing the size of each file as I could use a true template instead of just having common components.</div>
<div>

</div>
<div>
I then use the AWS console tool to upload the generated website files to S3 for an easy deployment, also allowing me to finally retire FileZilla from my tool chain.</div>
<div>

</div>
<div>
Amazon has some pretty good <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html">guides</a> to doing this, but I also used two good blog posts:&nbsp;<a href="http://nicluo.com/amazon-s3-on-domain-root-without-route-53/">Amazon S3 on Domain Root, without Route 53</a>&nbsp;and&nbsp;<a href="http://www.michaelgallego.fr/blog/2013/08/27/static-website-on-s3-cloudfront-and-route-53-the-right-way/">Static website on S3, CloudFront and Route 53, the right way!</a></div>
<div>

</div>
<div>
The blog portion of the site is still hosted at Blogger, which has and continues to work well. &nbsp;</div>
<div>

</div>
<div>
This also forced me to make a few updates to the site, fixing some broken links and removing some no-longer-relevant sections.</div>
<div>

</div>
<div>
Plus it gave me an excuse to finally post on the blog.</div>
