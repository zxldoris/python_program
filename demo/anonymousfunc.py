# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
anontmous fuction
"""


# function
def func(x): return x > 5


print filter(func, range(1, 11))

# lambda表达式
print filter(lambda x: x > 5, range(1, 11))
# 返回类型无论输入什么输出list
print map(lambda x, y: x + x, range(1, 11), range(11, 21))

print sum(range(1, 101))
print reduce(lambda x, y: x + y, range(1, 101), 0)
#强制转换为字典类型
print dict([(x, x * 2)for x in range(1, 10)])
