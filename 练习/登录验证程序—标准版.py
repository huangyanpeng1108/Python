#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/17 15:56
# @Author   : HYP
# @FileName : 登录验证程序—标准版.py
# @Software : PyCharm


users = [['lcy', '222'], ['hyp', '111']]
pass_flag = False
count = 0
first_input_flag = None  # 记录第一次的用户名
is_same_user = True  # 用于判断三次输入的用户名是否相同
# 从锁定文件里把锁定用户读出来
f = open("test", "r")
locked_users = []
for line in f:
    locked_users.append(line.strip())

while count < 3:
    _username = input("username:").strip()
    _password = input("password:").strip()

    if _username in locked_users:
        exit("此用户已锁定")

    if not first_input_flag:
        first_input_flag = _username
    if _username != first_input_flag:  # 代表本次输入的用户名跟第一次不同
        is_same_user = False  # 多次输入就不是同一次用户

    for user_item in users:
        if user_item[0] == _username and user_item[1] == _password:
            print("欢迎%s" % _username)
            pass_flag = True
            break
    else:
        print("username or password is wrong")
    if pass_flag:  # 代表认证成功
        break
    count += 1
else:
    print("too many attempts....")
    if is_same_user:  # 代表同一用户
        # 要锁定
        f = open("test", "a")  # a 代表追加
        f.write(_username+'\n')
        f.close()
        print("此用户已锁定", _username)