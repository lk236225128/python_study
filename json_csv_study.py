# -*- coding: utf-8 -*-
# @Time : 2022/11/23 10:06
# @Author : Kevin
# @File : json_csv.py
# @Software: PyCharm

import json

'''
json.dumps	对数据进行编码,将python中的字典 转换为 字符串
json.loads	对数据进行解码,将 字符串 转换为 python中的字典
json.dump	将dict数据写入json文件中
json.load	打开json文件，并把字符串转换为python的dict数据

数据转换对照
json	python
object	dict
array	list
string	str
number (int)	int
number (real)	float
true	True
false	False
null	None
'''

dict_data = {"a": 1, "b": 2}
list_data = [{"aa": 1, "bb": 2}]

# json.dumps
dump_data = json.dumps(dict_data)
print(dump_data, type(dump_data))

# json.dumps
d_data = json.dumps(list_data)
print(d_data, type(d_data))

# json.loads
load_data = json.loads(dump_data)
print(load_data, type(load_data))

# json.load
with open("json_data.json", "r", encoding="utf-8") as fw:
    json_file_data = json.load(fw)
print(json_file_data, type(json_file_data))
