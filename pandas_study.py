# -*- coding: utf-8 -*-
# @Time : 2022/11/23 10:06
# @Author : Kevin
# @File : pandas.py
# @Software: PyCharm

import pandas as pd

'''
系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维数组
Series的表现形式为：索引在左边，值在右边。如果没有为数据指定索引，于是会自动创建一个0到N-1（N为数据长度）的整数型索引
'''
obj = pd.Series([1, 2, 3, 4])
print(obj)

# 增加Index索引
obj2 = pd.Series([3, 4, 5], index=["a", "b", "c"])
print(obj2)

print(obj2["c"])

# 从list,array,dict to Series
import numpy as np

mylist = ["q", "w", "e"]
myarr = np.arange(3)
mydict = dict(zip(mylist, myarr))

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

print("=" * 20)
print(ser1)
print(ser2)
print(ser3)
print(ser3.head(1))  # 取ser3的第一行

sdata = {'Ohio': 35000, 'Texax': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texax']
obj4 = pd.Series(sdata, index=states)  # 将有索引的赋值，否则为空

print(obj4.values)  # 获取Series值
print(obj4.index)  # 获取Series索引
print(obj4.dtype)  # 获取Series值的类型

print(obj4[0:2])  # 切片获取,当index为数字类型时不可这么操作
print(obj4[-1])

obj4.index = ["demo1", "demo2", "demo3", "demo4"]  # 修改index
print(obj4)

# 修改值类型
obj5 = pd.Series([1, 2, 3], dtype=np.float32, index=["a", "b", "c"])
print(obj5)

print(obj5 + 100)  # 元素全+100

obj6 = pd.Series([1, 2, 3, 4, 5, 6, 7])
obj7 = pd.Series([10, 11, 12, 13, 14, 15, 16])
print(obj6 + obj7)

obj7 = obj7.append(obj6)
print(obj7)

print(obj7.shift(5))  # 按位移动的周期数
print(obj7.rolling(2).sum())  # 按窗口为2进行计算数据之和
print(obj7.rolling(2).mean())  # 按窗口为2进行计算数据平均值
print(obj7.rolling(2).max())  # 按窗口为2进行计算数据最大值
print(obj7.rolling(2).min())  # 按窗口为2进行计算数据最小值

print(obj7.pop(6))  # 移除对应值，并返回

print(obj7)
print(obj7.ewm(span=5, min_periods=4, adjust=True).mean())  # index 加权 (EW) 计算,再求平均值

'''
DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔值等)。
DataFrame既有行索引也有列索引。
DataFrame中的数据是一个或多个二维块存放的(而不是列表、字典或别的一维数据结构)
'''
