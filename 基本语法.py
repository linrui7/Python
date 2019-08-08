# coding=utf-8
# from 基础 import Add  # 导入其他文件的函数，或者系统目录中的函数

# 跨行 可以使用 \换行
from cProfile import help

x = 1
y = 2
if x == 1 and \
        y == 2:
    print 'put'

# 三个引号也可以换行
print ''' SBcs
        qqq456'''

# 缩进规范，不建议用tab

# 多重赋值
x = y = 2

# 多元赋值
x, y = 1, 2
x, y = y, x

# Python的变量的生命周期
# Python提供了垃圾回收机制自动识别一个变量的
# 生命周期是否走到尽头, 并自动释放空间

# 作用域
# if, else, elif, while, for, try/exception不会改变作用域，可以在外部访问
# def class 不能访问内部的元素
# 即使出了 for 循环，还是能访问到i的值和x的值
for i in range(0, 10):
    x = 2
    print(i)
print i
print x

# 特殊标识符
# Python使用下划线(_)作为变量的前缀和后缀, 来表示特殊的标识符.
# _xxx表示一个 "私有变量"  无法通过导包使用


# 文档字符串 使用_doc_ 或者help()查看
'''
定义了add函数
'''


def add(x, y):
    """
    文档内容：
    返回两个对象相加的加法
    """
    return x + y


print add.__doc__

# 对象
# Python中任何值都是一个对象。
# 包含id 类型 值


