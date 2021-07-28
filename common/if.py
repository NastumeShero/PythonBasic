# coding:utf-8
'''
	用法:
	if bool_result：  bool_result为条件判断语句，为true执行do，为false，跳过do执行后面的代码
		do
'''
# 条件判断语句 可以是一个表达式或者多个表达式用or或and来连接
info = 'my name is xiaomu , i love python'
info_list = info.split()
if 'xiaomu' in info and len(info) < 15:
    info_list[0] = 'her'

if 'xiaomu' in info or len(info) < 15:
    print(' '.join(info_list))

'''
 if condition : do
 else:  do
'''
url = 'https://www.baidu.com'
if 'baidu' in url:
    print('欢迎访问百度')
else:
    print('请前往百度访问')

if 'taobao' in url:
    _url = 'www.taobao.com'
else:
    _url = None
print('_url is %s' % _url)

'''
 if conditon:
 elif conditon:
 else:

'''
# 出现重名，更改新的名称
users = [
    ('dewei', 33, 90), ('xiaomu', 20, 99), ('xiaoming', 23, 100)
]
xiaoming = ['xiaoming', 21, 99]

if users[0][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
elif users[1][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
elif users[2][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
else:
    users.append(xiaoming)
print(users)

