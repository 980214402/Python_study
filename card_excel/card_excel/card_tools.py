import openpyxl

card_list = []   # 空列表

def card_menu():
    print('*' * 30)
    print('欢迎使用【名片管理系统 Excel】 V1.0')
    print()
    print('1. 新增名片')
    print('2. 显示全部名片')
    print('3. 搜索名片')
    print()
    print('0. 退出系统')
    print('*' * 30)



def card_add(filename, sheet):
    max_row = card_excel_open(filename, sheet)
    print("请按提示输入内容：")
    card_id = max_row
    card_name = input('请输入姓名: ')
    card_phone = input('请输入电话号码: ')
    card_QQ = input('请输入QQ: ')
    card_Email = input('请输入邮箱: ')
    card_user_info = {'id': card_id,
                          'name': card_name,
                          'phone': card_phone,
                          'QQ': card_QQ,
                          'Email': card_Email}
    card_list.append(card_user_info)
    card_user_info = str(card_user_info)
    card_excel_write(filename, sheet, max_row, 1, card_user_info)



def card_show(filename, sheet):
    card_excel_open(filename, sheet)
    if  len(card_list) == 0:
        print("没有存储名片 请使用新增功能")
    else:
        print('编号\t\t姓名\t\t电话\t\tQQ\t\t邮箱')
        for card_dict in card_list:
            print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(card_dict['id']),
                                                    card_dict['name'],
                                                    card_dict['phone'],
                                                    card_dict['QQ'],
                                                    card_dict['Email'])


def card_search():
    pass


def card_excel_open(filename, sheet):
    wb = openpyxl.load_workbook(filename)  # 加载excel文件
    sheet = wb[sheet]   # 找到表单
    max_row = sheet.max_row  # 获取最大行数
    for i in range(1, max_row):
        cell = sheet.cell(row=i, column=1).value  # 接收单元格的字典内容
        cell = eval(cell)
        card_list.append(cell)
    return max_row

def card_excel_write(filename, sheet, row, column, write):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet]
    # max_row = sheet.max_row
    sheet.cell(row, column).value = write  # 找到特定单元格，进行写入
    wb.save(filename)   # 保存excel

