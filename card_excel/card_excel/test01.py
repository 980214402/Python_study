

import openpyxl

wb = openpyxl.load_workbook('card_file.xlsx')
sheet = wb['Sheet1']
max_row = sheet.max_row

print(max_row)