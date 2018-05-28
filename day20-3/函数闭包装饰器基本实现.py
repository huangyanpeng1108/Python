#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/30 19:52
# @Author   : HYP
# @FileName : 函数闭包装饰器基本实现.py
# @Software : PyCharm

# 装饰器的框架：
# def timmer(func):
#     def wrapper():
#         func()
#     return wrapper

# 举例：
import time
def timmer(func):     # func = test
    def wrapper():
        # print(func)
        start_time = time.time()
        func()    # 就是在运行test()
        stop_time = time.time()
        print('运行时间是%s' % (stop_time - start_time))
    return wrapper

@timmer          # test = timmer(test)
def test():
    time.sleep(3)
    print('test函数运行完毕')

# test = timmer(test)   # 返回的是wraper的地址
# test()    # 执行的是wrapper()     start_time = time.time()

 # @timmer    就相当于 test = timmer(test)

test()


