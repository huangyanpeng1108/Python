#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/14 8:25
# @Author   : HYP
# @FileName : if语句.py
# @Software : PyCharm

# # 升级版
#
# age = 18
# count = 0
#
# while count < 4:
#     if count == 3:
#         choice = input("是否继续玩（y/n）：")
#         if choice == 'y' or choice == 'Y':
#             count = 0
#         elif choice == 'n' or choice == 'N':
#             print("已退出游戏")
#             break
#         else:
#             print("输入错误！请重新输入")
#             continue
#     user_guess = int(input("your guess:"))
#     if user_guess == age:
#         print("猜对了")
#         break
#     elif user_guess < age:
#         print("猜小了")
#     else:
#         print("猜大了")
#     count += 1


# # while....else   作用：else 检查问题，中间程序如果有退出的话，就不会执行else
# count = 0
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("loop is down...")
# print("out of loop")


# count = 0
# while count < 3:
#     score = int(input(">>>:"))
#     if score > 100:
#         print("成绩不可能大于100")
#     elif score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 60:
#         print("C")
#     elif score >= 0:
#         print("D")
#     else:
#         print("成绩不可能为负数")
#     count += 1

# count = 0
# while count <= 100:
#     if count == 50:
#         pass
#     elif count >= 60 and count <= 80:
#         print(count**2)
#     else:
#         print(count)
#     count += 1


# 死循环 dead loop


# 第二章 二进制运算，字符编码

# print(bin(342))

# 二进制怎么转为文字： ASCII表，一个二进位就是 1 bit；8 bit = 1 bytes
# 中文编码表：GB2312,  gbk,

#! -*- coding；utf-8 -*-

# 列表 : []   元组：()  字典：{}   集合：{}
# 有序类型：列表，元组，字符串,都可迭代；  无序类型：字典，集合，不可迭代；
# tuple1 = (1, 'hyp', 5, 8, 'l')
# print(tuple1)


# person = {"name": "hyp", "age": 18}
#
# person1 = dict(name='lcy', age=19)
#
# person2 = dict({"name": "sfv", "age": 20})
#
# person3 = dict((['name','hyp'],['lcy',20]))
# {}.fromkeys(seq,100)   # 不指定100，默认为None
#
# # 注意
# >>> dic = {}.fromkeys(['k1','k2'],[])
# >>> dic
# {'k1': [], 'k2': []}
# >>> dic['k1'].append(1)
# >>> dic
# {'k1': [1], 'k2': [1]}

set
