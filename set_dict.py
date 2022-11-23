'''
set 无序,不重复
'''

s_1 = set()
s_2 = set(["b", "c"])
s_3 = {"a"}

''''''
s_1.add("abc")

# update 函数后接集合，列表，元组，字典. 可添加元素
s_1.update([1, 2, 3])
s_1.update({"name": "kevin"})
print(s_1)

'''
删
'''
s_1.remove("abc")  # 移除元素,不存在会报KeyError错误

s_1.discard("a")  # 移除元素,不存在也不会报错

s_1.pop()  # 随机删除元素

s_1.clear()  # 清空set

'''
集合运算
'''
a_set = {"apple", "banana"}
b_set = {"Huawei", "Tengxu", "apple"}

# 并售
print(a_set.union(b_set))
print(a_set | b_set)

# 差集
print(a_set.difference(b_set))
print(a_set - b_set)

# 交集
print(a_set.intersection(b_set))
print(a_set.intersection_update(b_set))  # intersection_update 会原地更新在 aset,返回None
print(a_set & b_set)

# 不重合集
print(a_set.symmetric_difference(b_set))
print(a_set.symmetric_difference_update(b_set))

'''
集合判断
'''
print("apple" in a_set)
print(a_set.isdisjoint(b_set))  # 是否有相同元素
print(a_set.issubset(b_set))  # 是否是子集

'''
字典,由一系列的键值（key-value）对组合而成的数据结构
'''

d_1 = dict()
d_2 = dict(name="kevin")

info = [("name", "kevin"), ("age", 18)]
print(dict(info))

d_4 = {x: x * 2 for x in range(1, 20)}  # 字典推导式
print(d_4)

# 增
d_2["age"] = 20
# 查
print(d_2["name"])
print(d_2.get("age"))

# 改
d_2["age"] = 20

# 删
d_2.pop("age")
del d_2["name"]

# 判断
print("name" in d_2)
print("name" not in d_2)

# 设置默认值
d_2.setdefault("heigh", 172)
print(d_2)
