#coding=utf-8

import urllib2 as url
import urllib
import re

def baidu_search(keyword):
    p = {'wd': keyword}
    res = url.urlopen("http://www.baidu.com/s?" + urllib.urlencode(p))
    html = res.read()
    return html

def getList(regex, text):
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr

def getMatch(regex, text):
    res = re.findall(regex, text)
    if res:
        return res[0]
    return ""

def clearTag(text):
    p = re.compile(u'<[^>]+>')
    retval = p.sub("", text)
    return retval

html = baidu_search('天下无贼')
print html
# content = unicode(html, 'utf-8', 'ignore')
# 
# arrList = getList(u"<table.*?class=\"result\".*?>.*?<\/a>", content)
# for item in arrList:
#     regex = u"<h3.*?class=\"t\".*?><a.*?href=\"(.*?)\".*?>(.*?)<\/a>"
#     link = getMatch(regex,item)
#     url = link[0]
#     title = clearTag(link[1]).encode('utf8')
#     print url
#     print title