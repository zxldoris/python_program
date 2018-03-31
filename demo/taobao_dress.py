# coding=utf-8
# -*- coding: UTF-8 -*-

import urllib2
import re


class TaobaoDress:
    # 获取网页源码
    def get_page(self):
        url = 'https://s.taobao.com/search?q=连衣裙'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
        return content

    # 解析提炼内容
    def analysis(self, content):
        regex = '"pid".*?"title":"(.*?)[a-z]?"'
        pattern = re.compile(regex)
        items = re.findall(pattern, content)
        return items

    # 保存 名称：价格
    def save(self, items):
        for i in items:
            with open('taobao_dress.txt', 'w') as f:
                f.write(i)

    # 运行程序
    def run(self):
        content = self.get_page()
        items = self.analysis(content)
        for i in items:
            print(i)
        self.save(items)


if __name__ == '__main__':
    taobao_dress = TaobaoDress()
    taobao_dress.run()
