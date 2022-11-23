# -*- coding: utf-8 -*-
# @Time : 2022/11/23 08:27
# @Author : Kevin
# @File : Polymorphism.py
# @Software: PyCharm

# Polymorphism 多态

class People:
    def speak(self):
        pass


class Chinese(People):
    def speak(self):
        print("你好,我是中国人")


class American(People):
    def speak(self):
        print("hi , i am American")


p1 = Chinese()
p2 = American()

p1.speak()
p2.speak()

'''
duck typeing

一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
例: 一个对象，只要有 speak 方法，那么它就是一个 do_speak 方法所需要的 people 对象
'''


def do_speak(people):
    people.speak()


do_speak(p1)
do_speak(p2)

'''
property属性
'''


class Student:
    pass


s = Student()
s.name = "kevin"
s.age = 28
print(s.name, s.age)

'''
age如果是-28,则在业务层是不合法的,需引入property属性进行合法性校验
PS:一定是 @property 在前面，而 @xx.setter 在后

ValueError: age must be in [0,150]
'''


class NewStudent:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 < value <= 150:
            self._age = value
        else:
            raise ValueError("age must be in [0,150]")


ns = NewStudent()
ns.age = -28
