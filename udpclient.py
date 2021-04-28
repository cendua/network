# udpclient.py
from socket import*
host = '192.168.3.24'
port = 9999
adress = (host, port)
s = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('send message:')
    s.sendto(message.encode('utf-8'), adress)
    data, adress = s.recvfrom(1024)
    print(data.decode('utf-8'), adress)
s.close()
