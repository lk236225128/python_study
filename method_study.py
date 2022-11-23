# -*- coding: utf-8 -*-
# @Time : 2022/11/23 08:54
# @Author : Kevin
# @File : method_study.py
# @Software: PyCharm

'''
方法

实例方法,静态方法,类方法
'''


class Student:
    def __init__(self, name):
        self.name = name
        self._age = 10
        print("Student __init__ run")

    @staticmethod
    def static_method():
        print("静态方法 static_method run")

    @classmethod
    def class_method(cls):
        print("类方法 class_method run")

    def bark(self):
        print(f"实例方法 bark run ; my name is {self.name}")

    def speak(self, value):
        print(f"i speak {value}")

    def change(self, a):
        # 参数传递区分:不可变类型,可变类型
        print(f"修改前a的id值:{id(a)}:")
        a = 10
        print(f"修改后a的id值:{id(a)}")

    def kb_change(self, num: list):
        print(f"修改前num值:{num}:")
        num.append([1, 2, 3])
        print(f"修改前num值:{num}:")

        # 可变类型


st = Student("kevin")
st.static_method()
st.class_method()
st.bark()
st.speak("one")

word = "b"
st.change(word)
print(id(word))  # 传不可变类型时,函数内部不会改变原变量

nums = [4, 5, 6]
st.kb_change(nums)  # 可变类型 传的是引用,方法内是会改变原变量值
print(nums)

'''
参数类型:必需参数,关键字参数,默认参数,不定长参数
'''
