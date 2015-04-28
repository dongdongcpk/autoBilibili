#coding=utf-8

import urllib2 as url
import urllib
from bs4 import BeautifulSoup as bs

def baidu_search(keyword):
    p = {'wd': keyword}
    res = url.urlopen("http://www.baidu.com/s?" + urllib.urlencode(p))
    html = res.read()
    return html

html = baidu_search('静夜思的作者是谁')
soup = bs(html)
# print soup.get_text()
# print soup.prettify()
author_list = ['杜甫', '李清照', '王维', '李白']
author_dict = {}
for i in author_list:
    count = len(soup.find_all(text = i))
    author_dict[i] = count
    
print author_dict
sorted_author_list = sorted(author_dict, key = lambda x : x[1], reverse = True)
print sorted_author_list
print '作者是：' + sorted_author_list[0]

