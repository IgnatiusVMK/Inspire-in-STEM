#!usr/bin/python

########################
#          Tuples
#          Name: Ignatius Victor M.K
#          Date: 31/5/2021
########################

#list
fruits = ['mango','guava','orange']

fruits[2]='apple'
print(fruits)
# Tuple
new_fruits = ('mango','Lime','guava','banana')
#new_fruits[1]='apple' #TypeError: 'tuple' object does not support item assignment
print(new_fruits[2])

cars=('audi','bmw','vw','toyota')
cars=('nissan','bmw','vw','toyota')
print(cars)

fav_foods=('nyamachoma','mutura','ugali')
for fav_food in fav_foods:
    print(fav_food)