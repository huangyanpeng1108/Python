
# 登录验证程序
list_name = ['hyp', 'alex', 'shan']
list_pwd = ['123', '456', '789']

flag = 0
list_new = []

while flag < 3:
    username = input(">>>用户名：")
    password = input(">>>密码：")

    if username in list_name and password != list_pwd[list_name.index(username)]:
        list_new.append(username)
        n = list_new.count(username)
        if n > 2:
            print("对不起，%s账户已锁定" % username)
        else:
            print("第%s次输入错误,请重新输入！" % n)
    elif username in list_name and password == list_pwd[list_name.index(username)]:
            print('登录成功，欢迎光临%s！' % username)
            break
    else:
        print('登录失败，用户名或密码错误，请重新输入！')

    flag += 1

# # 1、casefold() : 将字符串的所有字符变小写。
# s = "HYPlcy"
# print(s.casefold())  # 结果：hyplcy
#
# # 2、count(sub[,start[,end]]) : 查找子字符串出现的次数
# str1 = "asdfgasdfgasert"
# print(str1.count("as"))
#
# # 3、index(sub[,start[,end]]) : 查找子字符串在该字符串中的位置，找到了返回第一个字符的索引值
# # 找不到会抛出异常。与find(sub[,start[,end]])类似，找不到返回-1.
# str2 = "Welcome hyp"
# print(str2.index("lc"))
# print(str2.index("lc",2,6))
# print(str2.find("lc",1,6))
# print(str2.find("lc",2,6))
#
# # 4、join() : 连接字符串
# str3 = '-'.join(['hyp','lcy','abc'])
# print(str3)
#
# # 5、replace(old,new[,count]) : 替换指定的字符串
# str4 = "hello hyp"
# print(str4.replace("hyp","lcy"))
#
# # 6、split(): 用于拆分字符串
# str5 = "h_y_p_l"
# print(str5.split('_'))
#
# # 7、capitalize(): 首字母大写
# str6 = "hyp"
# print(str6.capitalize())
#
# # 8、center(): 设置宽度，并将内容居中
# str7 = "hyp"
# print(str7.center(20))
# print(str7.center(20,"-"))
#
# # 9、startswith,endswith  以什么开头、结尾
# str8 = "hyplcy"
# print(str8.startswith("hy"))
# print(str8.endswith("cy"))
#
# # 10、format(): 格式化，将格式化的占位符替换为指定的值
# str9 = 'I am {name} ,{age}'
# print(str9.format(name = 'hyp',age = '18'))
#
# # 11、isnumeric、 isdigit、upper ......

