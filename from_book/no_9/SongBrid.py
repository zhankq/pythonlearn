class Brid:
    def __init__(self,hungry):
        self.hungry = hungry

    def eat(self):
        if self.hungry:
            print("Aaaah ...")
            self.hungry = False
        else:
            print("No, thanks")


#b=Brid()
#b.eat()
'''
class SongBrid(Brid):
    def __init__(self):
        Brid.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)
'''

class SongBrid(Brid):
    def __init__(self,hungry):
        super().__init__(hungry)
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBrid(False)
sb.sing()

sb.eat()

sb.eat()
