# the second test of the "face to the object"
from  socket import *

#初始化套接字
class initSocket():
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
    # def connet(self):
        self.adress=(self.ip,self.port)
        self.s=socket(AF_INET,SOCK_DGRAM)

#发消息,收消息
class Message(initSocket):
    def __init__(self,ip,port):
        super().__init__(ip,port)
    def sent(self):
        message = input('send message:')
        self.s.sendto(message.encode('utf-8'), self.adress)
    def receive(self):
        data, adress = self.s.recvfrom(1024)
        print(data.decode('utf-8'),self.adress)
#主函数

def main():
    ssocket=initSocket('192.168.3.24',5857)
    message=Message('192.168.3.24',5857)
    message.sent()
    message.receive()


if __name__ == '__main__':
    main()