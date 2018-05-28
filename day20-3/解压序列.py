#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/31 9:04
# @Author   : HYP
# @FileName : 解压序列.py
# @Software : PyCharm


# a,b,c = [1,2,3]
#
# print(a)
# print(b)
# print(c)

# 取第一个值和最后的一个值
l = [10,5,8,9,4,2,65,6,3,99]

a,*_,c = l

print(a)
print(c)
print(_)  # _ : 代表中间所有值

# 交换a, b的值

a = 1;b = 2
print(a)
print(b)

a,b = b,a
print(a)
print(b)