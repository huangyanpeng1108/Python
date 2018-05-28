#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/29 9:33
# @Author   : HYP
# @FileName : 文件处理.py
# @Software : PyCharm

f = open('test11.py','wb')
f.write(bytes('111\n',encoding='utf-8'))

f.write('hyp\n'.encode('utf-8'))







































