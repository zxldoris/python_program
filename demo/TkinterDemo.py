#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'zxl'

# import tkinter
from tkinter import *

# top = tkinter.Tk()
# top.mainloop()


# root = tkinter.Tk()
# li = ['C', 'Java', 'Python', 'C#']
# li2 = ['HTML', 'CSS', 'BootStrap']
# litka = tkinter.Listbox(root)
# litkb = tkinter.Listbox(root)
# for item in li:
#     litka.insert(0, item)
# for item in li2:
#     litkb.insert(0, item)
# litka.pack()
# litkb.pack()
# root.mainloop()

canvas_root = Tk()
canvas_width = 80
canvas_height = 40
c = Canvas(canvas_root, width=canvas_width, height=canvas_height)
c.pack()
y = int(canvas_height / 2)
c.create_line(0, y, canvas_width, y, fill='#476042')
c.mainloop()
