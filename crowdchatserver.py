# udpserver.py
# 导入socket模块
import socket
host = '192.168.3.24'
port = 5857
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口号
s.bind((host, port))
print('/////稍等稍等')
while True:
    data, address = s.recvfrom(1024)
    print(data.decode('utf-8'), address)
    msg = '这是udp sefver 的响应信息'
    s.sendto(msg.encode('utf-8'), address)
s.close()
