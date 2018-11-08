from reflect反射机制 import commons


# def run():
#     inp = input('请输入您要访问页面的网址url: ').strip()
#     if inp == 'login':
#         commons.login()
#     elif inp == 'logout':
#         commons.logout()
#     elif inp == 'home':
#         commons.home()
#     else:
#         print('找不到页面,404')


## 上述函数当commons中有多个页面时候,需要在run函数中加入多个elif,所以方法不可行
## 又因为用户输入的url字符串和相应调用的函数名好像！如果能用这个字符串直接调用函数,即可解决问题。
## 但是字符串不能直接调用函数,所以这里使用了反射机制,主要体现在getattr()等几个内置函数上
## getattr()函数的使用方法：接收2个参数，前面的是一个类或者模块，后面的是一个字符串
## 这个过程就相当于把一个字符串变成一个函数名的过程


# def run():
#     inp = input('请输入需要访问页面的url: ').strip()
#     func = getattr(commons, inp)  # 通过getattr()函数，从commons模块里，查找到和inp字符串“外形”相同的函数名，并将其返回，然后赋值给func变量
#     func()

## 上述代码鲁棒性不好，当输入的字符串inp在commons中不存在时，将会报错
## python提供了一个hasattr()的内置函数，它可以判断commons中是否具有某个成员，返回True或False


def run():
    inp = input('请输入需要访问页面的url: ').strip()
    if hasattr(commons, inp):
        func = getattr(commons, inp)  # 通过getattr()函数，从commons模块里，查找到和inp字符串“外形”相同的函数名，并将其返回，然后赋值给func变量
        func()
    else:
        print('404 error')
## 通过hasattr()的判断，可以防止非法输入导致的错误，并将其统一定位到错误页面。


if __name__ == '__main__':
    run()

