# coding=utf-8

# 序列 包含若干个元素，有序（如果顺序改变，值也就发生变化）排列，可以通过下标访问到一个或者多个元素。
# a[0,1,2] != b[1,2,0]    //有序，改变顺序影响。
# a{a:1,b:2} == b{b:2,a:1}  //无序

# 重复操作符* 让一个序列重复N次
import copy

a = [1, 2]
print a * 5

# 拼接
b = [4, 5]
a.extend(b)
print a
# 拼接多个字符串
a = ['a', 'b', 'c']
print a + b
result = ''.join(a)
print result
result = ':'.join(a)
print result

# 切片操作[)前闭后开
a = [1, 2, 3, 4]
print a[:]  # 全部
print a[1:2]  # 从下标1到2
print a[2:]  # 从下标2之后
print a[:2]  # 从0-2
# 步长
print a[::2]  # 每次走两步
print a[::-1]  # 倒着走 翻转

# 字符串逆序
a = 'abcafg'
print ''.join(a[::-1])

# 序列内建函数
a = [1, 5, 6, 47, 5, 4]
print max(a)
print (sorted(a))


def sort_find(list, x):
    for i in list:
        if list[i] == x:
            return i
        else:
            return None


def sort_find(list, x):
    for i, val in enumerate(list):
        if val == x:
            return i
        else:
            return None


# zip函数 拉链
x = [1, 3, 5, 7]
y = [2, 4, 6, 8]
c = [0, 0]
for i in zip(x, y, c):
    print i

# 用zip 构建字典
key = ('name',)
value = ('zhangsan',)
a = dict(zip(key, value))
print a

# 不可变对象：线程安全
# 字符串是使用,不可变，重新创建对象
# 如果需要将abc变为1bc
a = 'abc'
a = '1' + a[1:]

a = '1' + 'abc'
print a

a = 10
# Pyhton3   采用s = s'a={a}'  print a
# 也可以s = 'a=%d' % a 容易出错


# 转义字符 加上r
print r'%d d\n123'
print '%d d\n123'

# 列表
a = [
    [1, 2, 3],
    ['..'],
    ['sddd']
]
print a

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.extend([5, 6])
b.append([5, 6])
print a
print b

# 删除引用
a = [1, 2, 3, 4]
del a[2]
print a
# del a删除a这个列表

# 删除值
a = [1, 2, 4, 2, 3, 4]
a.remove(2)
print a

# 查找On
print (2 in a)

# list里面的sort函数
a = [1, 3, 5, 8, 7, 6]
# 重新创建对象
print sorted(a)
print a
# 修改了本身
print a.sort()
print a

# 深浅拷贝
# import copy
# 对于可变对象list dict才能深拷贝
# 不可变对象只能浅拷贝
a = [1, 3, 5, 7]
b = copy.deepcopy(a)

# 元组
a = (1, 2, 3)
a = a + (3,)
print a

a, b = 30, 30  # 相当于元组 (a,b)=(30,30)
print b

# 元组不可变，是元组里面的id 不变。如果元组里面包含可变对象，就可以修改。
a = ([1, 2, 3], [4, 5, 6])
a[0][0] = 100
print(a)

# 字典里面存的是键值对，键不可修改。同时可以hash
# 两种方式创建
a = {1: 'name', 2: 'age', 3: 20}
print a
a = dict((['x', 1], [2, 'age']))
print a

# 修改元素
a['x'] = 20
print a

# 访问
for i in a:
    print i, a[i]

# 删除
del (a['x'])
print a
# 全部删除
a.clear()

# 如果是字典进行赋值操作，可以直接取key。
# 如果是查找，就要先判定key是否存在，才能取值。没有key会抛出异常。
# 使用in/not in来判定一个key是否在字典中.

# 内置函数
print hash(100)
print hash('aaa')
# print hash(()) 求hash只能是不可变的。

a = {1: 'name', 2: 'age', 3: 20}
print a.keys()
print a.values()
print a.items()
print a

# set 集合 基于字典实现的数据结构。
a = set([1, 2, 3, 4])
b = set([2, 2, 3, 5, 6])
print b
print a | b  # 并集
print a ^ b  # 对称差集
print a & b  # 交集
print a - b  # 差集

# 数据去重
a = [1, 2, 3, 4, 8, 7, 8, 8]
a = list(set(a))
print a
