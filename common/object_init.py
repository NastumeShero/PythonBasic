'''
    - 什么是面向对象
    - 面向对象的定义与使用方法
    - 装饰器与类的装饰器
    - 私有函数与私有变量

'''
'''
    面向对象编程：利用对象去进行编程的过程（面向对象的属性和方法来进行编程）
    自定义对象数据类型就是面向对象中的类的概念
    类变量（对象的属性）
    类方法（对象的方法）
    类的名称定义：每个单词的首字母大写（驼峰式）
'''
# object类的通用对象
class Person(object):
    # 定义类变量（局部变量）
    name = None
    age = None


    # 定义类方法
    def run(self):
        print(f'{self.name} is dumping')

    def jump(self):
        print(f'{self.name} 在跳跃')
    # 局部函数
    def work(self):
        self.run()
        self.jump()
        def sleep(name):
            return name
        result = sleep(self.name)
        print('sleep result is ',result)



# 实例化Person对象
xiaomu = Person()
xiaomu.name = 'xiaomu'
print(xiaomu.name)
xiaomu.jump()
xiaomu.work()

# 每个实例化对象的属性值不同
# 实例化person对象
dewei = Person()
dewei.name = 'dewei'
# 实例化对象可以定义自己的属性
dewei.top = 174
dewei.jump()
print(f'dewei is {dewei.top}')

# 定义一个类
class Person1(object):

    # 定义构造函数：在实例化时需要传参
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    # 定义局部函数
    def run(self):
        print(f'{self.name} is running')

# 实例化对象
xiaosu = Person1(name='xiaosu',age=18)
xiaosu.run()

# 对象的生命周期
'''
init一个对象时，是一个对象生命的开始   ===》 内存中分配一个内存块

每个对象有一个内置函数__del__:删除对象 ===》 从内存中释放内存块
'''

'''
    私有函数与私有变量(独自拥有的，无法通过实例化对象来调用)
        - 无法被实例化后的对象调用的类中的函数与变量
        - 类内部可以调用私有函数与变量
        - 只希望类内部业务调用使用，不希望被使用者调用
    定义方法：
        在变量或函数名前添加__(两个下横线)
    
    pass 关键字，可以运用在类或函数中，当定义类或函数之后，还不确定类或函数的实现，可以使用pass
'''
class Cat(object):
    # 定义私有变量
    __cat_type = 'cat'

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def run(self):
        result = self.__run()
        print(result)
    # 定义私有函数
    def __run(self):
        return f'{self.__age}岁的{self.__cat_type},{self.name} 在奔跑'

    def dump(self):
        result = self.__dump()
        print(result)
    # 定义私有函数
    def __dump(self):
        return f'{self.__age}岁的{self.__cat_type},{self.name} 在跳跃'

cat = Cat(name='xiaomi',age=3)
cat.run()
cat.dump()

# 实例化无法调用私有函数与变量
# print(cat.__cat_type)  # AttributeError: 'Cat' object has no attribute '__cat_type'
# print(cat.__run())  # AttributeError: 'Cat' object has no attribute '__run'

# dir(object)方法： 查看该对象的函数与变量
print(dir(cat))

# 通过类名加私有变量或函数的名称，可以访问私有变量与函数，但一般不建议这么做
print(cat._Cat__cat_type)
print(cat._Cat__run())

'''
    封装
    定义： 将不对外的私有属性或方法通过可对外使用的函数而使用
    目的： 保护隐私，明确区分内外
    
    装饰器
    - 什么是装饰器
        装饰器是一种函数
        可以接受函数作为参数
        可以返回函数
        接收一个函数，内部对其处理，然后返回一个新函数，动态的增强函数功能
        将c函数在a函数执行，在a函数中可以选择执行或不执行c函数，也可以对c函数的结果进行二次加工处理
    - 如何使用装饰器
        将被调用的函数直接作为参数传入装饰器的外围函数括弧
        将装饰器与被调用函数绑定在一起
        @+装饰器函数，放在被调用函数的上一行，被调用的函数正常定义，只需要直接调用被执行函数即可
    语法：
    def out(func_args): 外围函数
        def inter(*args,**kwargs): 内嵌函数
            return func_args(*args,**kwargs)
        return inter
'''
def a(func):
    def b(*args,**kwargs):
        return func(*args,**kwargs)
    b()

a()
# b()   # NameError: name 'b' is not defined

'''
    类的继承
    类的多重继承
    类的多态
    类的高级函数
'''


'''
    异常
    -何为异常
    - 关键字
        - try
        - except
        - finally
    - 内置异常类型
    - 自定义异常类型
    - 自定义抛出异常
'''