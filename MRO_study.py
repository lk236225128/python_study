# -*- coding: utf-8 -*-
# @Time : 2022/11/22 18:14
# @Author : Kevin
# @File : MRO_study.py
# @Software: PyCharm

'''
代码示例继承关系如图

Grafathher1   Grafathher2
    |               |
  Fahter1        Fahter2
    |               |
  Son1             Son2
    |_______Me______|

class Me(Son2, Son1): MRO结果
(<class '__main__.Me'>, <class '__main__.Son2'>, <class '__main__.Fahter2'>, <class '__main__.Grafathher2'>, <class '__main__.Son1'>, <class '__main__.Father1'>, <class '__main__.Grafathher1'>, <class 'object'>)

class Me(Son1, Son2): MRO结果
(<class '__main__.Me'>, <class '__main__.Son1'>, <class '__main__.Father1'>, <class '__main__.Grafathher1'>, <class '__main__.Son2'>, <class '__main__.Fahter2'>, <class '__main__.Grafathher2'>, <class 'object'>)
'''

class Grafathher1():
    pass


class Father1(Grafathher1):
    pass


class Son1(Father1):
    def show(self):
        print("i am Son1")


class Grafathher2():
    def show(self):
        print("i am Grafathher2")


class Fahter2(Grafathher2):
    pass


class Son2(Fahter2):
    pass


class Me(Son1, Son2):
    pass


m = Me()
m.show()
# MRO : 从左向右,深度优先

# 查看MRO顺序
print(Me.__mro__)
# 或
import inspect
print(inspect.getmro(Me))

