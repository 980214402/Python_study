"""
文件名：
    cards_main.py  主文件
    cards_tolls.py  操作文件
使用的变量名：
    user_use: 用户操作
    card_list: 空列表
    card_dict: 空字典

   card_menu():显示界面
   card_add(): 名片增加
   card_show(): 名片显示
   card_search(): 名片搜索
   card_find_dealO(): 处理查询的名片
   card_input_info(): 处理输入的名片信息

"""


while True:

    user_use = input("请选择需要的操作：")

    if  user_use in ['1', '2', '3']:
        print("你选择的操作 {}".format(user_use))
    elif user_use == '0':
        print("你选择的操作是 {}".format(user_use))
        print('欢迎再次使用 本程序')
        break
    else:
        print('输入错误，请重新选择操作')

