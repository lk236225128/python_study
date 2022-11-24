# -*- coding: utf-8 -*-
# @Time : 2022/11/23 16:35
# @Author : Kevin
# @File : generator_map_reduce_filter.py
# @Software: PyCharm
'''
map
两个参数，一个是函数，一个是Iterable
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''


def fuc(x):
    return x * x


result = map(fuc, [1, 2, 3, 4, 5])
print(list(result))
print(list(map(str, [1, 2, 3, 4, 5])))  # 把list所有数字转为字符串

'''
reduce
把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算
'''
from functools import reduce


def func(x, y):
    return x + y


reduce(func, [1, 2, 3, 4, 5, 6, 7])

'''
结合lambda
'''

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7])

'''
filter
接收一个函数和一个序列,把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''


def odd(x):
    return x % 2 == 1


list(filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 删偶保奇

'''
迭代器
可利用 for 循环的对象，都叫可迭代对象
'''
# 通过isinstance可以判断是否属于Python 内置的 collections.abc的Iterable
from collections.abc import Iterable

isinstance([1, 2, 3, 4], Iterable)

'''
可迭代协议
1. 对象内部实现了 __iter__() 方法 ，并返回一个迭代器实例，那么该对象就是可迭代对象
2. Python 解释器 __getitem__() 方法获取元素，如果可行，那么该对象也是一个可迭代对象
'''


class Array:
    my_list = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(self.my_list)


me = Array()
print(isinstance(me, Iterable))
for i in me:
    print(i)


class Array2:
    my_list = [1, 2, 3, 4, 5]

    def __getitem__(self, item):
        return self.my_list[item]


me2 = Array2()
print(isinstance(me2, Iterable))
# False , 因为 isinstance 这种方法就是检查对象是否有 __iter__ 方法,所以用 isinstance(my_list, Iterable) 去判断是否可迭代是不准确
for i in me2:
    print(i)

'''
什么是迭代器
迭代对象使用 iter 函数返回一个迭代器对象，
对于迭代器对象，我们可以使用 next 函数，去获取元素，每执行一次，获取一次，
等到全部获取完毕，会抛出 StopIteration 提示无元素可取
'''
alist = [1, 2, 3, 4, 5, 6, 6]
gen = iter(alist)
next(gen)
next(gen)
next(gen)
next(gen)

'''
迭代器协议
对比可迭代对象，迭代器的内部只是多了一个函数而已 – __next__()
'''
