# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
使用说明：
1.猜数字过程中，可随时输入quit或exit退出。
2.范围输入支持乱序
3.输入超过2个参数，只识别前两个参数
"""
from random import randrange


def char_judge():
    while True:
        try:
            var = input()
        except Exception as e:
            with open('num_guess.txt', 'a+', encoding='utf-8') as f:
                f.write(e + '\n')
            print("请正确输入：")
            break
        else:
            if var in ['quit', 'exit']:
                exit(0)
            else:
                break
    return var


num_range = ''
guess_num = ''
print("请输入随机数范围，如输入多个数字，仅前两位有效:")
num_range = char_judge()
# 处理输入的字符
num_list = num_range.split(' ')
start = min(int(num_list[0]), int(num_list[1]))
end = max(int(num_list[0]), int(num_list[1]))
# 生成随机数
random_num = randrange(start, end)
# 猜数字游戏开始，最多5次
for i in range(0, 5):
    print("请输入你猜测的数字：")
    guess_num = int(char_judge())
    if guess_num == random_num:
        print('恭喜你，猜对了！')
        # 将猜测数字以追加方式写入文档
        with open('num_guess.txt', 'a+', encoding='utf-8') as f:
            f.write(str(guess_num) + '\n')
    # 超出设定范围
    elif guess_num > end or guess_num < start:
        print('请输入正确的范围：')
    # 没有猜中
    else:
        with open('num_guess.txt', 'a+', encoding='utf-8') as f:
            f.write(str(guess_num) + '\n')
        # 给定新范围
        if guess_num > random_num:
            end = guess_num
        else:
            start = guess_num
        print('抱歉，猜测错误！新的猜测范围：[%d ~ %d]，剩余猜测次数：%d' % (start, end, 4 - i))
