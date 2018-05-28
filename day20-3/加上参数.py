#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/30 21:08
# @Author   : HYP
# @FileName : 加上参数.py
# @Software : PyCharm

import time

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('test函数运行时间为%s' %(stop_time - start_time))
        return res
    return wrapper

@timmer
def test(name,age):
    time.sleep(1)
    print('test函数运行完毕,名字是【%s】 年龄是【%s】' %(name,age))
    return '这是test的返回值'

# res = test('hyp',18)
# print(res)

test('hyp',18)