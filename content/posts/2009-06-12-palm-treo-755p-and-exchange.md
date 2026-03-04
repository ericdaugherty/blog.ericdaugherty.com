---
title: "Palm Treo 755p and Exchange"
date: 2009-06-12T13:49:00.002Z
url: /2009/06/palm-treo-755p-and-exchange.html
draft: false
---

My company upgraded/migrated our Windows Domain last weekend, and as a result, my Treo 755p's ActiveSync Support stopped working.  When I entered the setup information and tried to run the initial Sync, I got the error codes: 1913 4828.<div><br /></div><div>There is some confusion about what this error code means.  It can often be related to SSL certificate issues, which may have been part of my problem.  I found this page very helpful to debug the SSL issues:  <a href="http://kb.palm.com/wps/portal/kb/common/article/16733_en.html">http://kb.palm.com/wps/portal/kb/common/article/16733_en.html</a></div><div><br /></div><div>Once I had that working (I did have to change the server name to match our certificate) I was still having issues, and I came across this post: <a href="http://episteme.arstechnica.com/eve/forums/a/tpc/f/579009962631/m/417009683931">http://episteme.arstechnica.com/eve/forums/a/tpc/f/579009962631/m/417009683931</a> that suggested the issue was the ActiveSync security policy.  I tracked down our IT guy and cajoled him into testing out removing the policy, since ours didn't really do anything anyway.  It worked!  The odd thing is that the old domain seemed to have a policy as well but something must be different.  </div><div><br /></div><div>So apparently the Treo (Versamail 3.5.5) doesn't support ActiveSync with security policies.  Ya, ya, time to upgrade to a real phone...</div>
