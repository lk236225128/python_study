# -*- coding: utf-8 -*-
# @Time : 2022/11/22 08:43
# @Author : Kevin
# @File : class_meta.py
# @Software: PyCharm


class People:
    def __init__(self, name):
        self.name = name
        self._age = 10
        self.__sex = "boy"
        print("People __init__ run")


class Student(People):
    def __new__(cls, *args, **kwargs):
        print("Student __new__ run")
        # 重写 __new__ 方法 一定要 return super().__new__(cls)
        return super().__new__(cls)

    # Python魔法方法的一个巨大优势就是可以构建一个拥有Python内置类型行为的对象
    def __init__(self, name):
        super().__init__(name)
        print("Student __init__ run")

    def __del__(self):
        print("Student __del__ run")

    def __str__(self):
        return "this is Student"

    @staticmethod
    def static_method():
        print("Student static_method run")

    @classmethod
    def class_method(cls):
        print("Student class_method run")

    def bark(self):
        print(f"bark run ; my name is {self.name}")


class Tester(People):
    def __init__(self, name):
        super().__init__(name)
        print("Tester __init__")


st = Student("kevin")
st.static_method()
st.class_method()
st.bark()

print(st == 10)
