# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
while �������ʽ��
    ����ִ��
else:
    �˳�ʱִ��==��finally


for var in str��
    ����ִ��
else:
    ˳��ѭ����ִ��
"""


# str = 'fkadhfkladkff'
# for (i,v) in enumerate(str):
#     print(i,v)
# while���
def numsum(start, end):
    i = start
    sum1 = 0
    while i <= end:
        if i % 2 != 0:
            sum1 += i
            i += 1
        else:
            i += 1
    return sum1


print(numsum(3, 100))

# for ���
sum2 = 0
for i in range(0, 100):
    if i % 2 != 0:
        sum2 += i
print(sum2)
