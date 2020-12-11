
# 定义一个列表来存放名片 card_list
card_list = []

# 菜单界面
def card_menu():
    print("*" * 30)
    print("欢迎使用【名片管理系统】 V 1.0")

    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")

    print("0. 退出系统")
    print("*" * 30)

# 1、增加名片
def card_add():
    print("新增名片")
    # 定义一个字典来存放用户输入的数据，card_dict
    # card_dict = {'name':'','phone':'','qq':'','email':''}
    # card_dict['name'] = input("请输入姓名：")
    # card_dict['phone'] = input("请输入电话：")
    # card_dict['qq'] = input("请输入QQ:")
    # card_dict['email'] = input("请输入邮箱:")
    # 修改
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    card_dict = {'Name':name,
                 'Phone':phone,
                 'QQ':qq,
                 'Email':email}
    card_list.append(card_dict)
    print(card_list)
    print("添加 %s 的名片成功" % card_dict['Name'])

# 2、显示全部
def card_show():
    print("显示全部名片")
    # print("姓名 电话 QQ 邮箱")
    for name in ['姓名', '电话', 'QQ', 'Email']:
        print("%s\t\t" % name, end='')
    print('')

    # for card in card_list:
    #     print(card)

    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card['Name'],
                                        card['Phone'],
                                        card['QQ'],
                                        card['Email']), end='')
        print("")


# 3、搜索名片
def card_search():
    print("搜索名片")

    card_name = input("请输入想要搜索的姓名：")
    for name in ['姓名', '电话', 'QQ', 'Email']:
        print("%s\t\t" % name, end='')
    print('')

    for card in card_list:
        if card_name == card['Name']:
            print("%s\t\t%s\t\t%s\t\t%s" % (card['Name'],
                                            card['Phone'],
                                            card['QQ'],
                                            card['Email']), end='')
            print("")



