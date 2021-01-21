# import json
#
# dict = {"Name": 1, "QQ": 9}
# json_str = json.dumps(dict)
# with open('1.txt', 'w') as f:
#     f.write(json_str)

"""
典型的应用场景：Json数据的解析

>>> user
"{'name' : 'jim', 'sex' : 'male', 'age': 18}"
>>> b=eval(user)
>>> b
{'age': 18, 'name': 'jim', 'sex': 'male'}
>>> exec("c="+user)
>>> c
{'age': 18, 'name': 'jim', 'sex': 'male'}
"""

# 打开文件
file = open("1.txt")
# 读取文件
text = eval(file.read())
if len(text) > 0:
    print(text)
else:
    print("没有内容")

print(type(text))
# 关闭文件
file.close()