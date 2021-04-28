# udpclient.py
import socket
# host = '192.168.3.24'
# port = 5857
# adress = (host, port)
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#初始化构建套接字
class socketInit:
    def __init__(self,adr,s):
        self.adr=adr
        self.s=s

#收发信息的操作
class normalOption(socketInit):
    def __init__(self,adr,s):
        super().__init__(adr,s)
    def sent_message(self):
        message = input('please input your sended message:')
        self.s.sendto(message.encode('utf-8'), self.adr)
    def recv_message(self):
        data, adress = self.s.recvfrom(1024)
        print(data.decode('utf-8'), self.adr)


#选择节点并进行发送消息
class selectcilennum(normalOption):
    def __init__(self):
        self.clinum = input()
    def sent(self):

        if self.clinum == '1':
            normalOption.sent_message(self)

            #normalOption.recv_message(self)
        elif self.clinum == '2':
            normalOption.sent_message(self)

            #normalOption.recv_message(self)
        else :
            normalOption.sent_message(self)
            #normalOption.recv_message(self)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ss=socketInit(('192.168,3,24',5857),s)
    print("\nplease select contacts's number:\n1:client1  2:cline2 3:cint3")
    while True:
        joj = selectcilennum()
        joj.sent()
    pass

if __name__=='__main__':
    main()








