# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
解决中文乱码：f = open('a.txt','w',encoding='utf-8')

"""
# 接受用户的输入 并将用户输入的内容以追加的方式写入到文件，直到用户输入exit或quit则退出程序，退出的时候显示文件中所有记录内容
# f = open('fileopt.txt', 'a', encoding='utf-8')
# while 1:
#     string = input()
#     if ('quit' or 'exit') in string:
#         f.write(string)
#         f.close()
#         f2 = open('fileopt.txt','r')
#         print(f2.readline())
#         f.close()
#         exit(0)

while True:
    string = input()
    if ('quit' or 'exit') not in string:
        with open('fileopt.txt', 'a+', encoding='utf-8') as f:
            f.write(string + '\n')
    else:
        with open('fileopt.txt', 'a+', encoding='utf-8') as f:
            f.write(string[:len(string) - 4])
        with open('fileopt.txt', 'r', encoding='utf-8') as f2:
            for v in f2:
                print(v, end='')
            exit()
