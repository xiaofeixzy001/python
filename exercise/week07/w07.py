#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__: Caesar


"""
1、请将 "1,2,3"，变成 ["1","2","3"]
2、使用Python copy一个文件，从a目录,copy文件到b目录
3、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
"""


# 1,将 "1,2,3"，变成 ["1","2","3"]

# s = "1,2,3"
# s1 = list(s.split(','))
# print(s1)


# 2,使用Python copy一个文件，从a目录,copy文件到b目录

srcfile = "a/test.txt"
dstfile = "b/test.txt"
def copy(srcfile, dstfile):
    with open(srcfile, 'r', encoding='utf-8') as f1:
        with open(dstfile, 'w', encoding='utf-8') as f2:
            f2.write(f1.read())

copy(srcfile, dstfile)


# 3,以下代码输出什么，请解释原因(写到问题下方)
"""
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)

说明：

li = [[]] * 5   # [[],[],[],[],[]]
意思是列表li内的元素乘5，然后在赋值给li，也就是[[],[],[],[],[]]

li[0].append(10)
print(li)  # [[]10,[10],[10],[10],[10]]

li[1].append(20)  #  [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
print(li)

li内的列表元素是一段内存地址，而非具体的值，使用*号复制5份，都是指向同一段内存地址，
所以只要修改任何一个元素，都会同步被修改。

li.append(30)  # [[],[],[],[],[], 30]  --> [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
print(li)

"""
