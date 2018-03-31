# coding=utf-8
# -*- coding: UTF-8 -*-
class SchoolMember:
    num = 0
    def __init__(self, name):
        self.name = name
        SchoolMember.num += 1
        print('现在有%d人' % SchoolMember.num)
class Teacher(SchoolMember):
    def __init__(self, name, salary):
        SchoolMember.__init__(self, name)
        self.salary = salary
        print('老师名字：%s工资是：%d' % (self.name, self.salary))

class Student(SchoolMember):
    def __init__(self, name, score):
        SchoolMember.__init__(self, name)
        self.score = score
print(__name__)
if __name__ == "__main__":
    tea1 = Teacher('wang', 10000)
    tea2 = Teacher('li', 20000)
    print(__name__)
