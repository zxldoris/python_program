import tkinter
from tkinter.ttk import *


def my_callback(label):
    label.configure(text = "Hello")


root = tkinter.Tk()
root.title("谁是卧底")
root.geometry('580x300+0+0')

# 创建Label
label = Label(root)
label.pack(side="top")

Button(root,text="Click",command=lambda:my_callback(label)).pack()
root.mainloop()
