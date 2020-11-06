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

def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo("Information", "Please Enter Fullname to Proceed")
    elif v_password.get() == "":
        messagebox.showinfo("Information", "Please Enter Password to Proceed")
    elif v_cofirmPassword.get() == "":
        messagebox.showinfo("Information", "Please Confirm Password to Proceed")
    elif v_phoneNo.get() == "":
        messagebox.showinfo("Information", "Please Enter Phone Number to Proceed")
    elif len(v_phoneNo.get()) != 10:
        messagebox.showinfo("Information", "Please Enter 10 digit Phone Number to Proceed")
    elif v_email.get() == "":
        messagebox.showinfo("Information", "Please Enter Email ID to Proceed")
    elif v_gender == 0:
        messagebox.showinfo("Information", "Please Select Gender to Proceed")
    elif v_country.get() == "":
        messagebox.showinfo("Information", "Please Enter Country to Proceed")
    elif var1_skill.get() == 0 and var2_skill.get() == 0 and var3_skill.get() == 0:
        messagebox.showinfo("Information", "Please Select Skills to Proceed")
    elif v_password.get() != v_cofirmPassword.get():
        messagebox.showinfo("Information", "Password Missmatch")

def clearAllFields():
    v_fName.set("")
    v_password.set("")
    v_cofirmPassword.set("")
    v_phoneNo.set("")
    v_email.set("")

def callNewScreen():
    window.destroy()
    os.system("python LoginScreen.py")


# Label widget implements a display box where you can place text or images
lb_heading = Label(window, text="Registration Screen", width=20, font=("bold", 20), bg="light blue")
lb_heading.place(x=90, y=53)

lb_fullname = Label(window, text="Full Name", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80, y=130)
# Entry will allow User to enter any kind of values like numbers, string, special characters
entry_fullname = Entry(window, textvariable=v_fName)
entry_fullname.place(x=240, y=130)

lb_password = Label(window, text="Password", width=20, font=("bold", 10), bg="light blue")
lb_password.place(x=80, y=170)
entry_password = Entry(window, textvariable=v_password)
entry_password.place(x=240, y=170)

lb_confirmPassword = Label(window, text="Confirm password", width=20, font=("bold", 10), bg="light blue")
lb_confirmPassword.place(x=80, y=210)
entry_confirmPassword = Entry(window, show="*", textvariable=v_cofirmPassword)
entry_confirmPassword.place(x=240, y=210)

lb_phoneNo = Label(window, text="Phone No.", width=20, font=("bold", 10), bg="light blue")
lb_phoneNo.place(x=80, y=250)
entry_phoneNo = Entry(window, textvariable=v_phoneNo)
entry_phoneNo.place(x=240, y=250)

# validate_phoneNo = window.register(validate_phoneno(v_phoneNo))
# entry_phoneNo.config(validate="key", validateCommand=(validate_phoneNo, "%P"))



lb_email = Label(window, text="Email", width=20, font=("bold", 10), bg="light blue")
lb_email.place(x=80, y=290)
entry_email = Entry(window, textvariable=v_email)
entry_email.place(x=240, y=290)

lb_gender = Label(window, text="Gender", width=20, font=("bold", 10), bg="light blue")
lb_gender.place(x=80, y=330)
Radiobutton(window, text="Male", bg="light blue", padx=5, variable=v_gender, value=1).place(x=230, y=330)
Radiobutton(window, text="Female", bg="light blue", padx=5, variable=v_gender, value=2).place(x=290, y=330)

lb_country = Label(window, text="Country", width=20, font=("bold", 10), bg="light blue")
lb_country.place(x=80, y=370)
list_country = {"India", "Viet Nam", "UK", "Germany", "USA"};

# List_country shows all items in the list vertically in drop down, if we remove * it will show all items in horizontally
droplist = OptionMenu(window, v_country, *list_country)
droplist.config(width=16, bg= "light blue")
v_country.set("Select Your Country")
droplist.place(x=240, y=370)

lb_skills=Label(window, text="Skills", width=20, font=("bold",10), bg="light blue")
lb_skills.place(x=80, y=410)
var1_skill=IntVar()
Checkbutton(window, text="Java", bg="light blue", variable=var1_skill).place(x=230, y=410)
var2_skill=IntVar()
Checkbutton(window, text="Python", bg="light blue", variable=var2_skill).place(x=290, y=410)
var3_skill=IntVar()
Checkbutton(window, text=".Net", bg="light blue", variable=var3_skill).place(x=360, y=410)

btn_register = Button(window, text="REGISTER", command=validateAllFields, bg="dark blue", fg="white", font=("bold", 10)).place(x=150, y=450)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, bg="dark blue", fg="white", font=("bold", 10)).place(x=250, y=450)
btn_existinguser = Button(window, text="Existing User?", command=callNewScreen, bg="dark blue", fg="white", font=("bold", 10)).place(x=330, y=450)

window.mainloop()