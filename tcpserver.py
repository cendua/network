import socket
ip_port = ('192.168.3.24', 12345)
sk = socket.socket()
sk.bind(ip_port)
# 设置最大连接数
sk.listen(5)
print('server waiting//////')
conn, addr = sk.accept()
print("链接成功,客户端为")
print(addr)
while True:
    client_data = conn.recv(1024)
    print('receive clinet data=>' + client_data.decode('utf-8'))
    if client_data == 'q':
        break
    msg = 'cilient,我是server'
    conn.sendall(msg.encode('utf-8'))

conn.close()
sk.close()
