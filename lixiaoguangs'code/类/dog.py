#首字母大写的是类
class Dog():
    """模拟小狗"""
    #使用的文档字符串可以调用,必须缩进
    def __init__(self,name,age):
        #类中的函数成为方法
        """初始化属性name and name"""
        self.name = name##属性
        self.age = age

    def sit(self):
        """模拟小狗命令后蹲下"""
        print(self.name.title()+"is now sitting")
    def roll_over(self):
        """小狗打滚"""
        print(self.name.title() + "rolled over!")

class Dog:
    my_dog = Dog('willie',6)

    print("My dag's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")
