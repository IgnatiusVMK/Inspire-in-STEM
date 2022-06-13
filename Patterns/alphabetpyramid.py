#!usr/bin/python

########################
#          Alphabetical Patterns
#          Name: Ignatius Victor M.K
#          Date: 11/6/2021
########################

n=10
ascii= 65
for i in range(n):
    print((n-i-1)*" ", end=" ")
    for j in range(0, i+1):
        print(chr(ascii), end=" ")
        ascii +=1
    print()