# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'


# class Moveable:
#     def move(self):
#         print('moving')
#
#
# class MoveOnFoot(Moveable):
#     def move(self):
#         print('move on feet')
#
#
# class MoveOnWheel(Moveable):
#     def move(self):
#         print('Move on wheel')
#
#
# class MoveObj:
#     def set_move(self, moveable):
#         self.moveable = moveable()
#
#     def move(self):
#         self.moveable.move()
#
#
# if __name__ == '__main__':
#     m = MoveObj()
#     m.set_move(Moveable)
#     m.move()
#     m.set_move(MoveOnFoot)
#     m.move()
#     m.set_move(MoveOnWheel)
#     m.move()

def movea():
    print('moving a..')
def moveb():
    print('moving b..')

class MoveObj:
    def set_move(self, move):
        self.moveable = move

    def move(self):
        self.moveable


if __name__ == '__main__':
    m = MoveObj()
    m.set_move(movea())
    m.move()
    m.set_move(moveb())
    m.move()
