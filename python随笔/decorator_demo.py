#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装饰器"""
import time
###### 第一波 ######


def foo():
    print('foo')


print('函数对象,表示foo这个函数', foo)
foo()  # 调用foo函数
###### 第二波 ######


def foo():
    print('foo')


def foo(x): return x + 1


print('foo函数被重定义了：', foo(1))
######## 基础平台部门提供的功能如下  ##########


def f1():
    print('f1')


def f2():
    print('f2')


def f3():
    print('f3')


def f4():
    print('f4')


########  业务部门A 调用基础平台部门提供的功能  ##########
f1()
f2()
f3()
f4()
########  业务部门B 调用基础平台部门提供的功能  ##########
f1()
f2()
f3()
f4()
# 问题：之前基础平台部门的开发人员在写代码的时候，没有考虑验证相关的问题，基础平台提供的功能可以被任何人使用。
# 现在需要对基础平台的所有功能进行重构，加入验证机制。即调用基础平台的功能时，先验证，再调用
# 解决方法：只对基础平台的代码进行重构，其他业务部门无需做任何修改
######## 基础平台部门提供的功能如下  ##########


def check_login():
     # 验证1
    # 验证2
    # 验证3
    pass


def f1():
    check_login()
    print('f1')


def f2():
    check_login()
    print('f2')


def f3():
    check_login()
    print('f3')


def f4():
    check_login()
    print('f4')
# 缺点: 写代码要遵循开放封闭的原则：即对扩展开发开放，对已实现的功能模块封闭；
# 改进：使用装饰器@w1----仅仅对基础平台的代码进行修改，其他业务部门的无需做任何操作
######## 修改后的基础平台部门提供的功能如下  ##########


def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func
    return inner


@w1
def f1():
    print('f1')


@w1
def f2():
    print('f2')


@w1
def f3():
    print('f3')


@w1
def f4():
    print('f4')


# 原理解释
"""单独以f1为例解释"""


def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func
    return inner


@w1
def f1():
    print('f1')


# 解释@w1内部会执行以下操作：
"""
执行w1函数，并将@w1下面的函数作为w1函数的参数，即：@w1等价于w1(f1)。即:将原来的f1函数塞进另一个函数中
接着，内部会执行下面的语句:
def inner():
    # 验证
    return f1  此时的func等于f1
return inner 
最后,将执行完的w1函数返回值赋值给@w1下面的函数的函数名 
w1函数的返回值：
    def inner:
        # 验证
        return 原来的f1()  
然后，将此返回值再重新赋值给f1
新f1 = def inner():
            # 验证
            return 原来的f1()
"""
# 一个参数


def w1(func):
    def inner(arg):
        # 验证
        return func(arg)
    return inner


@w1
def f1(arg):
    print('f1')
# 两个参数


def w1(func):
    def inner(arg1, arg2):
        # 验证
        return func(arg1, arg2)
    return inner


@w1
def f1(arg1, arg2):
    print('f1')
# 三个参数


def w1(func):
    def inner(arg1, arg2, arg3):
        # 验证
        return func(arg1, arg2, arg3)
    return inner


@w1
def f1(arg1, arg2, arg3):
    print('f1')
#  装饰具有n个参数的函数的装饰器


def w1(func):
    def inner(*argc, **kwargs):
        # 验证
        return func(*argc, **kwargs)
    return inner


@w1
def f1(arg1, arg2, arg3):
    print('f1')
# 同一个函数可以被多个装饰器修饰


def w1(func):
    def inner(*argc, **kwargs):
        # 验证
        return func(*argc, **kwargs)
    return inner


def w2(func):
    def inner(*argc, **kwargs):
        # 验证
        return func(*argc, **kwargs)
    return inner


@w1
@w2
def f1(arg1, arg2, arg3):
    print('f1')
# 装饰器实战


def now():
    print('2018-07-13')


f = now
print('函数对象', type(f))
f()
print('函数对象的name属性', f.__name__)
# 下面增强now函数的功能-----在函数调用前后自动打印日志，但又不修改now()函数定义-----在代码运行期间动态增加功能的方式，称为装饰器


def log(func):  # log()是一个装饰器，返回一个函数；原来的now函数仍然存在，但调用now函数相当于执行了一个新函数，即在log函数中返回的inner函数
    def inner(*args, **kwargs):
        print('调用%s():' % func.__name__)
        return func(*args, **kwargs)
    return inner

# 无参数装饰器
@log  # 相当于log(now)
def now():
    print('2018-07-13')


# 调用now函数
now()
# 如果装饰器函数本身需要传入一个参数，则函数结构更加复杂

