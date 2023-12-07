import socket
#前端
# socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# socket_client.connect(("127.0.0.1",8888))
#
# send_data = "hello".encode("utf-8")
# socket_client.send(send_data)
#
# recv_data = socket_client.recv(1024)
# print(recv_data)

#基于TCP的socket服务端

#创建服务段套接字对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置端口利用
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#绑定Ip和端口
server.bind(("127.0.0.1",8888))
#设置服务器监听
server.listen(128)
print("服务器启动，等待连接")

#等待客户端连接
client,ip_port=server.accept()
print(f"客户端使用IP{client},端口{ip_port}连接成功")

#接受客户端消息
recv_data = client.recv(1024).decode("utf-8")
print(f"接受客户端消息数据{recv_data}，长度{len(recv_data)}")

#将收到的数据转换成大写并编码后发送给客户端
send_data = recv_data.encode("utf-8")
client.send(send_data)

#关闭客户端
client.close()

#g关闭服务器连接


