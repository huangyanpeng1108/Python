#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/8 7:35
# @Author   : HYP
# @FileName : os模块.py
# @Software : PyCharm


import os,sys,time

# print(os.getcwd())  # 获取当前工作目录
# os.chdir("")          # 改变当前的脚本工作目录
# os.curdir           # 返回当前目录：（'.'）
# os.pardir           # 获取当前目录的父目录字符串名：（'..'）

# print(os.system("dir"))

for i in range(100):

    sys.stdout.write('#')    # 做进度条
    time.sleep(0.2)          # 延时
    sys.stdout.flush()       # 缓存多少，就显示多少



