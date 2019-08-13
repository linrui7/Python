# coding=utf-8

# 动态类型：在程序运行过程中类型发生改变
# 静态类型；运行过程中类型不能发生改变
# 强类型：越不支持隐式类型转换，类型越强。
# 弱类型：支持不同的类型进行转换。

# Python是一种动态强类型语言。
# 标准类型：整形，浮点型，复数型，布尔型，字符串，列表，元组，字典
# 其他内建类型：Null对象，类型，文件，函数，模块
# Null表示一个无意义的值
import math
import random


def func():
    if 0:
        a = "abc"
        return a
    else:
        return


# 没写返回值，返回Null

# 空字符串""。空列表[]。空元组()。空字典{}。有一个值的元组(2,)加上逗号区分()
a = [1, 2, 3]
b = [1, 2, 3]
# 比较对象值
if a == b:
    print "yes"
else:
    print "no"
# 比较对象身份
if id(a) == id(b):
    print "yes"
else:
    print "no"

# 比较是不是同一个对象
print (a is b)
print (a is not b)

# 对象类型比较
a = 100
print (type(a) == type(100))
print (isinstance(a, type(100)))

# 内置函数
print (abs(10))  # 绝对值
print (divmod(10, 2))  # 返回一个元组，商和余数
print (round(10, 1))  # 四舍五入,保留多少位小数
for i in range(0, 11):
    print (round(math.pi, i))  # 四舍五入,保留多少位小数

# 条件和循环
# 循环2次，生成0 ，1的随机数
for i in range(0, 2):
    print (random.randint(0, 1))
else:
    print "for循环已经走完"


# 函数定义和调用
def out():
    def inn():
        print "inn()"

    inn()


print (out())


# 函数叫可调用对象


def Print_add(x=0, y=0, z=0):
    print (x, y, z)


Print_add(100, 100)
Print_add(x=100, y=100)

# 排序
a = [1, 3, 5, 6, 5, 4, 3]
b = sorted(a)
print b
# 降序
c = sorted(b, reverse=True)
print c


# 自定义排序
def Cmp(x, y):
    if abs(x) < abs(y):
        return -1
    elif abs(x) > abs(y):
        return 1
    else:
        return 0


a = [1, -3, 4, 2]
print sorted(a, cmp=Cmp)


# 参数组
def log(**date):
    for key in date:
        print (key, date[key])


log(x=1, y=2, c=3)

# 不需要重载：
#    1.参数类型：动态类型解决
#    2.参数个数：参数组解决

# 函数返回值：return None或者return 对象

