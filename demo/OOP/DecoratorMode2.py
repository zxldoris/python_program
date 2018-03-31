# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


class Water:
    def __init__(self):
        self.name = 'Water'

    def show(self):
        print(self.name)


class Deco:
    def show(self):
        print(self.name)


class Sugar(Deco):
    def __init__(self, water):
        self.name = 'Sugar'
        self.water = water

    def show(self):
        print(self.name)
        print(self.water.name)


class Salt(Deco):
    def __init__(self, water):
        self.name = 'salt'
        self.water = water

    def show(self):
        print(self.name)
        print(self.water.name)


if __name__ == '__main__':
    w = Water()
    s1 = Sugar(w)
    s1.show()

    s2 = Salt(w)
    s2.show()
