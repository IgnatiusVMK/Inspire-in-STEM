#!usr/bin/python

########################
#          File operation commands
#          Name: Ignatius Victor M.K
#          Date: -/6/2021
########################
f  = open("lesson.txt") # equivalent to 'r' or 'rt'
f =open("lesson.txt",'w') # wi

#opening file
with open("lesson.txt",'w' ) as f:
    f.write("This is my new wfile\n")
    f.write("Call me Marely")
    f.write("Today is on a Monday")

"""
r opens a file for reading.(default)
w Opens a file for writing. Creates a new file
x opens a file for exclusive creation. If the
a opens a file for appending at the end of the filoe
t Opens in tect mode . (default) #we can read and write text to the file
b Opens in binary mode.
+ opens a file for updating (reading and writing)
"""