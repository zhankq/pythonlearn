class Student:
    def __init__(self,name,age,gender,phone,address,email):
        self.__name = name
        self._age = age
        self._gender = gender
        self._phone = phone
        self._address = address
        self._email = email
    
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self._age
    @property
    def gender(self):
        return self._gender
    @property
    def phone(self):
        return self._phone
    @property
    def address(self):
        return self._address
    @property
    def email(self):
        return self._email

demo = Student("张三",25,"男","13868049744","浙江杭州","zhankq@163.com")
print(demo.name)