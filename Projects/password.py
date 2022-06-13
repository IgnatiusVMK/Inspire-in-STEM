#!usr/bin/python

########################
#          Password generators
#          Name: Ignatius Victor M.K
#          Date: 3/6/2021
########################

import random

print("Welcome to our Password generator😊")
char ="Marley@7345"
num_pass = int(input("What number of passwords would you like to generate? "))
len_pass = int(input("Enter your preferred password length: "))
print("\n Here are your passwords! ")

for pwd in range(num_pass):
    password = " "
    for c in range (len_pass):
      password+= random.choice(char)
    print(password)

