#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/15 20:00
# @Author   : HYP
# @FileName : 三级菜单作业升级版本.py
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

# 终极版本
menu_layer = menu
last_layer = []
while True:
    for i in menu_layer:
        print(i)
    menu_choice = input(">>>:").strip()
    if not menu_choice:continue
    if menu_choice != 'q':
        if menu_choice in menu_layer:
            last_layer.append(menu_layer)
            menu_layer = menu_layer[menu_choice]
        elif menu_choice == 'b':
            menu_layer = last_layer.pop()
    else:
        break



# 思路混乱版
# list1 = []
# dic2 = {}
# flag = False
# count = 0
# for k in menu: # 第0级
#     print(k)
#
# while not flag:
#     menu_choice = input(">>>: ").strip()  # 第三级
#     if menu_choice != 'Q':  # 退出程序
#         # if menu_choice != 'q':  # 退出本次循环
#             if menu_choice in menu.keys():
#                 for k in menu[menu_choice]:
#                     list1.append(menu_choice)
#                     list2 = []
#                     list2.append(k)
#                     print(k)
#                 # count += 1
#                 dic = {}.fromkeys(list2, []).items()
#                 dic1 = {menu_choice:dic}
#                 dic2.setdefault(menu_choice,dic)
#                 list2.clear()
#                 menu = menu[menu_choice]
#                 # print(list2)
#             elif menu_choice == 'q':  # 退出本次循环
#                 for i in dic2[list1.pop()]:
#                     # count -= 1
#                     print(i)
#
#             # else:
#             #     print("输入地点不存在，请重新输入！")
#         # else:
#         #     # menu = menu[menu_choice]
#     else:
#         flag = True











