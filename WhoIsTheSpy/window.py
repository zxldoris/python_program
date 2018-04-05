#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
import tkinter
from tkinter.ttk import *


class Win:
    def __init__(self):
        self._pnum = 0
        self._cardflag = 0  # 标志为1， 表示开始发牌
        self._player = dict()
        self._voteflag = 0  # 几号玩家被选，调用对应玩家的setter vote(1)
        self._txt = None

    def opt(self):
        root = tkinter.Tk()
        root.title("谁是卧底")
        root.geometry('580x300+0+0')

        # 创建Label
        label = Label(root)
        label.pack(side="top")

        subframe = Frame(root)
        subframe.pack(side="bottom")

        # 创建组合框1
        cbb1 = Combobox(subframe, width=12, state="readonly")
        cbb1["values"] = (3, 4, 5, 6, 7, 8)
        cbb1.grid(column=1, row=1)
        cbb1.current(0)
        # 创建开始Button
        bst = Button(subframe, text="开始", command=lambda: self.bstart(label,cbb1))
        bst.grid(column=2, row=1)

        # 创建显示词语Button
        bsh = Button(subframe, text="显示卡牌", command=lambda: self.bshow(label))
        bsh.grid(column=3, row=1)

        # 创建组合框2
        # var2 = tkinter.StringVar()
        cbb2 = Combobox(subframe, width=12, state="readonly")
        cbb2["values"] = (3, 4, 5, 6, 7, 8)
        cbb2.grid(column=4, row=1)

        # 创建投票Button
        bvt = Button(subframe, text="投票", command=lambda: self.bvote(label))
        bvt.grid(column=5, row=1)

        # 创建关闭Button
        bcl = Button(subframe, text="关闭", command=self.bclose)
        bcl.grid(column=6, row=1)

        root.mainloop()

    def bstart(self, label,cbb1):
        # 获取组合框1数据pnum， 设定玩家数setter，调用发牌程序（设置一个标志）
        label.configure(text="游戏开始")


    def bshow(self, label):
        # 显示玩家字典players setter
        label.configure(text="玩家1：白菜")

    def bvote(self, label):
        # 获取组合框2数据
        label.configure(text="玩家1获得1票")

    def bclose(self):
        exit()

    @property
    def pnum(self):
        return self._pnum

    @pnum.setter
    def pnum(self, value):
        self._pnum = value

    @property
    def cardflag(self):
        return self._cardflag

    @cardflag.setter
    def cardflag(self, value):
        self._cardflag = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def voteflag(self):
        return self._voteflag

    @voteflag.setter
    def voteflag(self, value):
        self._voteflag = value

    @property
    def text(self):
        return self._txt

    @text.setter
    def text(self, value):
        self._txt = value


def window():
    return Win()


if __name__ == '__main__':
    w = Win()
    w.opt()
    print(w.text)
