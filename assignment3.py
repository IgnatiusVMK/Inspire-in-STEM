#Task --> Write a program ;that gets user input and adds ksh 10,000
# to her account if she is btwn 25-30 years

#gender = input("What is your gender - male/female? ")
age = input("What is your age? ")

acc_bal = 0

#if gender = female
if (int(age) > 25) and (int(age) < 30 ):
    acc_bal = acc_bal +10000 
    print("Congrats,Ksh 10000 has been deposited to your acc.")
else:
    print("Sorry,request un-available for your age bracket💔😂")

 