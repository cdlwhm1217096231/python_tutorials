#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/24 11:06'
__author__ = 'cdl'

import socket
import time

class ChatClient:
    def __init__(self, username, port):
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("127.0.0.1", port))

    def send_msg(self, msg):
        self.socket.send("{username}::{msg}".format(username=self.username,msg=msg).encode("utf-8"))

    def recv_msg(self):
        data=self.socket.recv(1024)
        if data:
            print("\n【机器人小图】"+" "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
            print(data.decode("utf-8"))
            return True
        return False

    def main(self):
        data = self.socket.recv(1024)
        print(data.decode("utf-8"))
        msg = input("请输入消息：")
        self.send_msg(msg)
        while True:
            if self.recv_msg():
                msg=input("\n我：")
                self.send_msg(msg)
                if msg == "exit":
                    print("聊天室已关闭")
                    break

if __name__ == '__main__':
    cc = ChatClient(username="Curry", port=9999)
    cc.main()
# 将服务端程序跑起来，然后运行客户端
