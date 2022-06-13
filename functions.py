#!usr/bin/python

########################
#          Functions
#          Name: Ignatius Victor M.K
#          Date: 31/5/2021
########################

#-->block of code which gets executed together
 #-- Initialize the function
 #-- calling the function

#defining a function/initializing

def say_hello():
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
#say_hello()

def bark():
    print("Dogs bark woof woof")
def meow():
    print("Cats meow")
def roar():
    print("Lions roar")
#bark()
#meow()
#roar()

##### <-----function parameters-----> ####
 #-->function to add two numbers
def add_numbers(x,y): #x,y are called parameters
    sum_nums = x + y
    print("The sum of numbers:",sum_nums)
#add_numbers(40,50)
#add_numbers(100,400)
#add_numbers(558,856)

  #-->function to multiply two numbers
def multiply_nums(x,y):
    prod_nums = x * y
    print("The product of numbers:",prod_nums)
#multiply_nums(8,5)
#multiply_nums(80,58)

#!usr/bin/python

########################
#          Functions
#          Name: 
#          Date:  3/6/2021
########################

# Using default parameters

def print_name(name="Ignatius VMK"):
    print(name)
#print_name("Marley")
#print_name()

# returning from a function

def get_sum(num1, num2):
    sum_nums = num1 + num2
    return sum_nums

#print(get_sum(5,8))

# -- >Write a function that gets the square of numbers
#def square_num(number):
  #  square_num = number ** 2
 #   return square_num

#print(square_num)

# -- >Write a function that gets the powers of numbers
def powers(number, power):
    pow_numb = number **power
    return pow_numb
#print(powers(6,4))

def get_full_name(f_name, s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
#print(get_full_name("Ignatius " ,"Kariuki"))

# Returning a dictionary

def create_full_name(f_name,s_name):
    person = {'first':'f_name', 'second':'s_name'}
    return person 

student = create_full_name('Ignatius','Kariuki')
#print(student)

# Parsing a list in a function
def greet_friends(names): # The "names" in the brackets is a list\
    for name in names:
        msg = "Hello, " + name.title() + " !"
        print (msg) 
friends = ['Bob', 'Johnte','Sam']
greet_friends(friends)