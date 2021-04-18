# Automation without writing a single line of code
<p>Due to the progress of technology, the threshold of various industries is getting lower and lower.
It used to be said that mastering Selenium equals with automation. Selenium seems to be a fancy stuff. But  nowadays selenium is just the basic. Everyone is busy in working on a variety of wheels more and more, and it become much more easier to get started with automation.
</p>
<p>When we talk about automation, we generally talk about automated testing frameworks.
</p>
<p>
Selenium-based testing framework includes:</p>

 - robot framework
 - webdriver
 - Appium
<p>JS language-based testing tools have:  </p>
 
 - cypress
 - puppeteer
<p>Each automation framework and tool has its own advantages, right? The 
</p>
<p>There are two main points to consider automation frameworks. </p>
<p>1. low learning costs; </p>
<p>2. easy and fast to use and maintain.</p>
None of the above frameworks can meet these two low thresholds. 
Now Microsoft has directly lowered the threshold to zero.

## playwright-python 
Recently, Microsoft has open-sourced a project called "playwright-python". 
This project is a pure automation tool for the Python language, even you don't have to write the code to automated the functions. 
For newbies, just try it once, simply read the code, and it's done.
If the page changes, the only thing to do is recording it again, which is too convenient. The key is that you can choose the language, Both JS and python can do.
Playwright is a powerful Python library that automates major browser automation such as Chromium, Firefox, WebKit, etc. 
With just one API, and it supports running in both headless and head modes.
Playwright offers automation technology that is portable, powerful, reliable and fast, supporting Linux, Mac and Windows operating systems.

## How to use playwright-python
1. Install playwright package (Precondition: Python3.7+)
```
pip install playwright
```
2. Install the browser driver file (chromium, firefox, Webkit and etc)                                                                                                                                                                                                                                                         （Takes some time）
```
python -m playwright install
```
3. Recording
<p>
With Playwright there is no need to write a single line of code, 
we just manually operate the browser and it will record our actions 
and then automatically generate the code script.

Here is the recorded command codegen, just one line. 
You can use --help to see how to use it, 
or simply add a url link directly after the command, 
or add options if you have other needs.</p>
```
C:\Users\Administrator>python -m playwright codegen --help
Usage: npx playwright codegen [options] [url]

open page and generate code for user actions

Options:
  -o, --output <file name>     saves the generated script to a file
  --target <language>          language to use, one of javascript, python, python-async, csharp (default: "python")
  -b, --browser <browserType>  browser to use, one of cr, chromium, ff, firefox, wk, webkit (default: "chromium")
  --channel <channel>          Chromium distribution channel, "chrome", "chrome-beta", "msedge-dev", etc
  --color-scheme <scheme>      emulate preferred color scheme, "light" or "dark"
  --device <deviceName>        emulate device, for example  "iPhone 11"
  --geolocation <coordinates>  specify geolocation coordinates, for example "37.819722,-122.478611"
  --load-storage <filename>    load context storage state from the file, previously saved with --save-storage
  --lang <language>            specify language / locale, for example "en-GB"
  --proxy-server <proxy>       specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"
  --save-storage <filename>    save context storage state at the end, for later use with --load-storage
  --timezone <time zone>       time zone to emulate, for example "Europe/Rome"
  --timeout <timeout>          timeout for Playwright actions in milliseconds (default: "10000")
  --user-agent <ua string>     specify user agent string
  --viewport-size <size>       specify browser viewport size in pixels, for example "1280, 720"
  -h, --help                   display help for command

Examples:

  $ codegen
  $ codegen --target=python
  $ codegen -b webkit https://example.com
```
<p>options含义：</p>
<p>-o：将录制的脚本保存到一个文件</p>
<p>--target：规定生成脚本的语言，有JS和Python两种，默认为Python</p>
<p>-b：指定浏览器驱动</p>
<p>For example, I want to search in baidu.com, drive it with chromium, 
and save the result as a python file of my.py.</p>

```
python -m playwright codegen --target python -o test.py -b chromium https://www.baidu.com
```