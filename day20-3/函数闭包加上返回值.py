#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/30 20:54
# @Author   : HYP
# @FileName : 函数闭包加上返回值.py
# @Software : PyCharm

import time

def timmer(func):
    def wrapper():
        start_time = time.time()
        res = func()
        stop_time = time.time()
        print('test函数运行时间为%s' %(stop_time - start_time))
        return res
    return wrapper

@timmer
def test():
    time.sleep(1)
    print('test函数运行完毕')
    return '这是test的返回值'
res = test()
print(res)





