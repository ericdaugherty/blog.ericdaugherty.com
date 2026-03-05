---
title: "Embedding PHP in HTML files and GoDaddy Statistics"
date: 2009-11-25T02:10:00.002Z
url: /2009/11/embedding-php-in-html-files-and-godaddy.html
draft: false
---

I host my site at GoDaddy, for better or worse.  The site is comprised entirely of 'static' HTML pages at GoDaddy.  The Blog is managed using Blogger, but it publishes HTML files via FTP to GoDaddy, and the rest of the content is HTML files I manage directly.<br /><br />I wanted to avoid the redundant header/footer/etc. structures in my pages since I was editing them manually.  So, I setup my site to parse the HTML files as PHP files, and then used PHP includes:

```php
<?php include 'head.php' ?>
```
to build the pages on the fly.  This allows me to maintain each page using simple HTML and avoid duplication of boilerplate HTML.  This works because I added the following line to the .htaccess file:

```
AddHandler x-httpd-php .html .htm
```
This solutions works well, but unfortunately destroys GoDaddy's web statistics (/stats/) output.  Apache attempts to parse these html files as well, but because of how they setup permissions (you have none), it fails and results in an HTTP 500 error.<br /><br />This would be a simple fix if I could edit the .htaccess file in the stats directory.  I could simply override the .html handler back to the default, and avoid the PHP processing.<br /><br />Instead, it looks like my options are:<br /><ul><li>FTP the files to my local machine and view them there.</li><li>Create a script that copies them to a different directory (with the correct permissions and .htaccess override) and view them there.</li><li>Change my files to .htm or another extension that doesn't conflict with the /stats files (.html).</li><li>Get Creative.</li></ul>Changing the file extensions isn't really an option for me as the entire point of mapping the .html files as PHP is to maintain all the existing incoming links without doing tons of rewrites.  I view that stats infrequently enough that the first option is workable, but it is annoying.  So I got creative...<br /><br />My hack was simply to create a PHP file that reads the files out of the /stats directory.  Here is a crude version:

```php
<?php
  $file=fopen("stats/INDEX.html","r");
  while(!feof($file))
  {
    echo fgets($file);
  }
  fclose($file);
?>
```
You could expand this to be dynamically driven from a request parameter.  Again, this is a HACK, but for the specific purpose it works.  It should of course be secured if you want to maintain the security defined in the original /stats directory.
