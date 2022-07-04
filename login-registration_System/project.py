from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('350x500')
w.title('Login')
w.resizable(0,0)

j=0
r=0
for i in range(100):
    c=str(222222+r)
    Frame(w,width=10,height=500,bg='#'+c).place(x=j,y=0)
    j=j+10
    r=r+1

Frame(w,width=250,height=400,bg='white').place(x=50,y=50)

#label
l1=Label(w,text='Username',bg='white')
l=('conosole',13) # font,text size
l1.config(font=1)
l1.place(x=80,y=200)

e1=Entry(w,width=20,border=0)
e1.config(font=1)
e1.place(x=80,y=230)

#label 2
l2=Label(w,text='Password',bg='white')
l=('conosole',13) # font,text size
l2.config(font=1)
l2.place(x=80,y=280)

e2=Entry(w,width=20,border=0)
e2.config(font=1)
e2.place(x=80,y=310)

Frame(w,width=180,height=2,bg="#141414").place(x=80,y=250)
Frame(w,width=180,height=2,bg="#141414").place(x=80,y=330)

from PIL import ImageTk,Image

image1=Image.open(log.PNG)
image2=ImageTk.PhotoImage(image1)

label1=Label(image=image2,border=0,justify=CENTER)
label1.place(x=115,y=50)

def cmd():
    if e1.get()=='Marley' and e2.get()=='Marley':
        messagebox.showinfo("Log-IN Successful","            WELCOME        ")
        q=Tk()
        q.mainloop()
    else:
        messagebox.showinfo("Log-In FAILED","         Please try again        ")

Button(w,width=20,height=2,fg='white',bg='#994422',border=0,command=cmd,text="L O G I N").place(x=100,y=375)


w.mainloop()