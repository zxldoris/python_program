# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


# 观察者模式
# 模式特点:定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，
# 当主题对象状态发生变化时会通知所有观察者

# 程序实例：公司里有两种上班时趁老板不在时偷懒的员工：
# 看NBA和股票行情的，并且事先让老板秘书出现时通知他们继续工作

# 观察者-->抽象观察者
class Observer(object):
    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


class StockObserver(Observer):
    def Update(self):
        print('%s,%s停止看图片' % self.name, self.sub)


class NBAObserver(Observer):
    def Update(self):
        print('%s,%s停止看图片' % self.name, self.sub)


# 规则（主题）-->抽象
class SecretaryBase(object):  # 秘书类
    def __init__(self):
        self.observer = []

    def Attach(self, new_observer):
        pass

    def Notify(self):
        pass

    def deleteobserver(self, new_observer):
        pass


class Secretary(SecretaryBase):
    def Attach(self, new_observer):
        self.observer.append(new_observer)

    def Notify(self):
        for p in self.observer:
            pass


if __name__ == "__main__":
    topic = Secretary()
    o1 = StockObserver('Tom', p)
    o2 = NBAObserver('Jack', p)
    o1.A
