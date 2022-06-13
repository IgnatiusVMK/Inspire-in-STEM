#!usr/bin/python

########################
#          Assignment1 
#          Name: Ignatius Victor M.K
#          Date: 24/5/2021
########################

# calculate the are of a circle 

# volume of a cylinder

# surface area of a cylinder

# volume of a cube

#let the user type input

# Area of a circle

radius = input("Enter the radius of circle ")
PI = int(22/7)

area =int(PI) * int(radius)*int(radius)
print("Area of a circle is " + str(area))

# Volume of cylinder
H = input("Enter the height of the cylinder ")
prod =int(PI)*int(radius)*int(radius)*int(H)
print("Volume of the cylinder is " + str(prod))

# Surface area of a cylinder
D = int(2* radius)

surfaceArea = (2*(int(PI)*int(radius)*int(radius)) + int(PI)*int(D)*int(H))
print("surfaceArea of a cylinder is " + str(surfaceArea))

# volume of a cube
L = input("Enter the length of the cube ")
Volume = int(L)*int(L)*int(L)
print("Volume of the cube is " + str(Volume))