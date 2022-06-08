# Ask user to select which input to check number or letter.
# After user enters their input the program should print based on the input inserted

num = int(input ("Enter data type: "))

#input("Enter as chosen above.")
temp=num
rev=0
while(num>0):
    rev=rev%10
    num=num/10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("Not a palindrome.")

string=input("Enter a string: ")
if (string==string[::-1]):
    print("The stirng is a palindrome")
else:
    print("Not a palindrome")
