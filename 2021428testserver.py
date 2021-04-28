from socket import *
from time import ctime
import re
HOST='192.168.3.24'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)
udpS=socket(AF_INET,SOCK_DGRAM)
udpS.bind(ADDR)
talkPair={}
print("waiting...............")
while True:
    data,addr=udpS.recvfrom(BUFSIZE)
    srcData=data.decode()
    talkName=re.match("routeone",srcData)
    if talkName:
        talkName=talkName.group(1)
        print(talkName)#用户注册用户名
        if talkName not in talkPair.keys():
            talkPair[talkName]=addr#字典关联socket
            sRes="welcome %s "%talkName
            udpS.sendto(sRes.encode(),addr)
        else:
            sRes="The name exsit"
            udpS.sendto(sRes.encode(),addr)
    else:#判断是否是发给某个人的
        talkName=re.match("^T:(\w+):",srcData)
        print(talkName)
        if talkName:
            talkName=talkName.group(1)
            if talkName:#判断发给某个人的姓名是否存在
                if talkName in talkPair.keys():#查找socket通信
                    udpS.sendto(srcData.encode(),talkPair[talkName])
                else:#发给某人的不存在提示用户不存在
                    sRes="No this one"
                    udpS.sendto(sRes.encode(),addr)
        else:
            sRes="Can't identify info"
            udpS.sendto(sRes.encode(),addr)
udpS.close()