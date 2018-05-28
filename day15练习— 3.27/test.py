#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/27 15:31
# @Author   : HYP
# @FileName : test.py
# @Software : PyCharm

# ls = []
# def test(n):
#     n = int(n / 2)
#     ls.append(n)
#     print(n)
#     if int(n % 2) == 1:
#         return ls
#     # test(n)
#     # return ls
#     return(test(n))
# # test(5)
# print(test(5))


# def calc(n):
#     print(n)
#     if int(n / 2) == 0:
#         return n
#     return (calc(int(n / 2)))
#
# calc(10)
# # print(calc(10))


# name = 'hyp'
#
# def foo():
#     name = 'lcy'
#     def bar():
#         name = 'wupeiqi'
#         def tt():
#             print(name)
#         return tt()
#     return bar()
#
# foo()
# # print(foo())


# f = lambda x,y,z:(x+1,y+1,z+1)
# print(f(1,2,3))

 # 将列表的每一个元素加1，并筛选出不能被2整除的元素：
a_l = [1,2,3,4,5]
test = list(map(lambda x:x + 1,a_l))
print(list(map(lambda x:x + 1,a_l)))
print(list(filter(lambda x:x % 2,a_l)))

# print(list(filter(lambda x:x % 2,test)))
print(list(filter(lambda x:x % 2,list(map(lambda x:x + 1,a_l)))))



# print(list(filter(lambda x:x % 2,map(lambda x:x + 1,a_l))))



