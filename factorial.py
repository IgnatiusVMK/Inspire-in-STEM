#!usr/bin/python

########################
#          Factorial of numbers
#          Name: 
#          Date: 27/5/2021
########################

#factorial of 6
number =int(input("enter the number "))
factorial = 1
if number<0:
    print("Factorial of -ve number doesn't exist")
elif (number==0):
    print("Factorial of 0 = 1")
else:
    for i in range(1,number+1):
        factorial = factorial * i
print("Factorial of number: " ,factorial)        

    