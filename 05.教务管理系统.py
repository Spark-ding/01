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
    system_version = 1.0
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
            print("输入格式错误，请输入三个数字并用空格分隔！")
            return
        #判断分数是否在0-150之间
        if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功。")
        else:
            print("各科成绩必须在0-150之间。")

    #修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                #输入修改后成绩
                print(f"当前成绩：{s}")
                raw_scores_list = (
                    input("请输入修改后语数外成绩（用空格隔开，不需要修改的科目请输入 '-'）：").split())
                if len(raw_scores_list) != 3:
                    print("输入格式错误，请输入三个值并用空格分隔！")
                    return
                # 剔除不需要修改的科目
                params = {}
                try:
                    if raw_scores_list[0] != "-":
                        params['chinese'] = int(raw_scores_list[0])
                    if raw_scores_list[1] != "-":
                        params['math'] = int(raw_scores_list[1])
                    if raw_scores_list[2] != "-":
                        params['english'] = int(raw_scores_list[2])
                except ValueError:
                    print("输入格式错误，成绩必须是数字。")
                    return
                #检查范围
                for v in params.values():
                    if not 0 <= v <= 150:
                        print("各科成绩必须在0-150之间。")
                        return
                #调用修改方法（Student类）
                s.update_score(**params)
                print("成绩修改成功。")
                print(f"最新成绩：{s}")
                return
        print("该生不在成绩系统中。")

    #删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功。")
                return
        print("未找到该学生，删除失败。")

    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生成绩：{s}")
                return
        print("未找到该学生。")

    #展示全部学生信息
    def all_student(self):
        if not self.student_list:
            print("当前没有学生信息。")
            return
        for s in self.student_list:
            print(s)

    #运行系统

    def run(self):
        while True:
            try:
                print()
                print(f"欢迎使用教务管理系统 v{EduManagement.system_version}")
                print("############# 学生成绩管理系统 #############")
                print("１．添加学生　　　２．修改学生成绩　　３．删除学生")
                print("４．查询单个学生　５．显示所有学生　　６．退出系统")
                choice = input("请输入操作（1-6）：")
                match choice:
                    case '1':
                        self.add_student()
                    case '2':
                        self.update_student()
                    case '3':
                        self.delete_student()
                    case '4':
                        self.query_student()
                    case '5':
                        self.all_student()
                    case '6':
                        print("感谢使用，再见！")
                        break
                    case _:
                        print("无效选项，请重新输入。")
            except KeyboardInterrupt:
                print("\n用户终端操作，退出系统。")
                break
            except Exception as e:
                print("发生未知错误：", e)

if __name__ == '__main__':
    edu = EduManagement()
    #添加一些初始测试数据
    edu.student_list.append(Student("王波", 90, 130, 120))
    edu.student_list.append(Student("李华", 120, 90, 130))
    edu.run()