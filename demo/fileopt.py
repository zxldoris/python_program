# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
����������룺f = open('a.txt','w',encoding='utf-8')

"""
# �����û������� �����û������������׷�ӵķ�ʽд�뵽�ļ���ֱ���û�����exit��quit���˳������˳���ʱ����ʾ�ļ������м�¼����
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
