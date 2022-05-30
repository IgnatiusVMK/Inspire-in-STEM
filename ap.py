#!usr/bin/python

########################
#          Arithmetic progression
#          Name: 
#          Date: 27/5/2021
########################

a = int(input("Enter the first number "))
d = int(input("Enter the common difference "))
n_term= int(input("Enter the n-term "))

for i in range(1,1+n_term):
    n_term = a + (i-1)*d
    print(n_term)

sum_n = (n_term/2)*(2*a+(n_term-1)*d)
print(sum_n)