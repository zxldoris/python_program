# coding=utf-8
# -*- coding: UTF-8 -*-
import urllib2
import re
import os


# 声明一个爬虫类
class Spider(object):
    # 构造方法
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/59.0'

    # 获取网页源码
    def get_page(self, page_index):
        headers = {"User-Agent": self.user_agent}
        try:
            request = urllib2.Request(url=self.url % str(page_index), headers=headers)
            # 接受响应
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.HTTPError as e:
            print(e)
            exit()
        except urllib2.URLError as e:
            print(e)
            exit()
        return content

    # 分析网页源码
    def analysis(self, content):
        regex = re.compile('<a title="(.*?)" href=.+</a>')
        items = re.findall(regex, content)
        return items

    # 保存
    def save(self, items):
        path = 'spiderteacher'
        file_path = path + '/' + items[0].decode('UTF-8') + '.txt'
        print(file_path)
        if not os.path.exists(path):
            os.mkdir(path)
        for i in items:
            with open(file_path, 'a+') as f:
                f.write(i + '\n')

    def run(self):
        for i in range(1, 29):
            print('starting', i)
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items)
        print('finished')


if __name__ == '__main__':
    spider = Spider()
    spider.run()
