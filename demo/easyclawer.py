# # coding=gbk
# # coding=utf-8
# # -*- coding: UTF-8 -*-
# # url: https://www.qiushibaike.com/textnew/
# import re
# import urllib2
#
# if __name__ == "__main__":
#     # ץȡ����һ����ҳ������https://www.qiushibaike.com/textnew/page/2/?s=5073277
#     # ��������
#     for page in range(1, 36):
#         url = 'https://www.qiushibaike.com/textnew/page/' + str(page) + '/?s=5073277'
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ��) Gecko/20100101 Firefox/59.0"}
#         try:
#             request = urllib2.Request(url=url, headers=headers)
#             # ������Ӧ
#             response = urllib2.urlopen(request)
#             content = response.read()
#         except urllib2.HTTPError as e:
#             print(e)
#             exit()
#         except urllib2.URLError as e:
#             print(e)
#             exit()
#         # ��ȡ����
#         regex = re.compile('<span>([^<].*?[^/>])</span>', re.S)
#         items = re.findall(regex, content)
#         for i in items:
#             print(i)
#         # �������
#         for i in items:
#             with open('easyclawer.txt', 'a+') as f:
#                 f.write(i + '\n')
#                 # ��ȡʣ��ҳ�������

# �����ع� ������� ���ݺ����ݵķ�װ

import urllib2
import re


# ����һ��������
class Spider(object):
    # ���췽��
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/textnew/page/%s/?s=5073277'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; ��) Gecko/20100101 Firefox/59.0'

    # ��ȡ��ҳԴ��
    def get_page(self, page_index):
        headers = {"User-Agent": self.user_agent}
        try:
            request = urllib2.Request(url=self.url % str(page_index), headers=headers)
            # ������Ӧ
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.HTTPError as e:
            print(e)
            exit()
        except urllib2.URLError as e:
            print(e)
            exit()
        return content

    # ������ҳԴ��
    def analysis(self, content):
        regex = re.compile('<span>([^<].*?[^/>])</span>', re.S)
        items = re.findall(regex, content)
        return items

    # ����
    def save(self, items):
        for i in items:
            with open('easyclawer.txt', 'a+') as f:
                f.write(i + '\n')

    def run(self):
        for i in range(1, 35):
            print('starting')
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items)
            print()

if __name__ == '__main__':
    spider = Spider()
    spider.run()
