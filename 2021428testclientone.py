from socket import *
import threading,re
HOST='192.168.3.24'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)
tC=socket(AF_INET,SOCK_DGRAM)
Tflag=True
def action(tC):
    while True:
        data,addr=tC.recvfrom(BUFSIZE)
        sRes=data.decode()
        talkName=re.match("^T:(\w):(.*)",sRes)#匹配通信的用户名
        if talkName:
            print(">",talkName.group(1)," say:",talkName.group(2))
        else:
            print(sRes)
t=threading.Thread(target=action,args=(tC,))
try:
    while Tflag:
        data=input(">")
        if data == '88':
            break
        tC.sendto(data.encode(),ADDR)
        if t.is_alive() is False:
            t.start()
except KeyboardInterrupt as e:
    print(e)
    tC.close()