# 带参数装饰器
def log(text):
    def decorator(func):
        def inner(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return inner
    return decorator


# 等价于log('execute')(now)-----首先执行 log('execute'),返回的是decorator函数,再调用返回的函数.参数是now函数,返回值最终是inner函数
@log('execute')
def now():
    print('2018-07-13')


# 调用now()函数
now()
# 经过装饰器装饰后的函数对象的属性已经改变
print(now.__name__)
# 解决方法:functools.wraps
import functools


def log(func):  # log()是一个装饰器，返回一个函数inner；原来的now函数仍然存在，但调用now函数相当于执行了一个新函数，即在log函数中返回的inner函数
    @functools.wraps(func)  # 此语句就是解决了由于原函数name属性复制到inner函数属性的问题,出现在返回函数定义之前
    def inner(*args, **kwargs):
        print('调用%s():' % func.__name__)
        return func(*args, **kwargs)
    return inner


@log
def now():
    print('2018-07-13')


# 已解决: 经过装饰器装饰后的函数对象的属性已经改变
print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return inner
    return decorator


# 等价于log('execute')(now)-----首先执行 log('execute'),返回的是decorator函数,再调用返回的函数.参数是now函数,返回值最终是inner函数
@log('execute')
def now():
    print('2018-07-13')


now()
print(now.__name__)
# 练习
import time
import functools


def metric(func):
    functools.wraps(func)

    def wraper(*args, **kwargs):
        start = time.time()  # 执行前计时
        func(*args, **kwargs)  # 执行函数
        end = time.time()  # 执行后计时
        print("%s executed in %s ms" % (func.__name__, 1000 * (end - start)))
        return func(*args, **kwargs)
    return wraper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
print(f)

s = slow(11, 22, 33)
print(s)
# 测试过程
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
# 练习2


def log1(arg):
    if not isinstance(arg, str):
        func = arg
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s' % (func.__name__))
            r = func(*args, **kw)
            print('end call %s' % (func.__name__))
            return r
        return wrapper
    else:
        text = arg
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s %s()' % (text, func.__name__))
                r = func(*args, **kw)
                print('end %s %s()' % (text, func.__name__))
                return r
            return wrapper
        return decorator


@log1
def now1():
    print('2018-07-13')
now1()
print('-----------------')
@log1('execute')
def now1():
    print('2018-07-13')
now1()
# 装饰器补充
# 不带参数的函数装饰器
"""装饰函数"""
def logger(func):
    def wrapper(*args, **kwargs):
        print('我要执行{}函数啦！'.format(func.__name__))
        func(*args, **kwargs)
        print('执行完了，给自己加一个鸡腿！')
    return wrapper

"""业务函数"""
@logger
def add(x, y):
    return print('{} + {} = {}'.format(x, y, x+y))
# 函数调用
add(200, 50)
# 函数执行时间计算
"""装饰函数"""
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        cost_time = t2-t1
        print('函数执行时间:{}'.format(cost_time))
    return wrapper
"""业务函数"""
@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)
"""调用函数"""
want_sleep(2)
# 带参数的函数装饰器
def say_hello(country):
    def wrapper(func):
        def decorator(*args, **kwargs):
            if country == "america":
                print('hello！')
            elif country == "china":
                print('你好！')
            else:
                return
            func(*args, **kwargs)   #  真正执行函数的地方
        return decorator
    return wrapper


@say_hello("america")
def american():
    print('I am from America.')

@say_hello("china")
def chinese():
    print("我来自中国。")
# 调用函数
american()
print("------------")
chinese()
# 不带参数的类装饰器
"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。 __init__ ：接收被装饰函数 __call__ ：实现装饰逻辑。
"""
class logger(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("[INFO]: the function {func}() is running...".format(func=self.func.__name__))
        return self.func(*args, **kwargs)
@logger
def say(something):
    print("say {}!".format(something))

# 调用函数
say("hello")

# 带参数的类装饰器
class logger(object):
    def __init__(self, level='INFO'):
        self.level = level
    def __call__(self, func):     # 接受函数
        def wrapper(*args, **kwargs):
            print('[{level}]: the function {func}() is running...'.format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper   #  返回函数
@logger('WARNING')
def say(something):
    print("say {}!".format(something))
# 调用函数
say('hello')

# 内置装饰器property---------------它通常存在于类中，可以将一个函数定义成一个属性，属性的值就是该函数return的内容
class Student():
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError('输入不合法：年龄必须为数值!')
        if not 0 < age < 100:
            raise ValueError('输入不合法：年龄范围必须0-100')
        self._age = age

    def get_age(self):
        return self._age

    def del_age(self):
        self._age = None


Curry = Student('库里')
Curry.set_age(30)
print(Curry.get_age())
Curry.del_age()
"""
上面的代码设计虽然可以变量的定义，但是可以发现不管是获取还是赋值（通过函数）都和我们平时见到的不一样。
按照我们思维习惯应该是这样的: # 赋值 XiaoMing.age = 25 # 获取 XiaoMing.age
"""
class Student():
    def __init__(self, name):
        self.name = name
        self.name = None
    @property  # 用@property装饰过的函数，会将一个函数定义成一个属性，属性的值就是该函数return的内容。同时，会将这个函数变成另外一个装饰器。就像后面我们使用的@age.setter和@age.deleter。
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('输入不合法：年龄必须为数值!')
        if not 0 < value < 100:
            raise ValueError('输入不合法：年龄范围必须0-100')
        self._age = value
    @age.deleter
    def age(self):
        del self._age

XiaoMing = Student("小明")
# 设置属性
XiaoMing.age = 25
# 查询属性
print(XiaoMing.age)
# 删除属性
del XiaoMing.age
