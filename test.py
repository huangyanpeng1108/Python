names=[]
phones=[]
while True:
    print("============通讯录管理系统===============")
    print("1、增加姓名和手机号")
    print("2、删除姓名")
    print("3、修改手机号")
    print("4、查询所有用户")
    print("5、根据姓名查找手机号")
    print("6、退出")
    print("===========================================")
    tag=int(input("请选择："))
    if tag==1:
        name = input("请输入姓名")
        names.append(name)
        phone = input("请输入手机号")
        phones.append(phone)
    elif tag==2:
        name = input("请输入姓名")
        if name in names:
            phones.pop(names.index(name))
            names.remove(name)
        else:
            print("姓名不存在")
    elif tag==3:
        name = input("请输入姓名：")
        phone = input("请输入要修改的手机号")
        index = names.index(name)
        phones[index]=phone
    elif tag==4:
        for i in names:
            print(i)
    elif tag==5:
        name = input("请输入姓名")
        print(phones[names.index(name)])
    else:
        break