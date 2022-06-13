#!usr/bin/python

########################
#          Loops
#          Name: Ignatius Victor M.K
#          Date: 26/5/2021
########################


#for number in range(0,10):
 #   if (number%2==0):
  #      print(number)

#Task -->
#sum of all even numbers btwen 0-50

#sum_nums = 0
#for number in range(0,50):
 #   if (number%2==0):
  #     sum_nums = sum_nums + number
   #    print(number)
#print(sum_nums) 

#products of all odd numbers btwn 0-50
#prod_nums = 1
#for number in range(0,50):
 #   if (number%2==1):
  #       prod_nums = prod_nums*number
         #print(number)
#print(prod_nums)

#Calculate the factorial of six
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

#Calculate the factorial of six
#number = 1
#for number in range(0,7):
 #   if (number):
  #       factorial = number*(number-1)
   #      print(number)
#print(factorial)

# Operators
# < less than
# > greater than
# >=
# <=
# == comparison operators
# = assigning

num = 0
while num < 10:
    if (num % 2 ==0):
        print(num)
    num = num+1
      