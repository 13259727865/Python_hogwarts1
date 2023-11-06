import json


class StudentManage:
    """
    实现学生管理系统：
    学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息
    1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

        print("*****************************************************")
        print("*                   学生管理系统                       *")
        print("*                1. 添加新学生信息                     *")
        print("*                2. 通过学号修改学生信息                *")
        print("*                3. 通过学号删除学生信息                *")
        print("*                4. 通过姓名删除学生信息                *")
        print("*                5. 通过学号查询学生信息                *")
        print("*                6. 通过姓名查询学生信息                *")
        print("*                7. 显示所有学生信息                   *")
        print("*                8. 退出系统                          *")
        print("******************************************************")
        select_op = input("输入编号选择操作：")

    2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
    3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
    4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
    5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
    6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
    7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
    8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
    9. 实现函数，输出所有学生信息
    """
    def __init__(self):
        # 学生信息
        with open("data.txt","r",encoding="utf-8") as student:
            self.student_list = json.load(student)



    # 获取菜单信息
    def getmenu(self):
        with open("menu.txt", "r", encoding="utf-8") as student_menu:
            print(student_menu.read())


    #判断学生是否存在
    def student_isexist(self,sid=None,name=None):
        student_isexist = False
        for item in self.student_list:
            if sid:
                if item["sid"] == sid:
                    print("输入的编号存在")
                    student_isexist = True
            elif name:
                if item["name"] == name:
                    print("输入的编号存在")
                    student_isexist = True
        return student_isexist

    #输入学生信息name,age,gender
    def input_student(self):
        name = input("请输入名字：")
        age = input("请输入年龄：")
        gender = input("请输入性别（W/M）")

        return name,age,gender


    # 添加新学生信息
    def add_student(self, sid):
        student_res=self.input_student()
        new_student = {"sid": sid, "name": student_res[0], "age": student_res[1], "gender": student_res[2]}
        self.student_list.append(new_student)
        print(f"新学生添加成功！{new_student}")
        self.save()
        return new_student


    #修改学生信息
    def update_student(self,sid):
        update_student_info = self.input_student()
        for item in self.student_list:
            if item["sid"] == sid:
                item["name"]=update_student_info[0]
                item["age"]=update_student_info[1]
                item["gender"] = update_student_info[2]
                print (f"学生信息修改成功：{item}")
                self.save()
                return

    #通过学号\姓名删除学生信息
    def del_student(self,sid=None,name=None):
        for item in self.student_list:
            if sid:
                if item["sid"] == sid:
                    index = self.student_list.index(item)
                    del_student = self.student_list.pop(index)
                    print(f"通过编号删除成功{del_student}")
                    self.save()

            elif name:
                if item["name"] == name:
                    index = self.student_list.index(item)
                    del_student = self.student_list.pop(index)
                    print(f"通过名字删除成功{del_student}")
                    self.save()


    #通过学号\姓名查询学生信息
    def select_student(self,sid=None,name=None):
        if sid:
            for item in self.student_list:
                if item["sid"]==sid:
                    print(f"查询到学生：{item}")
        elif name:
            for item in self.student_list:
                if item["name"] == name:
                    print(f"查询到学生：{item}")
        elif sid is None and name is None:
            for item in self.student_list:
                print(f"查询到学生：{item}")

    #保存修改数据
    def save(self):
        with open("data.txt","w",encoding="utf-8") as student_save:
            json.dump(self.student_list,student_save)
        print("保存到data.txt")



    def main(self):

        while True:
            self.getmenu()
            select_op = int(input("输入编号选择操作："))
            match select_op:
                #1. 添加新学生信息
                case 1:
                    while True:
                        sid = str(input("请输入新学生编号："))
                        #判断sid是否存在
                        ispre = self.student_isexist(sid)
                        if not ispre:
                            break
                    self.add_student(sid)

                #2. 通过学号修改学生信息
                case 2:
                    while True:
                        sid = str(input("请输入新学生编号："))
                        # 判断sid是否存在
                        if  self.student_isexist(sid):
                            self.update_student(sid)
                            break
                        else:
                            print("该编号不存在请重新输入！")
                #3. 通过学号删除学生信息
                case 3:
                    while True:
                        sid = str(input("请输入新学生编号："))
                        # 判断sid是否存在
                        if self.student_isexist(sid):
                            self.del_student(sid=sid)
                            break
                        else:
                            print("该编号不存在请重新输入！")
                #4. 通过姓名删除学生信息
                case 4:
                    while True:
                        name = str(input("请输入要删除的学生姓名："))
                        # 判断sid是否存在
                        if self.student_isexist(name):
                            self.del_student(name=name)
                            break
                        else:
                            print("该姓名不存在请重新输入！")
                #5. 通过学号查询学生信息
                case 5:
                    while True:
                        sid = str(input("请输入要查询的学生学号："))
                        # 判断sid是否存在
                        if self.student_isexist(sid=sid):
                            self.select_student(sid=sid)
                            break
                        else:
                            print("该学号不存在请重新输入！")
                #6. 通过姓名查询学生信息
                case 6:
                    while True:
                        name = str(input("请输入要查询的学生姓名："))
                        # 判断sid是否存在
                        if self.student_isexist(name=name):
                            self.select_student(name=name)
                            break
                        else:
                            print("该姓名不存在请重新输入！")
                #7. 显示所有学生信息
                case 7:
                    self.select_student()

                #8. 退出系统
                case 8:
                    self.save()
                    exit()

                case _:
                    print("输入操作序号有误，请重新输入")


if __name__ == '__main__':
    studio = StudentManage()
    studio.main()
