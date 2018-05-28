#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/17 14:49
# @Author   : HYP
# @FileName : 三级菜单——第2遍.py
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

current_layer = menu
list_layer = []
while True:
    for i in current_layer:
        print(i)
    choice = input(">>>: ")
    if not choice: continue
    if choice in current_layer:
        list_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        exit()
    elif choice == 'q':
        if len(list_layer) != 0:
            current_layer = list_layer.pop()
        else:
            print("已经到最上层了")





















