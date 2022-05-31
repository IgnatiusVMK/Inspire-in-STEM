# Write a program that will write numbers in reverse order
from unicodedata import digit


Number = int(input("Please enter any number: "))
Reverse  = 0
while (Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number =   Number //10

print("\n Reverse of entered number is = %d " %Reverse)

num  = int(input("Please enter any number: "))
reversed_num = 0
while num !=0:
    digit = num % 10
    reversed_num = reversed_num*10 +  digit
    num //=10
print("The reversed number is: " +str(reversed_num))