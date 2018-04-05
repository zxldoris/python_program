#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
# -----------------------------------------------
# getter setter 按照属性的方式赋值，不是按照方法传参
# -----------------------------------------------

__author__ = 'zxl'

REF = [[], [], [], [], []]
CUWORD = ["萝卜", "白菜"]


class P(object):
    def __init__(self):
        self._card = None
        self._vote = 0

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value):
        self._card = value

    @property
    def vote(self):
        return self._vote

    @vote.setter
    def vote(self, value):  # value在调用处设置为1
        self._vote += value

    def player_card(self, flag=0):
        self.card = CUWORD[0] if flag == 0 else CUWORD[1]


def player():
    return P()

if __name__ == '__main__':
    p = P()
    p.player_card(flag=1)
    print(p.card)
