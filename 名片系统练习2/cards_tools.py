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
    card_dict = {'Name': name,
                 'Phone': phone,
                 'QQ': qq,
                 'Email': email}
    card_list.append(card_dict)

    # 调用file_read方法，把新建的名片添加到文件中
    file_read(card_list)

    print(card_list)
    print("添加 %s 的名片成功" % card_dict['Name'])


# 2、显示全部
def card_show():

    print("显示全部名片")
    # print("姓名 电话 QQ 邮箱")

    if len(card_list) == 0:
        print("当前名片管理系统中没有名片存在，请使用名片新增功能进行添加。")

        return

    for name in ['姓名', '电话', 'QQ', 'Email']:
        # print("%s\t\t" % name, end='')  修改
        print(name, end='\t\t')
    print('')

    # for card in card_list:
    #     print(card)

    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card['Name'],
                                        card['Phone'],
                                        card['QQ'],
                                        card['Email']))


# 3、搜索名片
def card_search():
    print("搜索名片")

    card_name = input("请输入想要搜索的姓名：")
    # for name in ['姓名', '电话', 'QQ', 'Email']:
    #     print("%s\t\t" % name, end='')
    # print('')

    for card_find in card_list:
        if card_find['Name'] == card_name:
            print("姓名\t\t电话\t\tQQ\t\tEmail")
            print("=" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_find['Name'],
                                            card_find['Phone'],
                                            card_find['QQ'],
                                            card_find['Email']))

            # 处理查询到的名片
            card_deal_find(card_find)

            break
    else:
        print("没有找到您想要的名片")


# 处理查询到的名片
def card_deal_find(card_find):
    """处理查询到的名片

    :param card_find: 查询到的名片
    :return:
    """

    print(card_find)

    card_use = input("请选择要执行的操作 [1]修改 [2]删除 [0]返回上级")

    if card_use == '1':
        # card_find['Name'] = input("请输入姓名：")
        # card_find['Phone'] = input("请输入电话：")
        # card_find['QQ'] = input("请输入QQ：")
        # card_find['Email'] = input("请输入邮箱：")
        card_find['Name'] = card_input_info(card_find['Name'], "姓名：")
        card_find['Phone'] = card_input_info(card_find['Phone'], "电话：")
        card_find['QQ'] = card_input_info(card_find['QQ'], "QQ：")
        card_find['Email'] = card_input_info(card_find['Email'], "邮箱：")
    elif card_use == '2':
        card_list.remove(card_find)
        print("已删除 %s 的名片" % card_find['Name'])

    # 调用file_read方法，把处理后的数据写入文件
    file_read(card_list)


def card_input_info(find_value, tooltips):

    # 提示用户输入信息
    user_info = input(tooltips)

    # 判断用户是否输入信息，用户输入信息进行替换
    if len(user_info) > 0:
        return user_info

    # 用户没有输入信息，返回原值
    else:
        return find_value


# 把文件内的字典，添加到列表里
def file_open(list_input, file='1.txt'):
    """打开文件，读取字典，添加到列表里面

    :param list_input: 传入列表名
    :param file: 传入打开文件
    :return:
    """
    # 打开文件
    file_txt = open(file, 'r')

    while True:

        text_str = file_txt.readline()
        # 判断是否读到内容
        if not text_str:
            break

        # 读取一行内容 并转换为字典
        text_dict = eval(text_str)

        # 把读取到的字典添加到card_list列表中
        list_input.append(text_dict)

        # 每读取一行的末尾已经有了一个 `\n`
        # print(text, end="")

    # 关闭文件
    file_txt.close()
    return list_input


# 把字典添加到文件里
def file_read(list_input, file='1.txt'):
    """

    :param list_input: 列表数据
    :param file: 操作的文件
    :return: 无
    """

    # 打开文件
    file_txt = open(file, 'w')

    for card_dict in list_input:
        file_txt.write(str(card_dict) + "\n")
    # else:
    #     print("没有数据")

    # 关闭文件
    file_txt.close()


card_list = file_open(card_list)





