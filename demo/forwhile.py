# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
while 条件表达式：
    满足执行
else:
    退出时执行==》finally


for var in str：
    满足执行
else:
    顺利循环完执行
"""


# str = 'fkadhfkladkff'
# for (i,v) in enumerate(str):
#     print(i,v)
# while求和
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

# for 求和
sum2 = 0
for i in range(0, 100):
    if i % 2 != 0:
        sum2 += i
print(sum2)
