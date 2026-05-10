class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)
    def __str__(self):
        return f"姓名: {self.name} | 语文成绩:{self.chinese} |数学成绩：{self.math} | 英语成绩：{self.english}"
    def update(self,chinese, math, english):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class ManagerStudent:
    def __init__(self):
        self.manage_list=[]
    def add (self):
        name = input("请输入姓名：")
        for s in self.manage_list:
            if s.name == name:
                print("重复，重新输入")
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        if 100 >= chinese >= 0 and 100 >= math >= 0 and 100 >= english >= 0:
            stu=Student(name,chinese,math,english)
            self.manage_list.append(stu)
            print("成功")
        else:
            print("成绩应在0—100之间")
            return
    def edit (self):
        name = input("请输入要修改的姓名:")
        for s in self.manage_list:
            if s.name == name:
                chinese = int(input("请输入语文成绩："))
                math = int(input("请输入数学成绩："))
                english = int(input("请输入英语成绩："))
                if 100 >= chinese >= 0 and 100 >= math >= 0 and 100 >= english >= 0:
                    s.update(chinese, math, english)
                    print("成功")
                    return
                else:
                    print("成绩应在0—100之间")
                    return
        print("该姓名不存在！重新输入")
    def delete (self):
        name = input("请输入要删除的姓名:")
        for s in self.manage_list:
            if s.name == name:
                self.manage_list.remove(s)
                print("成功")
                return
        print("该姓名不存在！重新输入")
        return
    def select (self):
        name = input("请输入要查询的姓名:")
        for s in self.manage_list:
            if s.name == name:
                print(s)
                return
        print("该姓名不存在！重新输入")
        return
    def all_select (self):
        for s in self.manage_list:
            print(s)

    def run(self):
        while True:
            try:
                print("""
                    1.添加   2.修改   3.删除  
                    4.查询   5.展开   6.退出
                    """)
                st=int(input("请输入操作选项(1-5):"))
                match st :
                    case 1:
                        self.add()
                    case 2:
                        self.edit()
                    case 3:
                        self.delete()
                    case 4:
                        self.select()
                    case 5:
                        self.all_select()
                    case 6:
                        print("已退出！")
                        break
                    case _:
                        print("错误选项，重新输入！")
            except ValueError :
                print("出现错误！请仔细检查重新输入！")
            except Exception:
                print("出现错误！请仔细检查重新输入！")


if __name__ == '__main__':
    m1=ManagerStudent()
    m1.run()