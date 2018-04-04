#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog
import tkinter
import random


class CharsGenerate(object):
    def __init__(self):
        self.chars_buttom = list()  # 未录入的字符
        self.chars = list()  # 保存在显示屏上的字符和x坐标
        self.source_list_chg = [chr(i) for i in range(97, 123)]  # 状态保存
        self.source_list = self.source_list_chg

    # 生成一批不相同字符 两次生成允许相同
    def generate_chars(self, num=5):
        for i in range(0, num):
            char = random.choice(self.source_list_chg)
            self.chars.append(char)
            self.source_list_chg.remove(char)
        self.source_list_chg = self.source_list
        return self.chars

    # - 删除已经录入的字符
    def remove(self, char):
        self.chars.pop(char)

class Movement(object):
    def __init__(self, canvas, gen):  # gen_chars是CharsGenerate对象
        self.canvas = canvas
        self.gen = gen
        self.cnt = 0  # 正确录入计数
        self.total = 0  # 录入总数计数
        self._in_txt = None

    @property
    def in_txt(self):
        return self._in_txt

    @in_txt.setter
    def in_txt(self, value):
        self._in_txt = value

    # 字符移动函数
    def move(self):
        num = len(self.gen.chars)
        x = self.calcu_list_x(num)
        y = [j for j in range(0, 400)]
        for i in x:
            if self.in_txt in self.gen.chars:
                self.gen.remove(self.in_txt)
                continue
            else:
                for j in y:
                    for txt in self.gen.chars:
                        pid = tkinter.Canvas.create_text(self.canvas, i, j, text=txt)
                        self.delete_move(pid)

    # - 移动删除
    def delete_move(self, pid):
        self.canvas.delete(pid)

    # - 产生x坐标
    def calcu_list_x(self, num):
        x = []
        for i in range(0, num):
            x.append(random.randint(0, 300))
        return x


class Opt(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.frame = tkinter.Frame(self.root, width=300, height=20)
        self.frame.pack(side='bottom')
        self.root_canvas = tkinter.Canvas(self.root, width=300, height=400, bg='white')
        self.root_canvas.pack(side='top')
        # 创建文本输入框 并放到frame上
        self.e = tkinter.Entry(self.frame)

        cg = CharsGenerate()
        cg.generate_chars()
        self.mv = Movement(self.root_canvas, cg)
        self.mv.move()

    def main_opt(self):
        self.frame.bind("<Key>", self.__key)
        self.frame.bind("<Button-1>", self.__callback)
        self.root.mainloop()

    def __key(self, event):
        self.e.pack()
        print("pressed", repr(event.char))
        self.e.insert(1, repr(event.char))
        self.mv._in_txt = repr(event.char)

    def __callback(self, event):
        self.frame.focus_set()
        print("clicked at", event.x, event.y)


def main():
    opt = Opt()
    opt.main_opt()


if __name__ == '__main__':
    main()
    # 创建计分text，放到window上，并指定位置
    # text_str = '已产生字符：%s\n正确字符：%s\n'
    # t = tkinter.Canvas.create_text(root_canvas, 100, 100, text=text_str, state=tkinter.DISABLED)
