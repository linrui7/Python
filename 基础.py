# coding=utf-8


# 生成 一个列表，新列表的数是原列表的n平方
a = [1, 3, 5, 2, 4, 6]
b = [x ** 2 for x in a]
print b
# pass 空语句
x = 10
if x % 2 == 0:
    pass
else:
    print x

# break continue
for i in range(1, 15):
    if i == 14:
        continue
    print i

# while 语句
count = 0
while count < 3:
    print count
    count += 1

# for 循环
for num in range(1, 11):
    print num;

a = [0, 1, 2, 3]
for num in a:
    print num

b = 'ABCdef'
for num in b:
    print num

c = {'ip': '127.16.8.10.1', 'port': 80}
for num in c:
    print num, c[num]

# if条件，如果表达值非0或者为True
result = '0'  # input("请输入1或者0\n")
print result
if int(result) == 1:
    print "你输入了1"
elif result == '0':
    print "你输入了0"
else:
    print "输入错误"


# 函数
def Add(x, y):
    return x + y


# 不能实现重载底下的函数，第二个函数覆盖了第一个函数
# 函数也是一个对象
def Add(x, y, z):
    ret = x + y + z
    return ret


print '10+20+30 =', Add(10, 20, 30)


# 多个值返回
def get_somereturn():
    a = 10
    b = 20
    return a, b


# umpack解包
a, b = get_somereturn()
# 或者返回一个元组tuple
tu = get_somereturn()
# 或者使用占位符_
_, a = get_somereturn()
print a
print b

# 文件操作
# 使用open打开一个文件,只读
openfile = open('G:/test.txt', 'r')
a = openfile.readlines()  # 返回一个列表
print a
openfile.close()

# 写操作
openfile = open('G:/test.txt', 'w')
openfile.write('aaa\ndddd\ndddd\ndddd\nddd\ndffff')  # 返回一个列表
print a
openfile.close()

print

# strip 去掉str类型的字符串的头和尾的空白。
handle = open('G:/test.txt', 'r')
words = {}
for word in handle:
    # word = word[:-1]  去掉末尾的 \n
    word = word.strip()
    if word not in words:  # 使用 in 关键字判定这个单词是否是字典的key.
        words[word] = 1
    else:
        words[word] += 1;
handle.close()
print words
