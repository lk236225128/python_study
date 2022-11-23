'''
list 有序,可变

增、查、改、删
'''

# 创建
list_1 = list()  # 实例化
list_2 = ["XiaoMi", "TengXun"]  # 直接定义

# list_1 效率高于 list_2

# 增
'''
append,insert,extend 
'''
list_1.append("Apple")  # 尾部追加
list_1.insert(0, "Huawei")  # insert插入到指定位置
list_1.extend(list_2)  # 连接list
print(list_1)

# 查
print(list_1[0])
print(list_1.index("XiaoMi"))  # 查找XiaoMi的索引
print(list_1.count("Apple"))  # 统计Apple的数量
print(len(list_1))  # 打印list的元素数量

# 改
# list_2 = ["XiaoMi", "TengXun"]
list_2[1] = "MeiTuan"
print(list_2)

# 删
'''
pop,remove,clear
'''
list_1.pop()  # 移除最后一个元素,并返回该值
list_1.pop(0)  # 移除首位元素
list_1.remove("Apple")  # 移除第一个值为Apple的元素
list_1.clear()  # 清空元素
del list_1[:]  # 清空元素

# list反转
nums = [1, 3, 2, 4, 5, 6, 7, 8, 9]
nums.reverse()  # 原对象反转
print(nums)
# 或 切片(-1步长)
print(nums[::-1])  # 返回反转后的新对象,原对象不变

# list排序
nums.sort()  # 原对象内排序
# or use sorted
sorted(nums)  # 返回排序后新对象
# 需要保证列表内的元素俩俩是可比较的,如数值和字符串是不可比较


'''
tuple 有序,不可变
'''
tp_1 = tuple()  # 实例化

tp_2 = (1, 2, 3)

tp_3 = 1, 2, 3, 4, 5  # ()可有可无

tp_4 = (1,)  # 单个元素的tuple结尾需用,

tp_5 = (i for i in range(1, 10))  # tuple推导式,返回generator

'''
元组是不可变的。因此，你想对元组进行修改、新增的行为都是不被允许.会报以下错误

新增、修改
TypeError: 'tuple' object does not support item assignment
删除
TypeError: 'tuple' object doesn't support item deletion
'''

# tuple 转 list,list 转 tuple
list(tp_1)
tuple(list_1)

'''
homework

1. 如何对列表的元素进行增(指定位置、尾部追加)、删、查、改
2. 如何对列表进行排序、找到某个值的序号
3. 如何统计列表的元素个数、最大值、最小值、某个元素出现的次数
4. 如何给一个列表数据进行去重操作？

'''
