#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__: Caesar

"""

1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。

2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
"""

# 实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。

# def foo(str1, str2):
#     if str2 in str1:
#         res = str1.find(str2)
#         return res
#
# str1 = "hello,world."
# str2 = "wor"
# print(foo(str1, str2))



# 给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11


lst = [1,5,2,7,4,9,6]

# def foo(lst, n):
#
#     for i in lst:
#         j = n-i
#         if j in lst:
#             print(i,j)
# foo(lst, n)


def func(lst, n):
    res = []
    for k in range(len(lst)):
        for i in lst:
            if (n-i) in lst:
                res.append(lst.pop(k))
    return res


a = func(lst, 12)
print(a)
