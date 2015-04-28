#coding=utf-8

import cookielib
import urllib2
import urllib

baidu_url = 'http://www.baidu.com'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
resp = urllib2.urlopen(baidu_url)
print resp.read()
print '*' * 20
login_url = 'https://passport.baidu.com/?login'
para = {
    'userName': '',
    'password': '',
    'mem_pass': 'on'
        }
post_data = urllib.urlencode(para)
req = urllib2.Request(login_url, post_data)
req.add_header('User-Agent', 'userAgentIE9')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_header('Cache-Control', 'no-cache')
req.add_header('Accept', '*/*')
req.add_header('Connection', 'Keep-Alive')
resp = urllib2.urlopen(req)
print resp.read()


# if __name__ == '__main__':
#     pass