#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/1 11:07
# @Author   : HYP
# @FileName : 修改功能.py
# @Software : PyCharm

ret = []  # 定义一个空列表


def fetch(data):
    print("\033[1;44m这是查询功能\033[0m")
    print('\033[1;44m用户输入数据是：\033[0m', data)
    backend_data = 'backend %s' % data
    with open('haproxy.conf', 'r') as read_f:  # 打开文件
        tag = False
        for read_line in read_f:  # 循环文件每一行
            if read_line.strip() == backend_data:  # 当read_line与backend_data相同时
                tag = True
                continue
            if tag and read_line.startswith('backend'):  # 当 遇到下一个以backend开头时：
                # tag = False
                break  # 退出循环
            if tag:  # tag = True
                print(read_line, end='')
                ret.append(read_line)  # 添加到列表ret中
    return ret  # 返回 列表


def add():
    print('这是添加功能')

def change():
    print('这是修改功能')

def delete():
    pass

if __name__ == '__main__':  #
    msg = '''
        1:查询
        2:添加
        3:修改
        4:删除
        5:退出
    ''',
    msg_dic = {
        '1': fetch,
        '2': add,
        '3': change,
        '4': delete,
    }
    while True:
        print(msg)
        chioce = input("请输入你的选项:").strip()
        if len(chioce) ==0 or chioce not in msg_dic: continue
        if chioce == '5':break

        data = input('请输入你的数据：').strip()
        # msg_dic[chioce](data)
        if chioce != '1':
            data = eval(data)
        res = msg_dic[chioce](data)
        print(res)



