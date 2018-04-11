#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
# -----------------------------------------------
# getter setter 按照属性的方式赋值，不是按照方法传参
# -----------------------------------------------

__author__ = 'zxl'


class Player(object):
    def __init__(self):
        self._name = 0
        self._card = None
        self._vote = 0

    def player_card(self, flag=0):
        self.card = self.cuword[0] if flag == 0 else self.cuword[1]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

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


if __name__ == '__main__':
    pl = []
    for i in range(0, 3):
        p = Player()
        pl.append(p)
    pl[1].vote = 1
    pl[1].vote = 1
    pl[1].vote = 1
    pl[0].vote = 1
    print(pl[1].vote)
    print(pl[0].vote)
