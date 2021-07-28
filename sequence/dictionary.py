# coding:utf8
dict_info = {'id': 1, 'name': 'xiao', 'city': 'wuhan'}
dict_keys = dict_info.keys()   # 伪列表,不转换为列表时，无法使用list的方法
dict_values = dict_info.values()
print(dict_keys, type(dict_keys))
print(dict_values, type(dict_values))
dict_keys = list(dict_keys)  # dict_keys没有转换为list，无法使用list的方法
dict_keys.append('top')  # AttributeError: 'dict_keys' object has no attribute 'append'
print(dict_keys)

'''
	dict.items()  获取字典中所有的key-value
		返回一个伪列表，要使用列表的功能，需要转换为list
'''
dict_info={'id':1,'name':'xiao','city':'wuhan'}
items = dict_info.items()
items_list = list(items)
for i in range(len(items_list)):
    key = items_list[i][0]
    value = items_list[i][1]
    print(key,value)

'''
	1.通过[]获取key的value，若key不存在，则直接报错
		dict[key]
	2.通过get方法获取key的value值,若key不存在，返回默认值
		dict.get(key,default=None)
		a.通过get方法调用时，没有设置default的值，默认为None，
		b.get方法中设置default为某个值后，若key不存在，则返回设置的值；若key存在，则返回字典中定义的value
'''
user_info = {'id': 1, 'username': 'xiao', 'password': 'abcdef', 'created_time': '2021-06-24'}
values = []
id = user_info['id']
username = user_info.get('username')
values.append(id)
values.append(username)
print(values)
# test = user_info['test']  # 获取的key不存在，报错KeyError: 'test'
# values.append(test)
# 获取的key不存在时，默认返回None
test = user_info.get('test')
values.append(test)
# 获取的key在字段中存在时，设置了默认值不会生效
created_time = user_info.get('created_time','2022-01-01')
values.append(created_time)
print(values)

'''
	通过[]来定义字典的内容时：
	添加或修改字典，根据key在字典中是否存在
	若key不存在，则添加一个key-value
	若key存在，则修改key的value
'''
dict_info = {}
dict_info['id'] = 11
dict_info['name'] = 'xiao'
print(dict_info)

'''
update的用法：dict.update(new_dict)
 该函数函数无返回值
 new_dict 为新的字典
'''
new_dict = {'age': '30'}
dict_info.update({'top': '160'})
print(dict_info)
dict_info.update(new_dict)
print(dict_info)

'''
setdefault的用法：dict.setdefault(key,value)
	key 表示 需要获取的key
	value 表示 当key不存在时，对应这个key则存入字典的默认值
	当key在字典中存在时，设置的value不生效
	当key在字典中不存在时，设置key的值为value
'''
dict_info.setdefault('job', 'teacher')
dict_info.setdefault('id', 22)
print(dict_info)


'''
	用法：dict.pop(key) 删除字典中指定的key，并返回key对应的value值
		key为 需要删掉的key
		若key存在，返回key对应的value；
'''
my_dict = {'id':1,'name':'test'}
name = my_dict.pop('name')  # 删除字典中key为name的键值对，并返回name对应的value
print(my_dict)
print(name)
# my_dict.pop('12')  # 报错KeyError: '12'


my_dict = {'id':12,'name':'tester'}
del my_dict['name']
print(my_dict)  # 返回{'id':1}
del my_dict  # 删除my_dict这个字典，内存中已删除
# print(my_dict) # 报错，NameError: name 'my_dict' is not defined

# 示例
projects={
    'ipad':{'name':'ipad','price':2200,'desc':'平板电脑'},
    'iphone':{'name':'iphone','price':4700,'desc':'手机'},
    'pc':{'name':'pc','price':5200,'desc':'台式电脑'},
    'mac':{'name':'mac','price':8000,'desc':'笔记本电脑'}
}
# 当前店铺存在的商品信息
keys = projects.keys()
print('当前的商品信息有{}'.format(keys))
# 客户A购买了一个ipad
print('客户A购买了{}，花费了{}元'.format(projects['ipad']['name'],projects['ipad']['price']))
projects.pop('ipad')
print('当前的商品信息有{}'.format(projects.keys()))
# 客户B购买了一个mac
result = projects.pop('mac')
print('客户B购买了{}，花费了{}元'.format(result.get('name'),result.get('price')))
print('当前的商品信息有{}'.format(projects.keys()))
# 客户C购买了一个pc和iphone
print('客户C购买了{}和{}，花费了{}元'.format(
    projects['iphone']['name'],projects['pc']['name'],
    projects.values()[0]['price']+projects.values()[1]['price'])
)
projects.clear() # 清空商品
print('当前的商品信息有{}'.format(projects.keys()))
# 商店出售，删除变量
del projects

fruits={
    'apple':30,
    'banana':40,
    'pear':50
}
# 进货
real_fruits = fruits.copy()
print(real_fruits)
real_fruits['orange']=40
real_fruits.update({'cherry':100})
print(real_fruits)

# 卖货
real_fruits['apple']= real_fruits['apple'] - 5
print(real_fruits)
real_fruits['cherry'] -= 10
print(real_fruits)



default_dict = { 'a':None,'b':1,'c':0,'d':''}
print('a' in default_dict)
print(bool(default_dict['a']))

students = {
    'dewei':'到','xiaomu':'在','xiaoyun':'嗯','xiaogao':'在呢'
}
print('xiaogao在吗')
xiaogao=students.popitem()
print(type(xiaogao))
print('{} 喊 {}'.format(xiaogao[0],xiaogao[1]))
print(students)
students.clear()
print('students被清空后：{}'.format(students))
students.popitem()  # KeyError: 'popitem(): dictionary is empty'