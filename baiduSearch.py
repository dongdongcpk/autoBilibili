#coding=utf-8

import urllib2 as url
import urllib
from bs4 import BeautifulSoup as bs

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




