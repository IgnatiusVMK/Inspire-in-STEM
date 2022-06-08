#!usr/bin/python

####################################
#          Gui examples using ktinker
#          Name: Victor
#          Date: 7/6/2022
####################################

from tkinter import *

window = Tk()
# Add image file
#bg = PhotoImage(file = "HouseofMarley.png")
window.configure(bg='white')
# Adjust size 
window.geometry("550x450")
window.title("Python Graphical User Interface")
f_name = Label(window, text="First name" , font = ("Segoe Script",15))
s_name = Label(window, text="Second name", font = ("Segoe Script",15))

f_name.grid(column = 60, row = 100)
s_name.grid(column = 60, row = 120)

# input user-name
#btn = Button(window,text="User-name",bg='white',fg='green')
#btn.grid(column =100, row= 180)
# input password
#btn = Button(window,text="Password",bg='white',fg='green')
#btn.grid(column =70, row= 90)

f_name_box = Entry(window,width=20)
f_name_box.grid(column=100,row=100)
s_name_box = Entry(window,width=20)
s_name_box.grid(column=100,row=120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop-up")
    top.configure(bg='grey')
    msg= Label(top,text = "Welcome to", font = ("Arial "))

btn = Button(window,text="Log in",bg='Red',fg='black',command = open_popup().pack())
btn.grid(column =100, row= 130)


window.mainloop()