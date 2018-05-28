#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/3/28 19:07
# @Author   : HYP
# @FileName : 内置函数.py
# @Software : PyCharm

# # abs : 取绝对值
# print(abs(-1))
#
# # all ：所有的都为真，才为真；一个为假，就为假。
# print(all([1,2,'5']))  # True
# print(all([1,2,'5',''])) # False
# print(all('1230')) # True
# print(all('')) # True
#
# # any:
#
# # bin: 十进制转换二进制；
# print(bin(3))
#
# # bool: 布尔值；空，None，0 --> 都为 False; 其余都为 True
# print(bool(''))
# print(bool(5))
#
# # bytes : 编码转换二进制
# name = '你好'
# print(bytes(name,encoding='utf-8'))
# print(bytes(name,encoding='utf-8').decode('utf-8'))   # 用什么编码，就用什么解码
#
# print(bytes(name,encoding='gbk'))
# print(bytes(name,encoding='gbk').decode('gbk'))   # 用什么编码，就用什么解码
#
# # print(bytes(name,encoding='ascii'))  # ascii不能编码中文
#
# # chr : ascii 表
# print(chr(97))  # a
#
# # dir ：打印某一个对象的目录下都有什么方法
# print(dir(all))
# print(dir(dict))
#
# # divmod :
# print(divmod(10,3))  # 用来做分页功能的，例：10条信息，每页3条信息，分3页，余1，
# print(divmod(8,2))
#
# # eval：①把字符串的数据结构提取出来，② 计算字符串中的数学运算
#
# # hash : 可哈希的数据类型，不可变数据类型；
# print(hash('asdds54524ewfc45sdc'))
#
# # help:
#
# # hex : 十进制转换二进制，
# # oct ： 十进制转换八进制，
#
# # isinstance() : 判断类型
# print(isinstance(1,int))

# # locals ；
# name = 'hyp'
# print(globals())
# print(locals())

# # zip ；拉链
# print(list(zip(('a','b','c'),(1,2,3))))
#
# print(list(zip(('a','b','c'),(1,2,3,4))))
#
# print(list(zip('hello','12345')))

# # max, min : 取最大值，最小值。
#
# age_dic = {'age1':18,'age2':4,'age3':10,'age4':5}
# print(max(age_dic.values()))
#
# # 默认比较的是字典的key
# print(max(age_dic))
# print((max(zip(age_dic.values(),age_dic.keys()))))
# print(list(max(zip(age_dic.values(),age_dic.keys()))))


# # ord ：
# print(ord('a'))  # 97
#
# # pow:
# print(pow(10,3))  # 3**3
# print(pow(10,3,2)) # 3**3%2

# # reversed()  : 反转
# h = [1,2,3,4,5]
# print(list(reversed(h)))
# print(h)
#
# # round : 四舍五入
# print(round(3.4))
#
# # set ：集合
# print(set('hyp'))

# # slice :
# l = 'hyphyplcy'
# s1 = slice(3,5)
# s2 = slice(1,4,2)
#
# print(l[s1])
# print(l[s2])
# print(l[3:5])

# # sorted ：排序, 从小到大。本质就是在比较大小，只有同类型之间的比较，不同类型的不能比较。
#
# l = [5,4,8,9,2,1,3,0]
# ll = [5,4,'a',8,9,2,1,3,0]
# print(sorted(l))
# print(sorted(ll))  # 报错
# #print(sorted(people,key=lambda dic:dic['age']))

# # sorted :
# name_dic = {
#     'hyp':100,
#     'lcy':200,
#     'sdf':50
# }
# print(sorted(name_dic))
# print(sorted(name_dic,key = lambda key:name_dic[key]))
# print(sorted(zip(name_dic.values(),name_dic.keys())))
# # print(name_dic[key])

# str : 字符串的转换

# eval :

# sum : 求和

# # type : 查看数据类型
# asd = '123'
#
# if type(asd) is str:
#     asd = int(asd)
#     hyp = asd + 1
#     print(hyp)

# vars :

# import : 导入模块




















