# import keyword
# print(keyword.kwlist)

# a = 'hello python'
# print(len(a))
# print(a[::])
# print(a[1:len(a):2])

# name = 'a'
# sex = 'b'
# hobby = 'like python'
# print(""" --- %s基本信息 ---
#     name: %s
#     sex: %s
#     hobby: %s""" % (name, name, sex, hobby))

# list1 = []
# list2 = [1, 2, 3.14, True, '简单', [1, 2, 3]]
# print(list2[5][2])
# list2.append('板凳')
# list2.insert(4, 'lucky')
# list2.pop()
# list2.remove(2)
# list2[0] = '苗'
# list2.append('苗')
#
# print(list2.count('苗'))
#
# print(list2)

# tuple1 = ()
# tuple1[0] = '10'
# print(tuple1


# dict1_info = {'name': '梨子', 'age': 18}
# print(dict1_info)
# print(dict1_info['name'])
# print(dict1_info.get('name'))
# # print(dict1_info.items())
# # # a = dict1_info.items()
# # print("a: %s" % dict1_info.items())
# dict1_info['name'] = 'Lynn'
# dict1_info['weight'] = 45
# dict1_info.pop('age')
#
#
# print(dict1_info)

def good_job(salary, bonus, subsidy=500, *args, **kwargs):
    print('salary: {}'.format(salary))
    print('bonus: {}'.format(bonus))
    print('subsidy: {}'.format(subsidy))
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))

a = good_job(11, 22, 33, 44, 55, a=11, b=22)
print(a)