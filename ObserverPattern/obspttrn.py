#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


class Publisher(object):
    def __init__(self):
        self.observers = set()

    def add(self, observer):
        self.observers.add(observer)

    def remove(self, observer):
        self.observers.remove(observer) if observer in self.observers \
            else print('不存在此订阅者')

    def notify(self):
        [observer.update(self) for observer in self.observers]


class PublisherData(Publisher):
    def __init__(self, observer):
        Publisher.__init__(self)
        self.observer = observer
        self._news = None
        self._mag = None

    def __str__(self):
        return '%s has subscribe newspaper:%s, magazine:%s' % (self.observer, self._news, self._mag)

    @property
    def newspaper(self):
        return self._news

    @newspaper.setter
    def newspaper(self, value):
        self._news = value
        self.notify()

    @newspaper.deleter
    def newspaper(self):
        self._news = None

    @property
    def magz(self):
        return self._mag

    @magz.setter
    def magz(self, value):
        self._mag = value
        self.notify()

    @magz.deleter
    def magz(self):
        self._mag = None


class Observer(object):
    def update(self, publisher):
        print(publisher)


def main():
    p1 = Publisher()
    p1.add('tom')
    pd = PublisherData('tom')
    pd.newspaper = 'news_a'
    pd.magz = 'mag_a'
    print(pd)

if __name__ == '__main__':
    main()
