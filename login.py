from tkinter import *
import tkinter as tk
global username
global password
global username_entry
global password_entry
global main_screen
main_screen = Tk()   # create a GUI window     

# define login function
def login():
    
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen,text="Login").pack()
   # Label(login_screen, text="").pack()
    #Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()
    

def register():
        
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x280")
 
 # Set text variables
    name = StringVar()
    phonenumber = IntVar()
    email = StringVar()   
    username = StringVar()
    password = StringVar()
 
 # Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
   # Label(register_screen, text="").pack()

# Set username label
    name_lable = Label(register_screen, text="name * ")
    name_lable.pack()
    
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    # Set username label
    phonenumber_lable = Label(register_screen, text="Phone number * ")
    phonenumber_lable.pack()
 
  
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()
    # Set username label
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
 
 # Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

# Set username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
 # Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
 
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()

def main_account_screen():
  
    main_screen.geometry("300x270") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window

# create a Form label 
Label(text="Choose Login Or Register For Parking", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

Button(text="Login", height="2", width="30", command = login).pack()

main_account_screen() 

Button(text="Register", height="2", width="30", command=register).pack() 
    
def register_user():
    username_entry=register()
main_screen.mainloop()