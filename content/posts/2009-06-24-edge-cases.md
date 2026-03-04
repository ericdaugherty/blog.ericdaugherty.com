---
title: "Edge Cases"
date: 2009-06-24T15:58:00.002Z
url: /2009/06/edge-cases.html
draft: false
---

In tools like Outlook, there are an impossible number of ways users can interact with the tool.  This creates lots of 'edge cases' that don't get tested or developed for.<div><br /></div><div>Here is one:</div><div><ol><li>Use the default setting that does not have the BCC line shown.</li><li>Send an email with BCCs by clicking on the To: button and adding entries to the BCC line in the dialog box.</li><li>Send the message</li><li>Realize you want to reuse the body in a new message.</li><li>Open the sent message and click resend.  </li><li>Type in a new To: address</li><li>Send it to everyone you previously BCC'ed because Outlook doesn't show you the BCC line, even though it has entries.</li></ol><div>Oops.</div><div><br /></div><div>This is an edge case where adding a user to the BCC line causes it to be displayed, but opening/resending an email with users in the BCC line DOES NOT cause it to be displayed.  The trigger logic is flawed, but you don't realize it is flawed unless you are aware of other ways that a specific state can occur.  In this case, the logic to display the BCC line should be triggered by the 'state' of having entries in the BCC line, not the event of adding an address to the BCC line.</div></div>
