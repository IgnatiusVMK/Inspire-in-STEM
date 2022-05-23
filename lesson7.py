#!usr/bin/python

########################
#          Dictionaries
#          Name: 
#          Date: 24/5/2021
########################

# Initializing dictionaries

student = {"Name":"Mwai","age": 19,"gender":"male"}
print(student['Name'])
print(student['age'])
print(student['gender'])

# adding key value pairs 

student["iDNo"] = "21018642"
student["Hobby"] = "Netflix"
student["Favorite-food"] = "Muturaaa!"

#print(student)

#Initialize empty dictionary
student_1 = {}
student_1["fav_food"] = "Nyama choma"
student_1["Home_city"] = "Kahawa Sukari"

print(student_1)

#modyfing values 
student["Name"] = "Kariuki"

#print(student)

# Removing key value pairs

del student["Favorite-food"]
print(student)

print()