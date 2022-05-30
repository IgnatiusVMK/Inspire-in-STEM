#!usr/bin/python

########################
#          Patterns
#          Name: 
#          Date: 27/5/2021
########################

rows = int(input("enter number of rows: "))
for i in range (rows):
    for j in range (i+1):
        print(j + 1, end = " ")
    print("\n") 
