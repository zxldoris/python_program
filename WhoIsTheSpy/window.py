#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
import tkinter
from tkinter.ttk import *
import playgame
import player


class Win:
    def __init__(self, playgame):
        self._pnum = 0  # 当轮玩家数
        self.playgame = playgame  # PlayGame类
        self.wplayers = []
        self.wpcuword = []  # 随机选出的一对牌
        self.wnlayers = []
        self._voteflag = 0  # 几号玩家被选，调用对应玩家的setter vote(1)
        self._txt = []  # label上面显示的文本
        self.bstpress = 0  # 开始按键标志 为1-->已经按下
        self.bshshowflag = 1  # button 显示 标识
        self.bshowflag = 0  # 当前玩家数
        self.bshpress = 1  # 显示按键点击几次标志
        self.bvtpress = 1  # 投票按键点击几次标识
        self.tmp = []

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
        cbb1.bind("<<ComboboxSelected>>", self.getpnum(cbb1))

        # 创建开始Button
        bst = Button(subframe, text="开始", command=lambda: self.bstart(label, cbb1))
        bst.grid(column=2, row=1)

        # 创建组合框2
        cbb2 = Combobox(subframe, width=12, state="readonly")
        # 创建显示词语Button
        bsh = Button(subframe, text="显示卡牌", command=lambda: self.bshow(label, cbb2))
        bsh.grid(column=3, row=1)

        cbb2.grid(column=4, row=1)
        cbb2.bind("<<ComboboxSelected>>", self.getpnum(cbb2))

        # 创建投票Button
        bvt = Button(subframe, text="投票", command=lambda: self.bvote(label, cbb2))
        bvt.grid(column=5, row=1)

        # 创建关闭Button
        bcl = Button(subframe, text="关闭", command=self.bclose)
        bcl.grid(column=6, row=1)

        root.mainloop()

    def getpnum(self, cbb1):
        pass

    def bstart(self, label, cbb1):
        # 获取组合框1数据pnum， 设定玩家数setter，调用发牌程序（设置一个标志）
        if self.bstpress == 0:
            label.configure(text="游戏开始")
            self.pnum = int(cbb1.get())
            self.bshowflag = self.pnum
            self.bstpress = 1
            self.wplayers, self.wpcuword = self.playgame.startplay(self.pnum)
            for i in range(0, len(self.wplayers)):
                self.tmp.append(self.wplayers[i].name)
        else:
            label.configure(text="请不要重复点开始")

    def bshow(self, label, cbb2):
        # 显示玩家
        if self.bshpress <= self.bshowflag:
            txt = "玩家%d: %s" % (self.bshpress, self.wplayers[self.bshpress - 1].card)
        else:
            txt = "显示完毕"
        label.configure(text=txt)
        cbb2["value"] = self.tmp
        self.bshpress += 1

    def bvote(self, label, cbb2):
        wtxt = None
        # 获取组合框2数据
        self.pnum = len(self.wplayers)
        print(cbb2.get(), ":  type:", type(cbb2.get()))
        # self.wnlayers被删除的玩家集合，self.wplayers上一轮的玩家集合
        if self.bvtpress <= self.pnum:
            self.playgame.pgvote(int(cbb2.get()))
            label.configure(text="玩家%s获得1票 %s  %s" % (cbb2.get(), self.bvtpress, self.pnum))
        elif self.bvtpress == self.pnum + 1:

            self.wnlayers, self.wplayers = self.playgame.judge()
            if len(self.wnlayers) != 0:
                for i in range(0, len(self.wnlayers)):
                    self._txt.append(str(self.wnlayers[i].name))
                    if self.wnlayers[i].card == self.wpcuword[1]:
                        wtxt = "农民胜利"
                        label.configure(text=wtxt)
                        return
                    if self.wnlayers[i].name in self.tmp:
                        self.tmp.remove(self.wnlayers[i].name)
                        self.playgame.players.remove(self.wnlayers[i])
                str1 = " ".join(self._txt)
                label.configure(text="淘汰玩家：" + str1)
                cbb2["value"] = self.tmp

                self._txt = []
            else:
                cards = []
                for i in range(0, len(self.wplayers)):
                    cards.append(self.wplayers[i].card)
                if len(self.wplayers) <= 2 and self.wpcuword[1] in cards:
                    txt = "卧底胜利"
                    label.configure(text=txt)
                    return
        else:
            label.configure(text="请等待进行下一轮投票")
            self.bvtpress = 1
            self.playgame.nplayers = []

        print(cbb2.get())
        self.bvtpress += 1

    def bclose(self):
        exit()

    @property
    def pnum(self):
        return self._pnum

    @pnum.setter
    def pnum(self, value):
        self._pnum = value

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


if __name__ == '__main__':
    pg = playgame.PlayGame()
    w = Win(pg)
    w.opt()
    print(w.pnum)
    print(w.text)
