# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
import time

now_time = time.localtime()
wday = now_time.tm_wday + 1
day = now_time.tm_mday
datestr = '%d-%d-%d %d:%d:%d ����%d ' % (now_time.tm_year, now_time.tm_mon,
                                       now_time.tm_mday, now_time.tm_hour,
                                       now_time.tm_min, now_time.tm_sec, wday)
# result += '��Ѯ' if day<=15 else '��Ѯ'
if day <= 10:
    print(datestr + '��Ѯ')
elif day > 10 and day <= 20:
    print(datestr + '��Ѯ')
else:
    print(datestr + '��Ѯ')
