# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


# װ��ģʽ�о��ͼ̳��е����ƣ�����Ϊ�����ӹ��ܣ�����װ�������˼̳е�һЩ���ƣ�ʹ��������֮��Ľ�����Ϊ���
# ͨ��װ��������@Deco�����ഫ��Deco��ʹ��a_class���ܴ��࣬
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
