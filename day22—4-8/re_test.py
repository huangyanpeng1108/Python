#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/9 6:52
# @Author   : HYP
# @FileName : re_test.py
# @Software : PyCharm

# dic_yh = {'hyp':'123','alex':'456','shanshan':'789'}
#
# print(dic_yh.keys())


# # 登录验证程序
# list_name = ['hyp','alex','shan']
# list_pwd = ['123','456','789']
#
# flag = 0
# list_new = []
#
# while flag < 3:
#     name = input(">>>用户名：")
#     pwd = input(">>>密码：")
#
#     if name in list_name and pwd != list_pwd[list_name.index(name)]:
#         list_new.append(name)
#         n = list_new.count(name)
#         if n > 2:
#             print("对不起，%s账户已锁定" %name)
#         else:
#             print("第%s次输入错误,请重新输入！" %n)
#     elif name in list_name and pwd == list_pwd[list_name.index(name)]:
#             print('登录成功，欢迎光临%s！' %name)
#             break
#     else:
#         print('登录失败，用户名或密码错误，请重新输入！')
#
#     flag += 1


print('{}{}{}'.format('a','b'))


