# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


# 装饰模式感觉和继承有点类似，都是为了增加功能，但是装饰器少了继承的一些限制，使得类与类之间的交互更为灵活
# 通过装饰器符号@Deco将此类传入Deco，使用a_class接受此类，
def Deco(a_class):
    class NewClass:
        def __init__(self, age, color):
            self.wrapped = a_class(age)
            self.color = color

        def display(self):
            print(self.color)
            print(self.wrapped.age)

    return NewClass


@Deco
class Cat:
    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)
        print(dir(Cat))


if __name__ == '__main__':
    c = Cat(12, 'b')
    c.display()
