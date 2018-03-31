# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
# python3
import urllib2, urllib

if __name__ == '__main__':
    # 发送请求
    url = "https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fwww.oschina.net%2F"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/59.0"}
    data = {'email': 'dhfad@gmail.com', 'pwd': 'dhfkadjk'}
    request = urllib2.Request(url=url, data=urllib.urlencode(data), headers=headers)
    # 接受响应
    response = urllib2.urlopen(request)
    print(response.read())
