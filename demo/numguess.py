# coding=gbk
# coding=utf-8
# -*- coding: UTF-8 -*-
"""
ʹ��˵����
1.�����ֹ����У�����ʱ����quit��exit�˳���
2.��Χ����֧������
3.���볬��2��������ֻʶ��ǰ��������
"""
from random import randrange


def char_judge():
    while True:
        try:
            var = input()
        except Exception as e:
            with open('num_guess.txt', 'a+', encoding='utf-8') as f:
                f.write(e + '\n')
            print("����ȷ���룺")
            break
        else:
            if var in ['quit', 'exit']:
                exit(0)
            else:
                break
    return var


num_range = ''
guess_num = ''
print("�������������Χ�������������֣���ǰ��λ��Ч:")
num_range = char_judge()
# ����������ַ�
num_list = num_range.split(' ')
start = min(int(num_list[0]), int(num_list[1]))
end = max(int(num_list[0]), int(num_list[1]))
# ���������
random_num = randrange(start, end)
# ��������Ϸ��ʼ�����5��
for i in range(0, 5):
    print("��������²�����֣�")
    guess_num = int(char_judge())
    if guess_num == random_num:
        print('��ϲ�㣬�¶��ˣ�')
        # ���²�������׷�ӷ�ʽд���ĵ�
        with open('num_guess.txt', 'a+', encoding='utf-8') as f:
            f.write(str(guess_num) + '\n')
    # �����趨��Χ
    elif guess_num > end or guess_num < start:
        print('��������ȷ�ķ�Χ��')
    # û�в���
    else:
        with open('num_guess.txt', 'a+', encoding='utf-8') as f:
            f.write(str(guess_num) + '\n')
        # �����·�Χ
        if guess_num > random_num:
            end = guess_num
        else:
            start = guess_num
        print('��Ǹ���²�����µĲ²ⷶΧ��[%d ~ %d]��ʣ��²������%d' % (start, end, 4 - i))
