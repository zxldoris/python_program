# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-


# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# if __name__ == '__main__':
#     s1 = Singleton()
#     s2 = Singleton()
#     print(id(s1))
#     print(id(s2))

class Ab:
    a = 3


class Ac:
    a = 0


class MyFactory:
    def get_instance(self, ins):
        return ins()


if __name__ == '__main__':
    mf = MyFactory()
    print(type(mf.get_instance(Ab)))
    print(type(mf.get_instance(Ac)))
