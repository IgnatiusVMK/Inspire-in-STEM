#!usr/bin/python

########################
#          Quadratic equations
#          Name: 
#          Date: 31/5/2021
########################

# a is the co-efficient of the first term 
# b is the co-efficient of the second term
# c is the constant
import math

a = int(input("Enter the co-efficient of the first term: "))
b = int(input("Enter the co-efficient of the second term: "))
c = int(input("Enter the constant: "))
d = math.sqrt((b**2) - (4*a*c))

def find_roots(a,b,c):
    y_1=((-b + d) / (2*a))
    y_2=((-b - d) / (2*a))
    print("The roots of the quadratic equation:",y_1,y_2)
find_roots(a,b,c)