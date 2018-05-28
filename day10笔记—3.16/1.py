# 输出 1 — 100的所有奇数：
# n = 1
# while n < 101:
#     if  n % 2 == 1:
#         print(n,end=",")
#     else:
#         pass
#     n = n + 1


# 输出 1 — 100的所有偶数：
# n = 1
# while n < 101:
#     if  n % 2 == 0:
#         print(n,end=",")
#     else:
#         pass
#     n = n + 1


# 求1—100的所有数的和：
# n = 1
# sum = 0
# while n < 101:
#     sum = sum + n
#     n = n + 1
# print(sum)


# 使用while循环输出 1 2 3 4 5 6   8 9 10
# n = 1
# while n < 11:
#     if n == 7:
#         pass
#     else:
#         print(n,end=" ")
#     n = n + 1


# 求1-2+3-4+5...99的所有数的和：
# n = 1
# sum = 0
# while n < 100:
#     if n % 2 == 1:
#         sum = sum + n
#         n = n + 1
#     else:
#         sum = sum - n
#         n = n + 1
# print(sum)


# 用户登录（三次机会重试）
# n = 0
# zh = "hyp"
# mn = "123456"
# while n < 3:
#         # if n == 3:
#         #     print("账户已锁定！")
#         # else:
#         #     pass
#         inp = input(">>>:用户名")
#         inu = input(">>>:密码")
#         if zh == inp and mn == inu:
#             print("登录成功，欢迎使用！")
#             break
#         else:
#             print("用户名或密码错误，请重新输入！")
#             n = n + 1


# int 将字符串转换为数字：
# a = "123"
# b = int(a)
# print(type(b),b)

# base = 16  ---> 代表16进制
# num = "b"
# v = int(num,base=16)
# print(v)

# 这个数字的二进制至少用几位来表示：
# age = 3
# r = age.bit_length()
# print(r)


# 字符串：
# 首字母大写：
#test = "hyp"
# v = test.capitalize()
# print(v)

# 所有字母全变小写： casefold更牛逼，很多未知的对象变小写
# v1 = test.casefold()
# print(v1)
#
# test1 = "HYp"
# v2 = test1.lower()
# print(v2)

# 设置宽度，并将内容居中，前后各有10个*，（只能添加一个字符，例：99就不可以）
# test = "hyp"
# v3 = test.center(20,"*")
# print(v3)

# 计算f在字符串中出现了几次，从第5个字符开始
# test1 = "hypffg"
# v4 = test.count('f',5)
# print(v4)

# 以什么什么结尾；以什么什么开始
# test5 = "hypffr"
# c = test5.endswith('f')
# x = test5.startswith('h')
# print(c,x)

#
# test6 = "12345678\t9"
# z = test6.expandtabs(6)
# print(z,len(z))

# 从开始往后找，找到第一个之后，获取其未知
# test7 = "hyphyp"
# z1 = test7.find('yp',2)
# print(z1)

# 格式化，将一个字符串中的占位符替换为指定的值
# test8 = 'I am {name},age {r}'
# a = test8.format(name = 'hyp',r = 24)
# print(a)
#
# test8 = 'I am {0},age {1}'
# a = test8.format('hyp',24)
# print(a)
#
#
# test8 = 'I am {name},age {r}'
# a = test8.format_map({'name':'hyp','r':24})
# print(a)
#
# # 判断字符串中是否只含有 字母和数字
# test9 = "frehbgr54+"
# v = test9.isalnum()
# print(v)









