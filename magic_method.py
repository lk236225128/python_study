# -*- coding: utf-8 -*-
# @Time : 2022/11/23 09:02
# @Author : Kevin
# @File : magic_method.py
# @Software: PyCharm


'''
比较操作符
● __eq__(self, other)定义等于操作符(==)的行为。
● __ne__(self, other)定义不等于操作符(!=)的行为。
● __lt__(self, other)定义小于操作符(<)的行为。
● __gt__(self, other)定义大于操作符(>)的行为。
● __le__(self, other)定义小于等于操作符(<)的行为。
● __ge__(self, other)定义大于等于操作符(>)的行为。
'''

'''
一元操作符
● __pos__(self)实现取正操作，例如 +some_object。
● __neg_(self)实现取负操作，例如 -some_object。
● __abs__(self)实现内建绝对值函数 abs() 操作。
● __invert__(self)实现取反操作符 ~。
● __round__(self， n)实现内建函数 round() ，n 是近似小数点的位数。
● __floor__(self)实现 math.floor() 函数，即向下取整。
● __ceil__(self)实现 math.ceil() 函数，即向上取整。
● __trunc__(self)实现 math.trunc() 函数，即距离零最近的整数。
'''

'''
常见算数操作符
● __add__(self, other)实现加法操作。
● __sub__(self, other)实现减法操作。
● __mul__(self, other)实现乘法操作。
● __floordiv__(self, other)实现使用 // 操作符的整数除法。
● __div__(self, other)实现使用 / 操作符的除法。
● __truediv__(self, other)实现 true 除法，这个函数只有使用 from __future__ import division 时才有作用。
● __mod__(self, other)实现 % 取余操作。
● __divmod__(self, other)实现 divmod 内建函数。
● __pow__(self)实现 ** 操作符。
● __lshift__(self, other)实现左移位运算符 << 。
● __rshift__(self, other)实现右移位运算符 >> 。
● __and__(self, other)实现按位与运算符 & 。
● __or__(self, other)实现按位或运算符 | 。
● __xor__(self, other)实现按位异或运算符 ^ 。
'''

'''
反射算数运算符
● __radd__(self, other)实现反射加法操作。
● __rsub__(self, other)实现反射减法操作。
● __rmul__(self, other)实现反射乘法操作。
● __rfloordiv__(self, other)实现使用 // 操作符的整数反射除法。
● __rdiv__(self, other)实现使用 / 操作符的反射除法。
● __rtruediv__(self, other)实现 true 反射除法，这个函数只有使用 from __future__ import division 时才有作用。
● __rmod__(self, other)实现 % 反射取余操作符。
● __rdivmod__(self, other)实现调用 divmod(other, self) 时 divmod 内建函数的操作。
● __rpow__(self)实现 ** 反射操作符。
● __rlshift__(self, other)实现反射左移位运算符 << 的作用。
● __rshift__(self, other)实现反射右移位运算符 >> 的作用。
● __rand__(self, other)实现反射按位与运算符 & 。
● __ror__(self, other)实现反射按位或运算符 | 。
● __rxor__(self, other)实现反射按位异或运算符 ^ 
'''

