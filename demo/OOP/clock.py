# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'

import tkinter
import math
import time
import threading

"""""""""""""""""""""""""""
类名称：TimePointer
参数定义：
    root_canvas：
    point_zero：
    LINE_LONG：
    sub:下标
"""""""""""""""""""""""""""


def create_pointer():
    # 创建时针 分针 秒针
    pointer_hour = TimePointer(root_canvas, point_zero, SECOND_LINE_LONG, now_second, color='red')
    pointer_hour.draw()
    pointer_minute = TimePointer(root_canvas, point_zero, MINUTE_LINE_LONG, now_minute, color='green')
    pointer_minute.draw()
    pointer_hour = TimePointer(root_canvas, point_zero, HOUR_LINE_LONG,
                               now_hour * 5 + int(now_minute / 12), color='blue')
    pointer_hour.draw()

    return pointer_hour, pointer_minute, pointer_hour


class TimePointer(object):
    def __init__(self, root_canvas, point_zero, LINE_LONG, sub, color):
        self.root_canvas = root_canvas
        self.point_zero = point_zero
        self.LINE_LONG = LINE_LONG
        self.sub = sub
        self.color = color
        self.pid = None

    def draw(self):
        x, y = self.calcu()
        self.delete()
        pid = self.root_canvas.create_line(self.point_zero, x[self.sub], y[self.sub], fill=self.color)
        self.sub += 1
        global timer
        timer = threading.Timer(1,create_pointer())
        timer.start()

    def delete(self):
        if self.pid:
            self.root_canvas.delete(self.pid)

    # 计算出所有指针的坐标
    def calcu(self):
        x = []
        y = []
        for i in range(0, 60):
            x.append(self.point_zero[0] + self.LINE_LONG * math.sin(math.pi * i / 30))
            y.append(self.point_zero[1] - self.LINE_LONG * math.cos(math.pi * i / 30))
        return x, y


class TimePlate(object):
    def __init__(self, root_canvas, point_zero):
        self.root_canvas = root_canvas
        self.point_zero = point_zero
        self.pid = None

    def draw(self, root_canvas):
        # 刻度线数组
        x1, y1 = self.calcu(self.point_zero, SECOND_LINE_LONG)
        x2, y2 = self.calcu(self.point_zero, (SECOND_LINE_LONG - 10))
        # text 数组
        x3, y3 = self.calcu(self.point_zero, (SECOND_LINE_LONG - 20))
        clock_num = ['12', '3', '6', '9']

        for i in range(0, 60):
            width = 1
            if i % 5 == 0:
                width = 3
                if i % 15 == 0:
                    width = 5
                    root_canvas.create_text((x3[i], y3[i]), text=clock_num[int(i / 15)], font=15)
            root_canvas.create_line(x1[i], y1[i], x2[i], y2[i], width=width)

    def calcu(self, point_zero, line_long):
        x = []
        y = []
        for i in range(0, 60):
            x.append(point_zero[0] + line_long * math.sin(math.pi * i / 30))
            y.append(point_zero[1] - line_long * math.cos(math.pi * i / 30))
        return x, y


if __name__ == '__main__':
    # 参数定义
    width = 400
    height = 400
    # 时针 分针 秒针 长度
    SECOND_LINE_LONG = width / 2
    MINUTE_LINE_LONG = width / 3
    HOUR_LINE_LONG = width / 6
    point_zero = [width / 2, height / 2]  # 原点
    pointers_hour = [point_zero, width / 2, 0]
    # 获取当前时间
    now_hour = int(time.strftime('%I'))
    now_minute = int(time.strftime('%M'))
    now_second = int(time.strftime('%S'))
    print(now_hour, ':', now_minute, ':', now_second)

    # the main window of an application
    window = tkinter.Tk()
    root_canvas = tkinter.Canvas(window, width=width, height=height)
    root_canvas.pack()

    timer = threading.Timer(1, create_pointer)
    timer.start()
    # 创建基本表盘
    time_plate = TimePlate(root_canvas, point_zero)
    time_plate.draw(root_canvas)
    root_canvas.mainloop()
