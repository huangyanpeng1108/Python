#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/30 20:14
# @Author   : HYP
# @FileName : 练习装饰器.py
# @Software : PyCharm

import time

def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('test函数运行时间为%s' %(stop_time - start_time))
    return wrapper



@timmer
def test():
    time.sleep(2)
    print('test函数运行完毕')

test()



# import time
#
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('test函数运行时间为%s' % (stop_time - start_time))
#     return wrapper
#
#
#
# @timmer
# def test():
#     time.sleep(3)
#     print('test函数运行完毕')
#
# test()



