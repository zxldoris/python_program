# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


# �۲���ģʽ
# ģʽ�ص�:������һ��һ�Զ�Ĺ�ϵ���ö���۲����ͬʱ����һ���������
# ���������״̬�����仯ʱ��֪ͨ���й۲���

# ����ʵ������˾���������ϰ�ʱ���ϰ岻��ʱ͵����Ա����
# ��NBA�͹�Ʊ����ģ������������ϰ��������ʱ֪ͨ���Ǽ�������

# �۲���-->����۲���
class Observer(object):
    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


class StockObserver(Observer):
    def Update(self):
        print('%s,%sֹͣ��ͼƬ' % self.name, self.sub)


class NBAObserver(Observer):
    def Update(self):
        print('%s,%sֹͣ��ͼƬ' % self.name, self.sub)


# �������⣩-->����
class SecretaryBase(object):  # ������
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
