#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/15 14:31
# @Author   : HYP
# @FileName : 三级菜单 作业.py
# @Software : PyCharm

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

flag1 = False
flag2 = False
flag3 = False
for k in menu:  # 第0级
    print(k)
while not flag1:
    menu_choice1 = input(">>>: ").strip()  # 第一级
    if menu_choice1 == "Q":  # 退出程序
        flag1 = True
        flag2 = True
        flag3 = True
    else:
        if menu_choice1 == 'q':  # 退出本次循环
            for k in menu:  # 第0级
                print(k)
            flag1 = True
        else:
            if menu_choice1 in menu.keys():
                for k in menu[menu_choice1]:
                    print(k)

                while not flag2:
                    menu_choice2 = input(">>>: ").strip()  # 第二级
                    if menu_choice2 == "Q":
                        flag1 = True
                        flag2 = True
                        flag3 = True
                    else:
                        if menu_choice2 == 'q':
                            for k in menu[menu_choice1]:
                                print(k)
                            flag2 = True
                        else:
                            if menu_choice2 in menu[menu_choice1].keys():
                                for k in menu[menu_choice1][menu_choice2]:
                                    print(k)

                                while not flag3:
                                    menu_choice3 = input(">>>: ").strip()  # 第三级
                                    if menu_choice3 == "Q":
                                        flag1 = True
                                        flag2 = True
                                        flag3 = True
                                    else:
                                        if menu_choice3 == 'q':
                                            for k in menu[menu_choice1][menu_choice2]:
                                                print(k)
                                            flag3 = True
                                        else:
                                            if menu_choice3 in menu[menu_choice1][menu_choice2].keys():
                                                for k in menu[menu_choice1][menu_choice2][menu_choice3]:
                                                    print(k)
                                            else:
                                                print("输入地点不存在，请重新输入！")
                            else:
                                print("输入地点不存在，请重新输入！")
            else:
                print("输入地点不存在，请重新输入！")

























