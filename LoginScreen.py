from tkinter import *
from tkinter import messagebox

import os

window = Tk()
window.title("Welcome to User Login Screen")

window.geometry("500x500")
window.configure(background="light blue")

v_fullName = StringVar()
v_password = StringVar()

def validateUser(user_fName, user_password):
    if user_fName == "admin" and user_password == "admin":
        return True
    else:
        return False

def validateAllFields():
    if v_fullName.get() == "":
        messagebox.showinfo("Information", "Please enter FullName to Proceed.")
    elif v_password.get() == "":
        messagebox.showinfo("Information", "Please enter Password to Proceed.")
    else:
        status = validateUser(v_fullName.get(), v_password.get())
        if status:
            messagebox.showinfo("Information", "Congragulations, Login Success")
        else:
            messagebox.showinfo("Information", "Invalid Credentials")

def clearAllFields():
    v_fullName.set("")
    v_password.set("")

def callNewScreen():
    window.destroy()
    os.system("python RegistrationScreen.py")


lb_heading = Label(window, text="Login Screen", width=20, font=("bold", 20), bg="light blue" )
lb_heading.place(x=90, y=53)

lb_fullName = Label(window, text="FullName", width=20, font=("bold", 10), bg="light blue")
lb_fullName.place(x=80, y=130)
entry_fullName = Entry(window, textvariable=v_fullName)
entry_fullName.place(x=240, y=130)

lb_password = Label(window, text="Password", width=20, font=("bold", 10), bg="light blue")
lb_password.place(x=80, y=170)
entry_password = Entry(window, textvariable=v_password)
entry_password.place(x=240, y=170)

btn_login = Button(window, text="LOGIN", command=validateAllFields ,font=("bold", 10), bg="dark blue", fg="white").place(x=120, y=210)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, font=("bold", 10), bg="dark blue", fg="white").place(x=200, y=210)
btn_newUser = Button(window, text="New User", command=callNewScreen, font=("bold", 10), bg="dark blue", fg="white").place(x=280, y=210)

window.mainloop()