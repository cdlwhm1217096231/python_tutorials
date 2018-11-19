import socket

ip_port = ('127.0.0.1', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    inp = input('请输入你要发送的信息: ').strip()
    s.sendto(inp.encode(), ip_port)
    if inp == 'exit':
        break
s.close()