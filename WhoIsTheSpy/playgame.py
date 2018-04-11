#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
import random
import player

REF = [["镜子", "玻璃"], ["玉米", "小米"], ["反射", "折射"],
       ["穿衣", "试衣"], ["梦境", "幻想"]]


class PlayGame(object):
    def __init__(self):
        self.players = []  # 上一轮玩家集合
        self.nplayers = []  # 每轮淘汰玩家
        self.pcuword = []  # 随机选出的一对牌
        self.underflag = 0  # 卧底牌标志
        self.pvotes = []

    def startplay(self, pnum):
        # 从REF中选出一组牌
        self.pcuword = random.choice(REF)

        # 如果已经选择玩家数，创建pnum个玩家 并发牌
        for i in range(1, pnum + 1):
            p = player.Player()
            p.name = i
            if self.underflag == 1:
                p.card = self.pcuword[0]
            else:
                p.card = random.choice(self.pcuword)
                if p.card == self.pcuword[1]:
                    self.underflag = 1
            self.players.append(p)
        return self.players, self.pcuword

    def pgvote(self, name):
        for i in range(0, len(self.players)):
            n = self.players[i].name
            if n == int(name):
                self.players[i].vote = 1

    # 判定谁出局
    def judge(self):
        for i in range(0, len(self.players)):
            self.pvotes.append(self.players[i].vote)
        maxvt = max(self.pvotes)
        # 将被删除的对象保存在nplayer中
        for i in range(0, len(self.players)):
            if maxvt == self.players[i].vote:
                self.nplayers.append(self.players[i])
        return self.nplayers, self.players  # 淘汰玩家 返回更新的玩家列表


if __name__ == "__main__":
    pg = PlayGame()
    pg.startplay(5)
    pg.pgvote(3)
    pg.pgvote(3)
    pg.pgvote(2)
    pg.pgvote(2)
    pg.pgvote(1)
    for i in pg.players:
        print(i.vote)
    pg.judge()
