# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
# 运算符重载
class B(object):
    def __add__(self, other):
        return 10

    def __mul__(self, other):
        return 20


b1 = B()
b2 = B()
print(b1 + b2)
