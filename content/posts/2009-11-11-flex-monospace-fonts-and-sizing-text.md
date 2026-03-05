---
title: "Flex: Monospace Fonts and Sizing Text Components"
date: 2009-11-11T22:30:00.004Z
url: /2009/11/flex-monospace-fonts-and-sizing-text.html
draft: false
---

For a recent project I wanted to simulate an 80x24 terminal window in a Flex application.  To accomplish this I needed a fixed width (monospace) font and the ability to size the text control for the current font.  Here is what I did:<br /><br />First, I needed a monospace (fixed width) font.  You can embed your own fonts in a Flash SWF, but that was overkill for this effort.  You could specify a specific font, such as 'Courier New' that is monospace.  However, there can be issues if the client's device does not have the specific font face.  <a href="http://livedocs.adobe.com/flex/3/html/fonts_03.html#136858">Device Fonts</a> often serve as a fallback font if the specific font requested does not exist on the user's device.  In this case, I didn't want to select a specific font, I just wanted the default monospace font.  So I used the <span style="font-style: italic;">_typewriter</span> font (the other types are <span style="font-style: italic;">_sans</span> and <span style="font-style: italic;">_serif</span>).

```actionscript
<mx:text id="myText" fontfamily="_typewriter" />
```
Once I had a monospace font, I needed to determine the proper size of the control for an 80x24 terminal.  I started by simply setting the text control to an 80 character wide (and then 24 character high) string and noting the size, but I needed something that would work easily at runtime.  I created this quick helper method that would resize my control:

```actionscript
private function setSize(control:mx.controls.Label, charWidth:int, charHeight:int, defaultText:String = "") : void {

 var testString:String = "0";
 var width:int = control.width + (control.measureText(testString).width * charWidth);
 var height:int = control.height + (control.measureText(testString).height * charHeight);

 control.text = defaultText;
 control.width = width;
 control.height = height;
}
```
I set this method to be called when the container's creationComplete event fired.  This method assumes that the control is set to an empty string initially, and accepts an optional defaultText parameter if you wish to initialize it.<br /><br />The measureText method returns the size of the text, but not the surrounding control borders, so I added the default control size to the text size to achieve the proper control size.
