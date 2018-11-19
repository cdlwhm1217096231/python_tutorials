import socket

'''
相对TCP编程，UDP编程就简单多了，当然可靠性和安全性也差很多。由于UDP没有握手和挥手的过程，因此accept()和connect()方法都不需要
'''
ip_port = ('127.0.0.1', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(ip_port)

while True:
    data = s.recv(1024).strip().decode()
    print('服务端接收到的数据:',data)
    if data == 'exit':
        print('客户端主动断开连接!')
        break
s.close()
