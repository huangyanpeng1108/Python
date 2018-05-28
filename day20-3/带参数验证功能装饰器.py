#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/31 20:53
# @Author   : HYP
# @FileName : 带参数验证功能装饰器.py
# @Software : PyCharm

user_list = [
    {'name':'hyp','passwd':'123'},
    {'name':'lcy','passwd':'123'},
    {'name':'h','passwd':'123'},
    {'name':'p','passwd':'123'}
]

current_dic = {'username':None,'login':False}  # 记录当前用户状态

def auth(auth_type = 'filedb'):
    def auth_func(func):
        def wrapper(*args,**kwargs):
            print('认证类型是',auth_type)
            if auth_type == 'filedb':
                if current_dic['username'] and current_dic['login']:
                    res = func(*args, **kwargs)
                    return res
                username = input('用户名：').strip()
                passwd = input('密码：').strip()

                for user_dic in user_list:
                    if username == user_dic['name'] and passwd == user_dic['passwd']:
                        current_dic['username'] = username
                        current_dic['login'] = True
                        # func(*args, **kwargs)
                        res = func(*args,**kwargs)
                        return res
                else:
                    print('用户名或密码错误，登录失败')
            elif auth_type == 'ldap':
                print('鬼才会玩')
                res = func(*args, **kwargs)
                return res
            else:
                print('不知道')
                res = func(*args, **kwargs)
                return res
        return wrapper
    return auth_func

@auth(auth_type = 'filedb')
def index():
    print('欢迎来到京东主页')

@auth(auth_type = 'ladap')
def home(name):
    print('欢迎回家%s' %name)

@auth(auth_type = 'kkkkk')
def shopping_car(name):
    print('%s的购物车里有[%s,%s,%s]' %(name,'奶茶','妹妹','娃娃'))

index()
home('hyp')
shopping_car('hyp')


