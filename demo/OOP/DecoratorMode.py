# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


class BeDecorator(object):
    def be_edit_fun(self):
        print('be edit fun')

    def be_keep_fun(self):
        print('be keep fun')


class Decrator:
    def __init__(self, dec):
        self._dec = dec()

    def be_edit_fun(self):
        print('start')
        self._dec.be_edit_fun()

    def be_keep_fun(self):
        self._dec.be_keep_fun()


if __name__ == '__main__':
    bd = BeDecorator()
    bd.be_edit_fun()
    bd.be_keep_fun()

    dr = Decrator(BeDecorator)
    dr.be_keep_fun()
    dr.be_edit_fun()
