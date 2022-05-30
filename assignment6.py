#!usr/bin/python

########################
#          Geometric progression
#          Name: 
#          Date: 27/5/2021
########################

#Print first n terms of the Geometric Progression

a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
 
for i in range(1,n+1):
    t_n = a * r**(i-1)
    print(t_n)

## Getting Sum of first n terms in Geometric Progression
 # a(the first term), r(the common ratio), and n (the number of terms)
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
 
if(r>1):
  S_n = (a*(r**n))/(r-1)
else:
  S_n = (a*(r**n))/(1-r)
 
print("Sum of n terms: ",S_n)