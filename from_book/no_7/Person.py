class Person:
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello ,world! I'm {}.".format(self.name))

foo = Person()
bar = Person()
foo.set_name("llll")
bar.set_name('rrrrr')
bar.greet()
foo.greet()
