---
title: "Rails on GoDaddy"
date: 2007-07-31T04:14:00Z
url: /2007/07/rails-on-godaddy.html
draft: false
---
I decided to play with Ruby on Rails a little more and was just reminded of the painful process to get Rails working at GoDaddy.

First, you can have Java or Rails, but not both.  But as I <a href="http://www.ericdaugherty.com/blog/2007/05/guice-burned-by-godaddy.html">posted earlier</a>, Java is near useless at GoDaddy anyway.

So, the key steps to getting your Ruby on Rails app deployed at GoDaddy are:

Setup at GoDaddy:
1. Log in to the GoDaddy Hosting Control Center
2. Make sure Java is disabled (under Language Options).  If it is enabled, you can't deploy a Rails application.  Change the setting to none (and you'll need to wait 24 hours for your site(s) to be moved to a new server).
3. Log into the CGI control panel and create a Rails application directory.
4. Create a symbolic link to your newly created rails directory.

Local Edits:
1. Freeze your gems: `rake rails:freeze:gems`
2. Edit your dispatch.* files to reference #!/usr/local/bin/ruby

Upload:
1. Upload your rails application to the rails directory.
2. Chmod the dispatch.* files to 755 (in <a href="http://sourceforge.net/projects/filezilla">FileZilla</a>, right click and select File Attributes).
3. Wait.  GoDaddy won't recognized new .htaccess files for about an hour, so go do something else and come back later.

Test:
1. Test your app.  Hopefully it works.  If not, good luck.  A couple things you can try:
1a. Enable your Error Log in the hosting control panel, wait an hour, try again and view your log file in the CGI control panel.
1b. Download the <rails>/log/production.log log file.
2. Change to FastCGI.  Update your .htaccess file and change the dispatch.cgi reference to dispatch.fcgi.

I omitted the DB setup.  You'll need to create a database using the control panel and update your database.yml file with the appropriate information.

It isn't great, but if you already have GoDaddy hosting, it is workable.
