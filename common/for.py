'''
用法：
	for item in iterable:  # for循环语句块
		print(item)		  # 每次循环对应的代码块
解析：
	iteable  ：可循环的数据类型，如列表，元组，字符串，字典
	item： iterable中的每一个元素
'''
# 遍历list
users_list = ['xiaomu','xioaming','xiaohua']
for name in users_list:
    print(name)

# 遍历字符串
for i in 'python':
    print(i)

# 遍历元组
users_tuple = ('xiaohong','xiaomu','xioaming','xiaohua')
for name in users_tuple:
    if name == 'xiaomu':
        print("你好，xiaomu")
    else:
        print("欢迎{}学习python".format(name))

# 遍历字典
users_dict = {'name':'xiaoming','age':33}
for i in users_dict:
    print(i,users_dict[i])

# 字典利用items函数进行for循环
'''
用法：
    for key,value in dict.items():
        print(key,value)
    key： for循环体中获取的字典当前元素的key
    value： for循环体重对应当前key的value值
    dict.items() 返回一个伪列表
'''
users_dict = {'name':'xiaoming','age':33}
items = users_dict.items()  # 获取字典中每一个键值对的信息，返回一个伪列表
print(items,type(items))
for key,value in users_dict.items():
    print(key,value)


users_dict_list = [
    {'name':'xioamu'},{'name':'xiaohong'}
]
for user in users_dict_list:
    print(user)
    print(user.get('name'))

'''
用法：
	for item in range(start,stop,step=1):
		print(item)
	start：开始的数字
	stop：结束的数字或位置
	step：步长
'''
l = range(6)
print(l,type(l))
for i in l:
    print(i)
else:
	print('for循环结束')

'''
用法：
	for item in iterable:
		do
	else:
		elsedo
'''
l = range(6)
print(l,type(l))
for i in l:
    print(i)
    # 3/i    # 执行该行代码时，报错了，则不执行else中的语句
else:
	print('for循环结束')

# 嵌套for循环
a = 10
b = 20
for i in range(a):
    for j in range(b):
        print(i,j)
        print("{}+{}={}".format(i,j,i+j))
        print('======')