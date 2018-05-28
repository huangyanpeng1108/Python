#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/28 17:21
# @Author   : HYP
# @FileName : reduce函数.py
# @Software : PyCharm


# from functools import reduce

# num_l = [1,2,3,4,5,6,7,8,9,10]
# res = 0
# for num in num_l:
#     res+=num
#
# print(res)

#
# num_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def reduce_test(array):
#
#     res = 0
#     for num in array:
#         res += num
#     return  res
#
# print(reduce_test(num_l))

# map  filter函数：


# reduce 函数：
# from functools import reduce
#
# num_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reduce(lambda x,y:x+y,num_l,50))  # 50是设置的初始值


from functools import reduce

print(reduce(lambda x,y:x+y,range(1,101)))
print(reduce(lambda x,y:x+y,range(1,101),100))

















