#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/18 10:18
# @Author   : HYP
# @FileName : 登录验证程序—自我检验版.py
# @Software : PyCharm

_users = [['hyp', '111'], ['lcy', '222'], ['asd', '333']]

count = 0
list_user = []  # 记录输入过的用户名
list_username = []  # 用于存储账户名
locked_username = []  # 用于存储被锁定的用户名

f = open("test1", "r")
user_flag = False
for line in f:
    locked_username.append(line.strip())

while count < 3:
    username = input("Username:").strip()
    password = input("Password:").strip()
    if username in locked_username:
        exit("此用户已锁定")
    for item in _users:
        # 把用户名添加到list_username列表里,用于后面判断输入的用户名是否存在
        list_username.append(item[0])
        if username == item[0] and password == item[1]:
            print("Welcome to Beijing")
            exit()
    else:
        print("用户名或密码输入错误")
        if username in list_username:
            # 把每一次对的用户名但密码错误的都进行储存 用于判断相同用户名输入次数
            list_user.append(username)
        if list_user.count(username) == 3:  # 判断用户名是否有三次输入错误的记录
            f = open("test1", "a")
            f.write(username + '\n')
            f.close()
            print("此用户已被锁定")
            break
    count += 1




