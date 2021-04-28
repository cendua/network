# udpserver.py
from socket import*
host = '192.168.3.24'
prot = 12345
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, prot))
print('/////稍等稍等')
while True:
    data, address = s.recvfrom(1024)
    print(data.decode('utf-8'), address)
    msg = '这是udp sefver 的响应信息'
    s.sendto(msg.encode('utf-8'), address)
s.close()
