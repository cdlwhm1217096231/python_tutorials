import socketserver

class MyServer(socketserver.BaseRequestHandler):
    """
    必须继承socketserver.BaseRequestHandler类
    """
    def handle(self):   # handle()方法是整个通信的处理核心，一旦它运行结束，当前连接也就断开了
        """
        必须实现这个方法！
        """
        conn = self.request   # request里封装了所有请求的数据,调用send()和recv()方法都是通过self.request对象
        conn.sendall("欢迎访问socketserver服务端!".encode())
        while True:
            data = conn.recv(1024).decode()
            if data == 'exit':
                print("断开与%s的连接" % (self.client_address,))
                break
            print("来自%s的客户端向您发送的请求信息:%s" % (self.client_address, data))
            conn.sendall(("已收到你的信息%s" % data).encode())


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), MyServer)
    print("启动socketserver服务端!")
    server.serve_forever()    # 表示该服务器在正常情况下将永远运行
