#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/24 11:22'
__author__ = 'cdl'
import socket
import time
import threading
import requests
import json


class ChatServer:
    def __init__(self, port):
        # 绑定服务器的ip和端口，注意以tuple的形式
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", port))
        self.socket.listen(5)
        # 图灵机器人，授权码
        self.key = "42296682238b4405b04bb79b40ed1995"
        print("正在监听 127.0.0.1 ：{}...".format(port))

    def tcplink(self, sock, addr):
        # 每次连接，开始聊天前，先欢迎下。
        sock.send("你好，欢迎来到机器人聊天器！".encode("utf-8"))
        while True:
            data = sock.recv(1024).decode("utf-8")
            print(sock.getpeername())
            print(sock.getsockname())
            print(sock.fileno())
            username = data.split("::")[0]
            msg = data.split("::")[1]
            if msg == "exit":
                break
            if msg:
                print("【"+username+"】 "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
                print(msg)
                response = self.get_response(msg)
                sock.send(response.encode("utf-8"))
        sock.close()
        print("与 {} 结束聊天！".format(username))

    def get_response(self, info):
        # 调用图灵机器人API
        url = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        return jd['text']

    def main(self):
        while True:
            sock, addr = self.socket.accept()
            t=threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

if __name__ == '__main__':
    cs = ChatServer(port=9999)
    cs.main()