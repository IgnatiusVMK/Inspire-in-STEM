#!usr/bin/python

########################
#          Assignment4 
#          Name: Ignatius Victor M.K
#          Date: 24/5/2021
########################

# Write a program to withdraw Ksh 25,000 if account balance is between Ksh 100,000 to 200,000
#   30% if acc is 500,000 1,000,000.

acc_bal = input("Enter your account balance ")
if (int(acc_bal) > 100000) and (int(acc_bal) < 200000):
    acc_bal = float(acc_bal) - 25000
    print("Ksh 25,000 has been debitted from your account.\n")
    print("Your balance is " + str(acc_bal))
elif (int(acc_bal) > 500000) and (int(acc_bal) < 1000000):
    acc_bal = float(acc_bal) - (0.3*float(acc_bal))
    print(" We have deducted 30 percent from your accoungt")
    print("Your balance is " + str(acc_bal))
elif int(acc_bal > 1000000):
    print("We have deducted Ksh 15,000 from your aacount.")