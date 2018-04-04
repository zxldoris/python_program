#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
import tkinter
import random


class CharsGenerate(object):
    def __init__(self):
        self.chars = list()  # 保存在显示屏上的字符
        self.source_list_chg = list()  # 状态保存
        self.source_list = list()

    def __source_list_gen(self):
        for i in range(97, 122):
            self.source_list_chg.append(chr(i))
            self.source_list = self.source_list_chg

    # 生成一批不相同字符 两次生成允许相同
    def generate_chars(self):
        char = random.choice(self.source_list)
        self.chars.append(char)
        self.source_list_chg.remove(char)
        self.source_list_chg = self.source_list
        return char

    # 删除已经录入的字符
    def remove(self, char):
        self.chars.remove(char)


class Window(CharsGenerate):
    def __init__(self, canvas):
        CharsGenerate.__init__(self)
        self.canvas = canvas
        self.cnt = 0  # 正确录入计数
        self.total = 0  # 录入总数计数

    def judge(self, text):
        # 如果输入正确 字符消失 速度不变
        if text in self.chars:
            self.move('up', 'red', 1)
            self.cnt += 1
        if self.cnt / self.total >= 0.8:
            self.generate_chars()
            self.move('down', 'black', 2)

    def move(self, canvas, direction, color, speed):
        pass

    def delete_move(self, id):
        self.canvas.delete(id)



def key(event):
    e.pack()
    print("pressed", repr(event.char))
    e.insert(1, repr(event.char))

    # return repr(event.char)  # 返回键盘输入数据


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)


root = tkinter.Tk()
frame = tkinter.Frame(root, width=300, height=20)
frame.pack(side='bottom')

root_canvas = tkinter.Canvas(root, width=300, height=400, bg='white')
root_canvas.pack(side='top')
# 创建文本输入框 并放到frame上
e = tkinter.Entry(frame)
frame.bind("<Button-1>", callback)
frame.bind("<Key>", key)


# 创建计分text，放到window上，并指定位置
text = '已产生字符：%s\n正确字符：%s\n'
t = tkinter.Canvas.create_text(root_canvas, 100, 100, text=text, state=tkinter.DISABLED)
root.mainloop()
