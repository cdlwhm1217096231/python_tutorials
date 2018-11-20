import socket
"""
客户端依然使用socket模块就可以了，不需要导入socketserver模块
"""

ip_port = ("127.0.0.1", 9999)
s = socket.socket()
s.connect(ip_port)
s.settimeout(5)
data = s.recv(1024).decode()
print("服务端:", data)
while True:
    inp = input("你: ").strip()
    if not inp:
        continue
    s.sendall(inp.encode())

    if inp == "exit":
        print("谢谢使用,再见!")
        break
    data = s.recv(1024).decode()
    print("服务端:", data)
s.close()