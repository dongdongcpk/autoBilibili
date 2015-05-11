#coding=utf-8

from bs4 import BeautifulSoup as bs
from baiduSearch import Search

def get_questions(soup):
	return soup.find_all('p', 'qtitle')

def get_answers(soup):
	return soup.find_all('div', 'qselect')

def get_qa_dict():
	'''
	return a dict, like this:
	{key: {'q': question, 'a': [answer1, answer2, answer3, answer4]}}
	'''
	soup = bs(open('dump.html'))
	questions = get_questions(soup)
	answers = get_answers(soup)
	qa_dict = {}
	for q, a in zip(questions, answers):
		q_list = q.text.split(' ')
		key = q_list[0][1:]
		q = q_list[1]
		try:
			a = a.text.split()
		except:
			a = []
		qa_dict[key] = {'q': q, 'a': a}
	return qa_dict

if __name__ == '__main__':
	qa_dict = get_qa_dict()
	s = Search()
	for k, v in qa_dict.items():
		# print v['q'], type(v['q'])
		answer = s.select_key(v['q'].encode('utf-8'), v['a'])
		print k, answer
