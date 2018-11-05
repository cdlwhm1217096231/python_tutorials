#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/24 10:48'
__author__ = 'cdl'

# 使用socket网络编程
"""socket表示一个网络连接，通过这个连接，使得主机之间或者一台计算机上的进程间可以通信。"""
"""既然是通信，必定有一个发送方，一个接收方。对应一个客户端，和一个服务端。"""
# 创建客户端
import socket
import threading
# 1.创建socket，建立连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 指定IPv4协议（AF_INET）,IPv6协议请使用AF_INET6; 指定使用TCP协议（SOCK_STREAM），UDP协议请使用SOCK_DGRAM
sock.connect(('www.sina.com.cn', 80))  # 参数是一个tuple，tuple里指定服务器地址（域名或ip）和端口号
# 2.发送数据
sock.send("GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\n\r\n".encode("utf-8")) # 注意这里str格式要遵循HTTP协议标准, 注意结尾一定要用 \r\n\r\n
# 3.接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = sock.recv(1024)
    if d:
        # Python3接收到为bytes类型，要转为str
        buffer.append(str(d))
    else:
        break
data = ''.join(buffer)
# 创建服务端
# 1.创建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定ip和port
sock.bind(('127.0.0.1', 9999))  # 注意以元组格式传入，可以是某网卡的公网ip，或0.0.0.0，或127.0.0.1
# 3.监听端口
sock.listen(5)  # 指定等待连接的最大数量
# 4.接收数据
# 连接处理函数
def tcplink(sock, addr):
    while True:
        data = sock.recv(1024)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
while True:
    # 接受一个新连接，阻塞的，只有接收到新连接才会往下走
    sock, addr = sock.accept()
    # 每一次连接，都要创建新线程，否则一次只能处理一个连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


"""socket公共函数汇总"""
# 发送数据------------
# 发送TCP数据，返回值：发送的字节当量
sk.send("data string")
# 完整发送TCP数据，频繁调用send方法，确保数据发送完成
sk.sendall("data string")
# 发送UDP数据
sk.sendto("data string",address)
# 接收数据---------------
# 接收TCP数据，一次最大只接收1k数据
sk.recv(1024)
# 接收UDP数据，一次只接收1k数据，返回值：数据和发送方ip
(data,address) = sk.recvfrom(1024)
# 获取socket信息---------
# 获取远程socket的addr,port
(addr, port) = sk.getpeername()
# 获取本地socket的addr,port
(addr, port) = sk.getsockname()
# 获取其他信息------------
# 获取当前主机名
HostName = socket.gethostname()
# 获取当前主机的ip
HOST = socket.gethostbyname(HostName)
# 获取当前socket连接的文件描述符
file_no = sk.fileno()
# 设置socket--------------
# 设置连接的超时时间
sk.settimeout(timeout)
sk.gettimeout()
# 设置为非阻塞模式，默认是0（阻塞）
# 非阻塞下，accept和recv时一旦无数据，则报错：socket.Error
sk.setblocking(1)
# 设置socket内部参数，
# 具体有哪些参数，可以查看socket类的python源码
sk.setsockopt(level,optname,value)
sk.getsockopt(level,optname)



