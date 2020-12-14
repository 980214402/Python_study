# 名片管理系统 练习
import cards_tools


while True:

    cards_tools.card_menu()

    user_use = input("请输入希望执行的操作：")
    print("您选择的操作是 %s" % user_use)
    print("-" * 30)

    # 1、2、3 是对名片的操作
    if user_use in ["1", "2", "3"]:
        if user_use == "1":
            cards_tools.card_add()
        elif user_use == "2":
            cards_tools.card_show()
        elif user_use == "3":
            cards_tools.card_search()
    # 选择 0 退出系统
    elif user_use == "0":
        print("欢迎再次使用【名片管理系统】")

        break
    # 其他选择就返回，再次提示用户选择
    else:
        print("输入有误，请重新选择")

