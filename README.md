# Python 第六章练习代码

本仓库包含 Python 学习过程中第六章的实践代码，涵盖了模块导入、类与对象、异常处理、数据模型等知识点。

## 项目结构

- `module01/`：自定义模块示例
- `utils/`：工具函数模块
- `01.导入包示例.py`：演示如何导入包和模块
- `02.蒙特卡洛随机图生成器.py`：使用蒙特卡洛方法生成随机图
- `03.定义类.创建对象.py`：类的定义与对象创建
- `04.定义类（优化）.py`：优化后的类定义
- `05.教务管理系统.py`：综合练习——学生成绩管理系统
- `06.数据科学 N 维向量模型.py`：自定义向量类，支持加法、距离计算等
- `07.异常处理.py`：异常处理基础
- `08.异常的传递.py`：异常传递机制

## 运行环境

- Python 3.x
- 部分程序需要 `math`、`random` 等标准库（无需额外安装）

## 使用方法

1. 克隆仓库：
   ```bash
   git clone https://github.com/Spark-ding/Python-Chapter6-Exercises.git
2. 进入项目目录：
   cd Python-Chapter6-Exercises

3. 直接运行任意 .py 文件，例如：
   python 05.教务管理系统.py

##  知识点覆盖

### 1. 包与模块
- 创建包（包含 __init__.py）
- 导入模块的多种方式（import、from ... import）
- 模块别名（as）的使用

### 2. 面向对象编程
- 类的定义、构造方法 __init__
- 实例属性与类属性
- 实例方法、类方法（@classmethod）
- 魔法方法：__str__、__add__
- 运算符重载

### 3. 异常处理
- try...except...finally 结构
- 异常的传递机制
- 主动抛出异常（raise）

### 4. 综合项目
- 学生成绩管理系统：增删改查、成绩修改、输入校验
- N 维向量模型：向量加法、欧几里得距离计算、维度校验

##  代码示例

### 定义类与创建对象
    class Student:
        def __init__(self, name, chinese, math, english):
            self.name = name
            self.chinese = chinese
            self.math = math
            self.english = english

        def __str__(self):
            return f"姓名：{self.name}，总分：{self.chinese + self.math + self.english}"

### 向量加法（运算符重载）
    class Vector:
        def __init__(self, *coords):
            self.coords = coords

        def __add__(self, other):
            if len(self.coords) != len(other.coords):
                raise ValueError("维度不同")
            return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

## 🛠️ 使用到的标准库

- math：数学计算（如开方）
- random：蒙特卡洛随机图生成
- zip：用于配对坐标

## 📌 学习建议

- 先阅读代码注释，理解设计思路。
- 尝试自己重新实现一遍，再对比差异。
- 修改代码，观察运行结果的变化，加深理解。

## 👤 作者

- GitHub：Spark-ding

## 📄 许可证

本项目仅用于学习交流，可自由参考和修改。