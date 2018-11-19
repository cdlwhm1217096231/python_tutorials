import socket
import threading

'''
如果有多个客户端同时连接同一个服务器呢？因为服务器无法同时对多个客户端提供服务
因为Python的socket模块，默认情况下创建的是单进程单线程，同时只能处理一个连接请求，如果要实现多用户服务，那么需要使用多线程机制。
'''


def link_handler(link, client):
    """
    该函数为线程需要执行的函数，负责具体的服务器和客户端之间的通信工作
    :param link:  当前线程处理的连接
    :param client: 客户端ip和端口信息，一个二元元组
    :return: None
    """
    print("服务端开始接收来自[%s:%s]的请求...." % (client[0], client[1]))
    while True:  # 利用一个死循环，保持和客户端的通信状态
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("结束与[%s:%s]的通信..." % (client[0], client[1]))
            break
        print("来自[%s:%s]的客户端向你发来信息：%s" % (client[0], client[1], client_data))
        link.sendall('服务器已经收到你的信息'.encode())
    link.close()


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求

print('启动socket服务，等待客户端连接...')

while True:     # 一个死循环，不断的接受客户端发来的连接请求
    conn, address = sk.accept()  # 等待连接，此处自动阻塞
    # 每当有新的连接过来，自动创建一个新的线程，
    # 并将连接对象和访问者的ip信息作为参数传递给线程的执行函数
    t = threading.Thread(target=link_handler, args=(conn, address))
    t.start()

# 启动这个多线程服务器，然后多运行几个客户端，可以很明显地看到，服务器能够同时与多个客户端通信