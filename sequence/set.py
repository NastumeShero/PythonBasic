# coding:utf8
'''
    通过set()函数来定义一个集合
    集合是无序的，且不存在重复元素的
'''
a = set()   # 定义一个空的集合
print(a,type(a))
b = set(['python','django','java'])  # 定义一个集合
print(b)

'''
    通过{}来定义集合时，不能定义空的集合，不能将可变的数据类型传入，如list和字典
    定义集合时，若存在相同的元素，则集合中只展示一个
'''
# d = {[a,b,c]}  # TypeError: unhashable type: 'list'
# e = {{'a':1,'c':2}}  # TypeError: unhashable type: 'dict'
c = {(0,12,4)}
print(c,type(c))
# 定义集合时，存在相同元素
c1 = {'a','b','c','b'}
print(c1,type(c1))  # (set(['a', 'c', 'b']), <type 'set'>)
number_list = [1,2,3,4,3,2]
print(number_list) # 显示列表的内容
print(set(number_list))  # 将list转为set


# 给集合添加元素
'''
    用法：set.add(item)
        item 为要添加的元素
'''
a_list = ['python', 'django', 'java', 'python','Soft']
a_set = set()
for i in range(len(a_list)):
    a_set.add(a_list[i])
print(a_set)
a_set.add(True)
a_set.add(None)
a_set.add('test')
print(a_set)

'''
	用法：set.update(iterable)
		iterable:代表集合，列表，元组，字符串等可以迭代的对象
		该函数无返回值，直接作用于原集合
'''
a_tuple = ('a','b','c')
a_set.update(a_tuple)
print(a_set)
a_set.update('abdef')
print(a_set)
a_set.update('python')
print(a_set)

'''
    用法：set.remove(item) 
        item ：需要删除的元素
        无返回值，直接作用于原集合
'''
a_set.remove('test')
print(a_set)
# list = ['python','java']
# a_set.remove(list)  # 集合只能移除元素
# print(a_set)
'''
    用法： set.clear() 清空集合中的元素
'''
a_set.clear()
print(a_set)
# a_set.remove('python')  # 报错：KeyError: 'python'

'''
    del a_set
    del删除集合对象
'''
del a_set
'''
    用法：a_set.difference(b_set)
        b_set为当前集合需要对比的集合
'''
dirvers = ['dewei','xiaomu','xiaoming']
testers = ['xiaomu','xiaoman','xiaogang','xiaogang']
driver_set = set(dirvers)
tester_set = set(testers)

sample_drivers = driver_set.difference(tester_set)
# sample_drivers = driver_set.difference(testers)
print(sample_drivers)


'''
	用法：a_set.intersection(b_set)
		b_set ： 与当前集合对比的一个或多个集合
		返回值：返回原始集合与对比集合的交集
'''
a_list = ['name','xiaomu','xiaoming']
b_list = ['xiaoming','xiaohong','xiaofang ']
c_list = ['xiaohua','xiaobing','xiaoming']
a_set = set(a_list)
b_set = set(b_list)
c_set = set(c_list)
result = a_set.intersection(b_set,c_set)
# result = a_set.intersection(b_list,c_list)
print(result)
xiaotou = list(result)
print('{}是小偷'.format(xiaotou[0]))

'''
    用法：a_set.union(b_set...)
        b_set...: 与当前集合对比的1个或多个集合
        返回值：返回原始集合与对比集合的并集
'''
a_school = ['周五半天假','免费周末培训','周五休息']
b_school = ['放学时间提前','作业少点','饮食改善']
c_school = ['作业少点','周五半天假','座椅改善']

a_set = set(a_school)
b_set = set(b_school)
c_set = set(c_school)
help_data = a_set.union(b_set,c_set)
# help_data = a_set.union(b_school,c_school)
help_data.union()
print(help_data)

'''
	用法：a_set.isdisjoint(b_set) a_set中包含b_set的元素，则返回false，否则返回True
		b_set: 与当前集合来对比的集合
'''
company_not_allow = {'女','喝酒','抽烟','睡懒觉'}
one_player={'男','跑步','喝酒'}
two_player={'女','生活规律','跆拳道'}
three_player={'男','太极拳','年轻'}

print(company_not_allow.isdisjoint(one_player))
print(company_not_allow.isdisjoint(two_player))
print(company_not_allow.isdisjoint(three_player))
