# coding=utf-8

# 打开文件，及时关闭
from __builtin__ import help

f = open('g:\\test.txt', 'r')
print type(f)
# 如果不及时关闭，会造成文件资源泄漏
f.close()


def openf():
    g = open('g:\\test.txt', 'r')
    if 0:
        g.close
        return
    g.close()


# 为了解决异常下无法关闭close,使用with保证
def openf():
    with open('g:\\test.txt', 'r') as g:
        print g.readlines()
        a = [0, 1, 2, 3]
    # a[5]   抛出异常，但是还是会关闭file


openf()


# 查看内建函数
# dir(_builtins_)


# 文件存储有一种编码方式（gbk）
# 代码读取文件也有一种编码方式（Unicode）
def openf():
    # with open('g:\\test.txt', 'r', encoding='utf8') as g:
    print g.readlines()


# 读文件
# read: 读指定长度字节数的数据, 返回一个字符串.
# readline: 读取一行数据, 返回一个字符串,
# readlines: 读取整个文件, 返回一个列表. 列表中的每一项是一个字符串, 代表了一行的内容.
# 直接使用 for line in f 的方式循环遍历每一行. 功能和readline类似. 一次只读一行, 相比于readlines
# 占用内存少, 但是访问IO设备的次数会增多, 速度较慢.

with open('g:/test.txt', 'r') as f:
    for line in f:
        print line
# 写文件
# write: 向文件中写一段字符串.
# 如需写文件, 必须要按照 'w' 或者 'a' 的方式打开文件. 否则会写失败.

