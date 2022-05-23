# methods
name = "Safaricom"
# name = "Ada Lovelace"
user_name = " M-PESA "
age = 19
# age = 75
# person = "I am "+ str(name) + " and my age is " + str(age)
# print ("I am "+ str(name) + " and my age is " + str(age))
# the format () method
#print("My name is {} and I am {} years old".format(name, age) )
# newline \n and tab \t
# print(f"My name is {name} \n and I am {age} years old.")
print(user_name.lstrip())


# Multiple lines

msg = '''TFTAPESA KCB Vooma confirmed
         Ksh 50,000 debited from your KCB 
         account to pay for your outstanding loan.
         KCB Mpesa here for you.
         '''
print(msg)

text = """ Holla its your guy Marley.
           Tafuta pesa buanaaa!!!
        """
print(text)


# Slicing 
day = "Wednesday"
month = "May"
print(day[:3])
print(month[:-2])

f_name = "bob nestar" # small letters
# .upper() convert to upper case
print(f_name.upper())

s_name = "MARLEY" #
# .lower() convert to lower case
print(s_name.lower())

# concatination -converting from one data type to another
# int - > float float(x)
# float - > int int(x)
# int - > string str(x)
number = 6
print(str(number))

x = 4 #x is an integer
print(float(x))

y = 3.24
print(int(y))

f_name = "Ignacio "

s_name = "Marley"

full_name = f_name + s_name

print(full_name)

#The replace() method replaces a string with another

name = "Gregory isaacs"

print(name.replace('i','I'))

# The split 

msg = "Hello from this side of Nairobi."
print(msg.split())

print(len(msg))