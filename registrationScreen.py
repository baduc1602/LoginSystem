# Import message and (*) All libraries from Tkinter library
from tkinter import *
from tkinter import messagebox

# Import Regular Expression (email validation) and OS (moving to the next screen)
import re
import os

# Create the main window of our application, we have Tk class.
window = Tk()

window.title("Welcome to User Registration Screen")

# set the size of the window
window.geometry('500x500')

# set its background color
window.configure(background="light blue")

v_fName = StringVar()
v_password = StringVar()
v_cofirmPassword = StringVar()
v_phoneNo = StringVar()
v_email = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_skills = StringVar()

# Label widget implements a display box where you can place text or images
lb_heading = Label(window, text="Registration Screen", width=20, font=("bold", 20), bg="light blue")
lb_heading.place(x=90, y=53)

lb_fullname = Label(window, text="Full Name", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80, y=130)
# Entry will allow User to enter any kind of values like numbers, string, special characters
entry_fullname = Entry(window, textvariable=v_fName)
entry_fullname.place(x=240, y=130)

lb_password = Label(window, text="Password", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80, y=170)
entry_password = Entry(window, textvariable=v_password)
entry_password.place(x=240, y=170)

lb_confirmPassword = Label(window, text="Confirm password", width=20, font=("bold", 10), bg="light blue")
lb_confirmPassword.place(x=80, y=210)
entry_confirmPassword = Entry(window, textvariable=v_cofirmPassword)
entry_confirmPassword(x=240, y=210)

lb_phoneno = Label(window, text="Phone No.", width=20, font=("bold", 10), bg="light blue")
lb_phoneno.place(x=80, y=250)
entry_phoneno = Entry(window, textvariable=v_phoneNo)
entry_phoneno.place(x=240, y=250)

lb_email = Label(window, text="Email", width=20, font=("bold", 10), bg="light blue")
lb_email.place(x=80, y=290)
entry_email = Entry(window, textvariable=v_email)
entry_email.place(x=240, y=290)
