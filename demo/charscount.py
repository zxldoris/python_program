"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：isalpha方法判断是否是字母，isspace方法判断是否是空格，isdigit方法判断是否是数字
"""

# str 系统自带
string = input()
charcnt = 0
spacecnt = 0
numcnt = 0
othercnt = 0
for c in string:
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        charcnt += 1
    elif ord(c) == 32:
        spacecnt += 1
    elif ord(c) >= 48 and ord(c) <= 57:
        numcnt += 1
    else:
        othercnt += 1
print('charcnt:%d, spacecnt:%d, numcnt:%d, othercnt:%d' % (charcnt, spacecnt,
                                                           numcnt, othercnt))

charcnt1 = 0
spacecnt1 = 0
numcnt1 = 0
othercnt1 = 0
print(string)
print(list(string))
for c in string:
    if c.isalpha():
        charcnt1 += 1
    elif c.isspace():
        spacecnt1 += 1
    elif c.isdigit():
        numcnt1 += 1
    else:
        othercnt1 += 1
print('charcnt:%d, spacecnt:%d, numcnt:%d, othercnt:%d' % (charcnt1, spacecnt1,
                                                           numcnt1, othercnt1))
