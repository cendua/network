#from socket import *
import socket

# 链接服务端ip与端口
ip_port = ('192.168.3.24', 4545)
# creat socket
sk = socket.socket()
# connet service
sk.connect(ip_port)

while True:
    msg = input("please input message:")
    # 发送数据
    sk.sendall((msg.encode('utf-8')))
    if msg == 'q':
        break
    server_reply = sk.recv(1024)
    if not server_reply:
        break
    print(server_reply.decode('utf-8'))

sk.close()
