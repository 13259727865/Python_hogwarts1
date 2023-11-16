import json
import socket
import threading

import yaml


class StudentServer:
    def __init__(self):
        # 学生信息

        # 创建socket对象
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置复用端口
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定Ip和端口
        self.server.bind(("127.0.0.1", 8888))
        # 设置服务器监听
        self.server.listen(128)
        print("服务器启动，等待连接127.0.0.1：8888")

    def startserver(self):
        while True:
            # 接受客户端得连接，返回客户端的socket对象和ip_port
            client, ip_port = self.server.accept()
            print(f"客户端使用IP{client},端口{ip_port}连接成功")
            # 创建一个子线程，处理客户端请求
            t = threading.Thread(target=self.handleclientrequest, args=(client,))
            t.daemon = True
            t.start()

    # 处理客户端请求
    def handleclientrequest(self, client):
        recv_data = client.recv(4096).decode("gbk")
        if len(recv_data) == 0:
            client.close()
            return
        request = self.parseRequest(recv_data)
        # 把解析的客户端数据用不同的函数进行处理
        response = self.router(request)
        # 将响应数据返回给客户端
        print("end",response)
        client.send(response)
        client.close()

    # 解析客户端信息
    def parseRequest(self, recv_data):
        request = {
            "method": "",
            "path": "",
            "values": {}
        }
        recv_data = recv_data.split()
        request["method"] = recv_data[0]
        tmp = recv_data[1]
        if "?" in tmp:
            request["path"] = tmp.split("?")[0]
            params = tmp.split("?")[1].split("&")
            for x in params:
                k, v = x.split("=")
                request["values"][k] = v
        else:
            request["path"] = tmp
        return request

    # 路由函数
    def router(self, request):
        path = request["path"]
        reponse_body = ''
        if path == "/add":
            reponse_body = self.add_student(request)
        elif path == "/change":
            reponse_body = self.change_student(request)
        elif path == "/query":
            reponse_body = self.query_student(request)
        elif path == "/query":
            reponse_body = self.del_student(request)

        reponse = "HTTP/1.1\n\r"
        reponse += "Connection: keep-alive\n\r"
        reponse += "Cache-Control: max-age=0\n\r"
        reponse += "Content-Type: application/json; charset=utf-8\n\r"
        reponse += "\n\r"
        reponse += reponse_body
        reponse = reponse.encode()
        print(reponse)
        return reponse

    def student_isexist(self, sid=None, name=None):
        student_isexist = False
        student_list = self.read_student_data()
        for item in student_list:
            if sid:
                if item["sid"] == sid:
                    print("输入的编号存在")
                    student_isexist = True
            elif name:
                if item["name"] == name:
                    print("输入的编号存在")
                    student_isexist = True
        return student_isexist


    # 读取学生数据
    def read_student_data(self):
        with open("student_data.yaml", "r", encoding="utf-8") as student:
            student_list = yaml.safe_load(student)
            return student_list


    # 保存修改数据
    def save_student_data(self, student_list):
        with open("student_data.yaml", "w", encoding="utf-8") as student_save:
            yaml.safe_dump(student_list, student_save)
        print("保存到data.txt")

    # 添加学生信息接口
    def add_student(self, request):
        try:
            student_sid = request["values"]["sid"]
            if not self.student_isexist(sid=student_sid):
                new_student = {"sid": student_sid,
                               "name": request["values"]["name"],
                               "age": request["values"]["age"],
                               "gender": request["values"]["gender"]}
                student_list = self.read_student_data()
                student_list.append(new_student)
                self.save_student_data(student_list)
                return f"新学生添加成功！{new_student}"

            else:
                return "sid已存在！"
        except Exception as e:
            return f"参数有误"

    # 修改学生信息接口
    def change_student(self, request):
        try:
            request = request["values"]
            student_list = self.read_student_data()
            student_sid = request["sid"]
            if self.student_isexist(sid=student_sid):
                for item in student_list:
                    if item["sid"] == request["sid"]:
                        item["name"] = request["name"]
                        item["age"] = request["age"]
                        item["gender"] = request["gender"]
                        self.save_student_data(student_list)
                        return f"学生信息修改成功：{item}"
            else:
                return f"用户{request['sid']}不存在"
        except:
            return "参数有误！"

    #查询学生信息接口
    def query_student(self, request):
        try:
            request = request["values"]
            student_list = self.read_student_data()
            student_sid = request["sid"]
            if self.student_isexist(sid=student_sid):
                for item in student_list:
                    if item["sid"] == request["sid"]:
                        return f"{item}"
            else:
                return f"用户{request['sid']}不存在"
        except:
            return "参数有误！"


    #删除学生信息接口
    def del_student(self, request):
        try:
            request = request["values"]
            student_list = self.read_student_data()
            student_sid = request["sid"]
            if self.student_isexist(sid=student_sid):
                for item in student_list:
                    if item["sid"] == request["sid"]:
                        index = student_list.index(item)
                        del_student = student_list.pop(index)
                        self.save_student_data()
                        return f"通过编号删除成功{del_student}"
            else:
                return f"用户{request['sid']}不存在"
        except:
            return "参数有误！"


if __name__ == '__main__':
    server = StudentServer()
    server.startserver()
