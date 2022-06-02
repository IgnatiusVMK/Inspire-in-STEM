#!usr/bin/python

########################
#          Introduction to Classes
#          Name: 
#          Date: 26/5/2021
########################

class Person:
    def __init__(self, _name, _age):
        self.name= _name
        self.age= _age

    def sayHi(self):
        print('Hello, my name is ' +str(self.name) + ' and I am ' +str(self.age) + ' years old.')
person1 = Person('Marley', 19)
person2 = Person('James', 22)
person1.sayHi()
person2.sayHi()