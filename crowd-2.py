# udpclient.py
from socket import *
# import sys
host = '192.168.3.24'
print(host)
port = 5857
adress = (host, port)
s =socket(AF_INET,SOCK_DGRAM)

while True:
    message = input('please input your sended message:')
    s.sendto(message.encode('utf-8'), adress)
    data, adress = s.recvfrom(1024)
    print(data.decode('utf-8'), adress)
s.close()
