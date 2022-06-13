#!usr/bin/python

########################
#          Dictionary in dictionary
#          Name: Ignatius Victor M.K
#          Date: 16/5/2021
########################
billy_fav_food = ['beef','chicken','vegetable']
gin_fav_food = ['rice','ugali','potatoes']

# dictionary containing the above
food = {
     'billy':['beef','chicken','vegetable'],
     'gin':['rice','ugali','potatoes'],
      }

#create dictionary in dictionary 
#---- person..mary(name,email,password)
#person = {
       #  "mary = {
       #          'name':'Ignacio_marley',
       #          'gender':'Male',
       #          'phone_number':'+254790884584',
       #          'address':'67891 K-Sukari' }
        # }

fav_food = {
        'mary':['ugali','nyama','choma'],
        'jane':['chips']
          }

###............ Looping over dictionaries
for key, value in fav_food.items(): 
      print(f"{mary}:{}")