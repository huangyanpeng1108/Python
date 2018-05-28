#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/16 15:23
# @Author   : HYP
# @FileName : 购物车小程序作业.py
# @Software : PyCharm

"""
    待改进：上一次的余额 需要另存一个文档

"""

# 购物车小程序
_users = [['hyp', '111'], ['lcy', '222'], ['asd', '333']]
flag = False  # 循环判断标志位
count = 0
wages_flag = True  # 上一次余额的标志位
shopping_car = []
list_record = []  # 存储已买商品，用于下一次登录时，打印已买商品

while not flag and count < 3:
    username = input("用户名：").strip()
    password = input("密码：").strip()
    for item in _users:  # 遍历用户名和密码
        if username == item[0] and password == item[1]:
            flag = True
            print("登录成功，欢迎光临！")
            # 查询上一次消费记录
            f = open("shopping_cars", 'r', encoding='utf-8')
            for line in f:
                list_record.append(line.strip())
            # f.close()  # 注意
            if len(list_record):
                line_wages = list_record.pop()  # 记录上一次余额，待打印
                print(list_record)
                print("----------已购买的商品如下----------")
                # 遍历已买的商品
                for index, i in enumerate(list_record):
                    i = eval(i)
                    print("%s. %s %s" % (index, i['name'], i['price']))
                print(line_wages)
                wages_flag = False  # 同一用户下一次登录时，不需要输入工资

            goods = [
                {"name": "电脑", "price": 1999},
                {"name": "鼠标", "price": 10},
                {"name": "游艇", "price": 20},
                {"name": "美女", "price": 998}
            ]

            # if wages_flag:  # 是否需要再次输入工资
            while wages_flag:
                wages = input("工资：").strip()
                if not wages.isdigit():
                    print("输入错误，请重新输入")
                elif wages.isdigit():
                    wages_flag = False

            else:
                # 从文件中得到上一次的余额，以便再次消费
                h = open("last_wages", 'r', encoding='utf-8')
                for i in h:
                    wages = int(i)
                    break
            while flag:
                print("-----------商品列表-----------")
                for index, k in enumerate(goods):
                    print("\033[1;34;40m%s. %s %s\033[0m" % (index, k['name'], k['price']))
                choice = input('>>>商品编号选择:')

                if choice == 'q' or choice == 'Q':  # 退出购买，打印已购买商品和余额
                    if len(shopping_car) != 0:
                        print("已购买的商品如下".center(30,'-'))
                        for index, k in enumerate(shopping_car):
                            print("\033[1;34;40m%s. %s %s\033[0m" % (index, k['name'], k['price']))
                        print("\033[1;35;40m余额为：%d\033[0m" % wages)
                        # 用于存储上一次的余额
                        h = open("last_wages", 'w', encoding='utf-8')
                        h.write(str(wages) + '\n')
                        h.close()
                        f = open("shopping_cars", 'a', encoding='utf-8')
                        f.write("余额为:" + str(wages) + '\n')
                        f.close()
                        exit()
                else:
                    if choice.isdigit() and int(choice) < len(goods):
                        if goods[int(choice)]['price'] <= int(wages):
                            # 把选择的商品添加到购物车当中
                            shopping_car.append(goods[int(choice)])
                            f = open("shopping_cars", 'a', encoding='utf-8')
                            f.write(str(goods[int(choice)]) + '\n')
                            f.close()
                            wages = int(wages) - goods[int(choice)]['price']
                            print("%s已添加到购物车中" % goods[int(choice)])
                            print("还剩余额为：%s" % wages)
                        else:
                            print("您的余额已不足，请充值！")
                    else:
                        print("输入错误，请重新输入！")
    else:
        print("用户名或密码错误，请重新输入！")
        count += 1