#coding=utf-8

import urllib2 as url
import urllib
from bs4 import BeautifulSoup as bs

# def baidu_search(keyword):
#     p = {'wd': keyword}
#     res = url.urlopen("http://www.baidu.com/s?" + urllib.urlencode(p))
#     html = res.read()
#     return html

# html = baidu_search('静夜思的作者是谁')
# soup = bs(html)
# # print soup.get_text()
# # print soup.prettify()
# author_list = ['杜甫', '李清照', '王维', '李白']
# author_dict = {}
# for i in author_list:
#     count = len(soup.find_all(text = i))
#     author_dict[i] = count
    
# print author_dict
# sorted_author_list = sorted(author_dict, key = lambda x : x[1], reverse = True)
# print sorted_author_list
# print '作者是：' + sorted_author_list[0]

class Search():
	def baidu_search(self, keyword):
	    p = {'wd': keyword}
	    res = url.urlopen("http://www.baidu.com/s?" + urllib.urlencode(p))
	    html = res.read()
	    return html

	def select_key(self, question, answers):
		html = self.baidu_search(question)
		soup = bs(html)
		answer_dict = {}
		for a in answers:
		    count = len(soup.find_all(text = a))
		    answer_dict[a] = count
		sorted_answer_list = sorted(answer_dict, key = lambda x : x[1], reverse = True)
		return sorted_answer_list[0]




