# 名片管理系统 练习


while True:

    # todo (小明) 功能菜单

    user_use = input("请输入需要选择的操作：")
    print("您选择的操作是 %s" % user_use)

    # 1、2、3 是对名片的操作
    if user_use in [1, 2, 3]:
        pass
    # 选择 0 退出系统
    elif user_use == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他选择就返回，再次提示用户选择
    else:
        print("输入有误，请重新选择")

