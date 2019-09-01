class Caolei:
    def cal(self,expression):
        self.value=eval(expression)

    #def talk(self):
    #
        print('~~~~')

class Talker:
    def talk(self):
        print('hell',self.value)

class totals(Caolei,Talker):
    pass

f = totals()
f.cal('1+2')
f.talk()
