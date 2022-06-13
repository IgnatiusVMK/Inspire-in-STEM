#!usr/bin/python

########################
#          Dictionaries
#          Name: Ignatius Victor M.K
#          Date: 25/5/2021
########################

### -------------What are dictionaries:
    #A dictionary is a collection of a key value pairs
### -------------Syntax for dictionaries:
    #Dictionary = {'key':'value'}
### -------------Define, Add,Remove:
#names = ['John','Mary']
colors = {'color':'red'}
vehicle = {'type':'Toyota','plate_number':'TYT6789'}
   # print(type(names)) #We use the type method to determine data types
#print(type(vehicle))
#print(vehicle['type'],vehicle['plate_number']) # You can access the value 
#print(vehicle['plate_number'])

#dictionary2; person
person = {'name':'Ignacio_marley',
          'gender':'Male',
          'phone_number':'+254790884584',
          'address':'67891 K-Sukari'
          }
person['age'] = '19'
person['fav_color'] = 'black'
del person['phone_number']

#print(person['name'],person['gender'],person['age'])
#print(type(person))
#print(person)
###............ Looping over dictionaries
#for key, value in person.items():
 #   print(f"{value}:{key}")

# ------Dictionaries in Dictionaries,Lists in Dictionaries,Dictionaries in listsform
# Methods;--- #print() , #form(), #input()-----arguments go inside the brackets
print(person.get('password', 'The \'location\' key is non-existent'))
#Using get to access the value in a dictionary