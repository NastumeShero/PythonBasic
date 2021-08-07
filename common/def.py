# coding:utf8
'''
    定义函数，传入默认参数
    a 为必传参数，且a必须赋值
    b 为默认参数，不赋值时，b默认为1
'''
def add(a,b=1):
	print('{}+{}={}'.format(a,b,a+b))

# 调用函数
add(2)   # 2+1=3
add(2,6) # 2+6=8
add(b=2,a=4)

'''
    定义函数，传入可变参数
    *args代表可变元组参数：将无参数名的值，包起来封装成一个元组
'''
def a_test(a,b=1,*args):
    print(a,b,args)

# 调用函数
a_test(1,2,3)

'''
    定义函数，传入可变参数
    **kwargs 代表可变字典参数 ：将入参里面的key=value，包装成键值对，封装成一个字典
'''
def b_test(a,b=1,**kwargs):
    print(a,b,kwargs)

# 调用函数
b_test(1,2,c=2,name='test')
# b_test(1,2,b=2,name='test')  # 参数b有多个不同的值（TypeError: b_test() got multiple values for argument 'b'）

'''
    定义函数，入参的定义顺序
    参数定义顺序，从左到右依次是：必传参数，默认参数，可变元组参数，可变字典参数
'''
def c_test(a,b=1,*args,**kwargs):
    print(a,b)
    if len(args) >= 1:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print(args,len(args))
    print(kwargs,len(kwargs))

# 调用函数
c_test(1,3,4,5,name='xiao')
a = ('python','java')
b = {'name':'test'}
c_test(1,3,*a,**b)

'''
    定义函数时，可指定变量的类型；
    但函数调用时，不会去校验传入的参数类型与定义的类型是否一致
'''
def person(name:str,age:int = 18):
    print(name,age)

# 调用函数
person(0,'20')  # 函数能正常调用，不会去校验类型

'''
    定义函数，在函数中定义全局变量
    一般不建议在函数中通过global定义全局变量
    注意：
        - 使用不当，递归函数容易导致内存溢出
        - 要避免滥用递归
'''
count = 0
def e_test():
    global count
    count +=1
    if count !=5:
        print('count条件不满足，我要重新执行，当前count为{}'.format(count))
        # 返回函数本身，表示再次调用该函数，也称为递归调用
        return e_test()
    else:
        print('count is %s' % count)

# 调用函数
e_test()

'''
    定义lambda函数
    一般用于：定义一个轻量化的函数，即用即删除
    - 无参数的lambda函数语法：
        lambda:value
    - 有参数的lambda函数语法：
        lambda x,y:x*y  # x和y，是函数的入参；x*y是函数的返回
'''
# 定义无参数的函数
f = lambda : print(1)
f()
# 定义有参数的函数
f1 = lambda x,y: print(x+y)
f1(3,4)

users = [
    {'name':'xiao'},
    {'name':'test'},
    {'name':'alice'},
]
# 定义lambda函数，x为入参，返回x['name']的值
users.sort(key=lambda x:x['name'])
print(users)

