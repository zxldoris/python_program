# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
anontmous fuction
"""


# function
def func(x): return x > 5


print filter(func, range(1, 11))

# lambda���ʽ
print filter(lambda x: x > 5, range(1, 11))
# ����������������ʲô���list
print map(lambda x, y: x + x, range(1, 11), range(11, 21))

print sum(range(1, 101))
print reduce(lambda x, y: x + y, range(1, 101), 0)
#ǿ��ת��Ϊ�ֵ�����
print dict([(x, x * 2)for x in range(1, 10)])
