#学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return (f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} "
                f"| 总分：{self.chinese+self.math+self.english}")

    #修改学生的成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


#学生管理系统类
class EduManagement:
    def __init__(self):
        self.student_list = []

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")

        #判断学生姓名是否存在，若存在则添加失败
        for s in self.student_list:
            if s.name == name:
                print(f"学生{name}已经存在，不能重复添加！")
                return

        try:
            chinese, math, english = [int(i) for i in input("请输入语数外成绩（用空格隔开）：").split()]
        except ValueError:
            print("输入格式错误，请输入三个数字并用逗号分隔！")
            return
        #判断分数是否在0-150之间
        if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功。")
        else:
            print("各科成绩必须在0-150之间。")


























if __name__ == '__main__':
    s1 = Student("王波", 90, 130, 120)
    print(s1)
    s1.update_score(chinese=130)
    print(s1)
