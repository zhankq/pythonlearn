class User:
	def __init__(self,name="ddds"):
		self.name=name

	def walk(self,content="d"):
		print(self,"正在慢慢地走",content)


u= User()

User.walk(u)
#u.walk("fkit")

class Person:
    '这是一个学习Python定义的一个Person类'
    hair = "black"
    def __init__(self,name="Charlie"):
        #定义实例变量
        self.name = name
    #定义一个say() 方法
    def say(self,content):
        print(content)

u = Person()
u.say("dd")
