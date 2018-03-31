"""
1、判断是不是因子,若不是进入下一次循环，是调第二步
2、是因子，判断在因子的list中是否存在，若存在continue，不存在就添加
3、判断传入参数是不是为list中元素之和
"""

# def complete_num(num):
#     factor_list = []
#     for i in range(1, num):
#         if num % i == 0:
#             if i in factor_list:
#                 continue
#             else:
#                 factor_list.append(i)
#         else:
#             continue
#     num2 = 0
#     for j in factor_list:
#         num2 += j
#     if num == num2:
#         return True
#     else:
#         return False

# print('is complete number?', complete_num(5))
"""
完美数优化代码
"""

while True:
    num = int(input("input:"))
    list_num = [1]
    for i in range(2, num):
        if i in list_num:
            continue
        if num % i == 0:
            list_num.append(i)
            list_num.append(int(num / i))
    if num == sum(list_num) and (num not in list_num):  # 排除1
        print('yes')
    else:
        print('no')
