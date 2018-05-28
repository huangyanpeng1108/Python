#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/16 20:23
# @Author   : HYP
# @FileName : 作业讲解—三级菜单.py
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















