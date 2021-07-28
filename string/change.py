# coding:utf-8
# 数字类型转换为字符串类型
int_data = 12
float_data = 3.14

str_int_data = str(int_data)
str_float_data = str(float_data)
print(str_int_data,type(str_int_data),str_float_data,type(str_float_data))

zero_number = 0
_number = -1

str_zero_number = str(zero_number)
str_number = str(_number)

print(str_zero_number,type(str_zero_number),str_number,type(str_number))

# 字符串转成数字类型（int或float）

int_data_str = int('1234')
float_data_str = float('3.14')
print(int_data_str,type(int_data_str),float_data_str,type(float_data_str))

mix_str = '123a'
# print(float(mix_str))  # ValueError: could not convert string to float: '123a'
float_data_str = '3.14'
test_data = float(float_data_str)



'''
	用法：string.split(sep=None,maxSplit=-1)
		sep： 切割的规则符号，不填写，默认为空格，如字符串无空格则不分割生成列表
		maxSplit：根据切割符号切割的次数，默认为-1，表示不限制
		返回值： 返回一个list
'''
a = 'abc'
print(a.split())
b = 'a b c'
print(b.split()) # ['a', 'b', 'c']
c = 'a,b,c,dd'
print(c.split(',')) # ['a', 'b', 'c', 'dd']
print(c.split(',',1))  # ['a', 'b,c,dd']


a = [1,2,3]
b = (1,2,3)
c = {1,2,3}
print(tuple(a),set(a))
print(type(tuple(a)),type(set(a)))
print(tuple(a) is b) # 对应的内存地址不同，则返回false
print(set(a) is c) # 对应的内存地址不同，返回false

print(list(b),set(b))
print(list(c),tuple(c))

print(list(a))

print(str(a),type(str(a)))
print(str(b),type(str(b)))
print(str(c),type(str(c)))

print(list(str(a)))