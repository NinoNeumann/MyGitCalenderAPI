# 项目来源
https://github.com/Zfour/python_github_calendar_api.git
## 原理
通过python爬取github主页的html并从中提取装载gitcalender的table标签里面的每日提交信息，然后将其传给js脚本并生成一个calender的挂件。
## 原项目存在的问题
github可能是把存放calender的table修改了，所以原项目中的正则匹配失效了，所以就git不到。
## 我做了些什么
就是重新写了匹配的方式，不能保证以后github再改它不会失效。
## 使用方法
直接在网址上输入: \
 ```https://my-git-calender-api.vercel.app/api/?<username>``` \
 例如: \
```https://my-git-calender-api.vercel.app/api/?NinoNeumann```
