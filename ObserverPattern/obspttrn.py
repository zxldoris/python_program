#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 主题分成了人员管理数据管理两个类
class Publisher:
    def __init__(self):
        self.observers = set()

    def add(self, observer):
        if observer in self.observers:
            print('add failed')
        else:
            self.observers.add(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
            # print('remove %s' % observer)
        except ValueError:
            print('Failed to remove:%s' % observer)

    def notify(self):
        [observer.update(self) for observer in self.observers]

    def printobs(self):
        for observer in self.observers:
            print(observer)


class DefaultPublisher(Publisher):
    def __init__(self, subscriber):
        Publisher.__init__(self)
        self._subscriber = subscriber
        self._newspaper = None
        self._magazine = None

    def __str__(self):
        return '%s subscribe %s' % (self._subscriber, self._newspaper)

    @property
    def newspaper(self):
        return self._newspaper

    @newspaper.setter
    def newspaper(self, news):
        self._newspaper = news
        self.notify()

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, mag):
        self._magazine = mag
        self.notify()


class Observer:
    def update(self, publisher):
        print('newspaper subscriber,%s'.format(publisher))


def main():
    p = Publisher()
    p.add('subscriber_a')
    dp = DefaultPublisher('subscriber_a')
    dp.newspaper = 'news'
    print(dp)
    p.printobs()

    p.remove('subscriber_a')
    p.printobs()

if __name__ == '__main__':
    main()
