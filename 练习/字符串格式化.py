#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/14 0:10
# @Author   : HYP
# @FileName : 字符串格式化.py
# @Software : PyCharm

# 字符串格式化输出
name = input('Name:')
age  = input('Age :')
job  = input('Job :')

info = '''
----------- info of %s ----------
Name :   %s
Age  :   %s
Job  :   %s
----------- end ------------------
''' % (name,name,age,job)

print(info)