# -*- coding: utf-8 -*-
# @Time : 2022/11/23 08:44
# @Author : Kevin
# @File : Mixin.py
# @Software: PyCharm

'''
Mixin模式,主要作为增强功能，添加到子类中

规范
● 责任明确：必须表示某一种功能，而不是某个物品；
● 功能单一：若有多个功能，那就写多个Mixin类；
● 绝对独立：不能依赖于子类的实现；子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能

例:交通工具中，并非所有类型都能飞，car就不能 . 但飞机Airplane可以 , 可以把飞行能力Mixin独立出来 .
它和基类Vehicle没有任何继承关系 , 但可以扩展类的功能 , 有点像面向行为编程
'''


class Vehicle:
    # 交通工具
    pass


class PlaneMixin:
    # 飞行能力
    def fly(self):
        print("i can fly")


class Airplane(Vehicle, PlaneMixin):
    # 飞机类
    pass


class car(Vehicle):
    # 汽车类
    pass


ap = Airplane()
ap.fly()
