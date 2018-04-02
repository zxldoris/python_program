# coding=utf-8
# -*- coding: UTF-8 -*-
__author__ = 'zxl'

"""
使用说明：
    -1退出
    输入无效数字或字符会提示重新输入
    本程序中只有一个产生球的类，其他相对复杂过程使用方法
"""
import random
import time
import os


class Ball(object):
    def __init__(self, red_base_num_list, blue_base_num_list):
        self.base_num_list = red_base_num_list
        self.blue_base_num_list = blue_base_num_list

    def create_ball(self, base_num_list):
        selected_ball = random.choice(base_num_list)
        base_num_list.remove(selected_ball)  # 将选中的球号从列表中移除
        return selected_ball


def generate_prize_num():
    # 生成中奖号码(红球6个，蓝球1个):红球list[1,33] 篮球list[1,16]
    red_ball_base_num_list = []
    for i in range(1, 34):
        red_ball_base_num_list.append(i)
    blue_ball_base_num_list = []
    for i in range(1, 17):
        blue_ball_base_num_list.append(i)
    ball = Ball(red_ball_base_num_list, blue_ball_base_num_list)
    red_ball_answer_list = []
    for i in range(0, 6):
        red_ball = ball.create_ball(red_ball_base_num_list)
        red_ball_answer_list.append(red_ball)

    blue_ball_answer = ball.create_ball(blue_ball_base_num_list)
    return red_ball_answer_list, blue_ball_answer


def prize_level(red_a, blue_a, red_g, blue_g):
    red = [i for i in red_a if i in red_g]  # 求交集
    red_len = len(red)
    blue_len = 1 if blue_a == blue_g else 0
    if red_len in range(0, 3) and blue_len == 1:
        prize = 6
    elif (red_len == 3 and blue_len == 1) or (red_len == 4 and blue_len == 0):
        prize = 5
    elif (red_len == 4 and blue_len == 1) or (red_len == 5 and blue_len == 0):
        prize = 4
    elif red_len == 5 and blue_len == 1:
        prize = 3
    elif red_len == 6 and blue_len == 0:
        prize = 2
    elif red_len == 6 and blue_len == 1:
        prize = 1
    else:
        prize = 0
    return prize


# 输入判定函数
def input_judge():
    red_guess_nums = []
    for i in range(0, 6):
        while True:
            try:
                guess_r = int(input('请输入红色投注号码：'))
                if guess_r in red_guess_nums:
                    print('请不要重复输入！')
                    continue
                if guess_r <= 0:
                    if guess_r == -1:
                        os._exit(0)
                    else:
                        print('请不要输入无效负数！')
                        continue
            except:
                print('请正确输入：')
            else:
                red_guess_nums.append(guess_r)
                break
    while True:
        try:
            blue_guess_num = int(input('请输入蓝色投注号码：'))
            if blue_guess_num <= 0:
                if guess_r == -1:
                    os._exit(0)
                else:
                    print('请不要输入无效负数！')
                    continue
        except:
            print('请正确输入：')
        else:
            break
    return red_guess_nums, blue_guess_num


if __name__ == '__main__':
    # 生成中奖号码
    red_ball_answer_list = []
    red_ball_answer_list, blue_ball_answer = generate_prize_num()
    print(red_ball_answer_list, blue_ball_answer)

    # 输入投注号码
    red_guess_nums, blue_guess_num = input_judge()

    # 判定中何等奖
    level = prize_level(red_ball_answer_list,
                        blue_ball_answer, red_guess_nums, blue_guess_num)
    if level == 0:
        print('sorry,you do not guess it!')
    else:
        print('Congratulations! you get %drd level prize' % level)

    # 将开奖信息保存
    with open('twocolorballs_info.txt', 'a+') as f:
        f.write('red ball:%-30s\t blue ball:%-2s \t\t%-20s\n' %
                (str(red_ball_answer_list), str(blue_ball_answer), time.strftime('%Y.%m.%d %H:%M:%S')))
