# Lists
motorcycle_owner = "Mojo Jojo"
plate_number = [' H123A', ' Y1234', ' S1234']
motorcycle = ['honda', 'yamaha', 'suzuki']
# accesing list items using index
# print(motorcycle)
# motorcycle[1]= "Bugatti"#changing element in a list
#print("I love " + str(motorcycle[0]))
#adding element in a list
#motorcycle.append('Bugatti')#adding an item to a list append()
# task ---- print motorcycle and plate_number
#print(str(motorcycle[0] ) + str(plate_number[0]))
#print(str(motorcycle[1] ) + str(plate_number[1]))
#print(str(motorcycle[2] ) + str(plate_number[2]))
#deleting an item from a list-- del
#del motorcycle[0] #deleting an item
#print(motorcycle)
#popped_motorcycle = motorcycle.pop() #pop removes the last index
# Task -- print a statement:
# My name is Mojo Jojo and I own a motorcycle plate number
#print("My name is {} and I own a {} {} ".format(motorcycle_owner,motorcycle[0],plate_number[0]))

#Removing an item from a list
#motorcycle.remove('honda')
#print(motorcycle)

#
school = ['Joy', 'Hope', 'Mercy', 'Happy']
pupil = ['Peace', 'Patience', 'Amani','Charity']

#Hardest way
#print(f"I am {pupil[0]} from {school[0]} school")
#print(Loopsf"I am {pupil[1]} from {school[1]} school")
#print(f"I am {pupil[2]} from {school[2]} school")
#print(f"I am {pupil[3]} from {school[3]} school")

#Simplified
for pupil in pupil:
  print(f'Hello I am pupil {pupil}')

#sentence = f'Hello my name is {pupil}'

fruits = ['Orange','Apple','Banana','Guava','Pineapple']
#print(fruits[-1])

fruits[2] = 'passion'
#print(fruits[20])
