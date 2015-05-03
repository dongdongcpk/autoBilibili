#coding=utf-8

import cookielib
import urllib2
import urllib
from bs4 import BeautifulSoup as bs

headers = {
    'Host': 'account.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Referer': 'https://account.bilibili.com/login',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://account.bilibili.com'
}

class Bilibili:
    def __init__(self):
        #登录的url
        self.login_url = 'https://account.bilibili.com/login'
        #代理ip
        self.proxy_url = 'http://120.193.146.97:843'
        #头部信息
        self.login_headers = headers
        #手机号，密码，验证码
        self.userid = '18698666910'
        self.pwd = ''
        self.vdcode = ''
        
        #设置代理
        self.proxy = urllib2.ProxyHandler({'http': self.proxy_url})
        #设置cookie
        self.cookie = cookielib.CookieJar()
        #设置cookie处理器
        self.cookie_handler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookie_handler, self.proxy, urllib2.HTTPHandler)
        
    def post(self, vdcode):
        '''
        发送登录post请求
        '''
        self.vdcode = vdcode
        self.post = {
            'act': 'login',
            'gourl': 'https://account.bilibili.com/login/dologin',
            'keeptime': 604800,
            'userid': self.userid,
            'pwd': self.pwd,
            'vdcode': self.vdcode,
        }
        #将post数据进行编码转换
        self.post_data = urllib.urlencode(self.post)
        req = urllib2.Request(self.login_url, self.post_data, self.login_headers)
        resp = self.opener.open(req)
        html = resp.read()
        return html
    
    def open(self):
        '''
        打开login页面
        '''
        req = urllib2.Request(self.login_url, headers = self.login_headers)
        resp = self.opener.open(req)
        return resp
        
    def get_vdcode(self):
        '''
        获取验证码
        '''
        vdcode_url = 'https://account.bilibili.com/captcha'
        req = urllib2.Request(vdcode_url, headers = headers)
        resp = self.opener.open(req)
        html = resp.read()
        f = open('./vdcode.png', 'w')
        f.write(html)
        f.close()

if __name__ == '__main__':
    bili = Bilibili()
    bili.open()
    for i in bili.cookie:
        headers['Cookie'] = i.name + '=' + i.value
    bili.get_vdcode()
    vdcode = raw_input('请打开当前路径下名为vdcode.png的图片，输入验证码：')
    html = bili.post(vdcode)
    soup = bs(html)
    print soup.prettify()
    
    
    
    
    
    
    
    
    
        
        
        
        
        