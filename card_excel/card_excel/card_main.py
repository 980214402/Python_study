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
import card_tools


def card(filename, sheet):

    card_tools.card_excel_open(filename, sheet)
    # card_tools.card_excel_delete(filename, sheet, 1, max_row)
    # 直接删除会导致文件中没有记录，如果用户不正常退出会丢失数据
    while True:

        card_tools.card_menu()

        user_use = input("请选择需要的操作：")

        if user_use in ['1', '2', '3']:
            print("你选择的操作 {}".format(user_use))
            if user_use == '1':
                card_tools.card_add()
                card_tools.card_excel_rewrite(filename, sheet, card_tools.card_list) # 修改card后，对文件进行删除重写
            elif user_use == '2':
                card_tools.card_show()

            elif user_use == '3':
                card_tools.card_search()
                card_tools.card_excel_rewrite(filename, sheet, card_tools.card_list)
        elif user_use == '0':
            print("你选择的操作是 {}".format(user_use))
            print('欢迎再次使用 【名片管理系统 Excel】')
            break
        else:
            print('输入错误，请重新选择操作')


# 调用名片
card('card_file.xlsx', 'Sheet1')