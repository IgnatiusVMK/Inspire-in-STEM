#!usr/bin/python

########################
#          Class
#          Name: 
#          Date: 3/6/2021
########################

class Vehicle:
    def __init__(self, srlno,  max_speed, mileage):
        self.serial = srlno
        self.max_speed= max_speed
        self.mileage= mileage

Toyota = Vehicle('001','240km', 400)
print(Toyota.mileage,Toyota.max_speed)

def specs(self):
        print("Vehicle serial no. " + str(self.serial_no) + " has a maximum speed of "+ str(self.max_speed)+ "and a mileage of" + str(self.mileage) + "." )
Toyota = Vehicle('001','240km ', ' 19,000km')
Chevloret = Vehicle('002','330km ', ' 22,000km')
Toyota.specs()