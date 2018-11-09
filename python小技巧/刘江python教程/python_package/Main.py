# import module_a

# module_a.func()

print('-----------1----------------')
from module_a import func

# module_a.func()    错误的调用方式
func()  # 这时需要直接调用func

print('------------2---------------')
from module_a import func as f


def func():  # main模块内部已经有了func函数
    print("this is main module!")

func()
f()

print('------------3---------------')
from module_a import *


def func():
    print("this is main module!")

func()  # 从module_a导入的func被main的func覆盖了
