#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/15 8:12
# @Author   : HYP
# @FileName : list学习.py
# @Software : PyCharm

# 创建空列表
list_1 = []
list()

# 查询
name = ['hyp', 'lcy', 'yuh', 'qwe', '鹏哥']
# print(name[0])

# # 索引 下标
# n2 = [1, 4, 8, 5, 2, 5, 8, 6, 2, 5]
# n2.index(6)
# print(n2.index(6))
#
# # 统计5的个数
# n2.count(5)
#
# # 切片
# print(n2[1:5])
#
# print(n2[2: 9: 2])  # 步长
#
# # 增加
# name.append('ypu')  # 插到末尾
# print(name)
#
# # insert ：指定位置插入
# name.insert(1, 'abc')
# print(name)
#
# # 修改
# name[2] = 'cvb'  # 修改一个
# print(name)
#
# name[1:3] = 'asd'  # 批量修改
# print(name)
#
# # 删除
# name.pop() # 删除最后一个
# name.remove('hyp')
#
# del name[3]   # 删除元素
#
# del name[1:3] # 批量删除

# # 循环
# for k in name:
#     print('loop', k)

# # range
# for i in range(10):
#     print(i)
#
# # 排序
# # n = ['a', 'e', 'q', '好', 14]
n = ['a', 'e', 'q', 'A', '!']
# n.sort()  # 数字和字符串不能一起排序
# print(n)  # 按 ASCII 表进行排序

# # 拼接
# n2 = [1, 2, 4]
# n.extend(n2)  # 在 n列表 的末位进行拼接
# print(n)

# 复制 copy

# n3 = ['q', 'e', 'r', 'fr']
# for i in n3:
#     print(n3.index(i), i)

# # enumerate 枚举
# n3 = ['q', 'e', 'r', 'fr']
# for k, i in enumerate(n3):
#     print(k, i)
#     if k % 2 == 0:  # 偶数
#         n3[k] = -1
# print(n3)

# # 找出第二个2的索引值，不能人肉搜索
# # 先索引，后切片
# n3 = ['we', 'q', 2, 'e', 'r', 'sw', 'zz', 2, 'fr', 'hyp', 2]
# print(n3.index(2))
# print(n3[3:].index(2))

# 打印商品列表 购物车小程序

# _name = 'hyp'
# _pwd = '123'
# while 1:
#     username = input("用户名：")
#     password = input("密码：")
#     if username == _name and password == _pwd:
#         pass
#     else:
#         print("用户名或密码错误，请重新输入！")


products = [['iphone', 6888], ['MacPro', 11488], ['iPad4', 3888], ['iWatch', 2888]]
shopping_car = []
wages = int(input("工资："))
while 1:
    print("-----------商品列表---------")
    for index, k in enumerate(products):
        print("%s. %s %s" % (index, k[0], k[1]))
    choice = input('>>>商品选择:')

    if choice == 'q' or choice == 'Q':
        print("购物车中的商品如下:\n", shopping_car)
        print("余额为：", wages)
        # print("本次共消费：", )
        break
    else:
        if choice.isdigit() and int(choice) <= len(products):
            # 把选择的商品添加到购物车当中
            shopping_car.append(products[int(choice)])
            if products[int(choice)][1] <= wages:
                wages = wages - products[int(choice)][1]
                print("%s已添加到购物车中" % products[int(choice)])
                print("还剩余额为：%s" % wages)
            else:
                print("您的余额已不足，请充值！")
        else:
            print("输入错误，请重新输入！")
            continue




