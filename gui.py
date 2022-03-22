### - Imports
from pydoc import text
from textwrap import fill
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import auth
import textmain
 
### - Initialization
root = Tk()
choose_subject = False
 
### - Subject Choices
math = ['Algebra 1',
   'Geometry',
   'Algebra 2',
   'Pre-Calculus'
]
 
english = ['English 1',
   'English 2',
   'AP Literature',
]
 
science = ['Biology',
   'Chemistry',
   'Physics',
]
 
social_studies = ['World History',
   'US History',
   'Government',
   'Economics'
]
 
### - Colors:
Violet = '#b7b1b2'
Purple = '#4b3d8f'
Green = '#37a987'
 
 
### - Window Parameters
root.title('StudyBuddy')
root.geometry('400x800')
root.config(bg=Violet)
root.grid()
 
### - Font
Font_Comic_Sans = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 32)
Font_Comic_Sans_Lower = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 18)
Font_Comic_Sans_Ultra_Lower = tk.font.Font(family = 'Proxima Nova', weight = 'bold', size = 14)
 
### - Functions
 
def username_sign_up():
   global new_user
   new_user = True
   login_canvas.grid_remove()
 
### - Sign-Up System
   global sign_up_canvas
   sign_up_canvas = tk.Canvas(root, bg=Violet, highlightthickness=0)
   sign_up_canvas.grid()
 
   global username
   username = tk.StringVar(sign_up_canvas)
 
   login_title = Label(sign_up_canvas, text = 'Sign Up:', bg = Violet, fg=Purple)
   login_title.config(font=Font_Comic_Sans, width=18)
   login_title.grid(pady = 35)
 
   enter_user = Label(sign_up_canvas, text = 'Username', bg = Violet, fg=Purple)
   enter_user.config(font=Font_Comic_Sans_Lower)
   enter_user.grid(pady=5)
 
   new_username = tk.Entry(sign_up_canvas, width=25, text='Username', textvariable=username, bg=Violet)
   new_username.grid(padx=80, pady=2)
 
   confirm_user = Button(sign_up_canvas, text = 'Enter', bg = Violet, fg=Purple, borderwidth=0, command=lambda:username_confirm(username.get()))
   confirm_user.config(font=Font_Comic_Sans_Lower)
   confirm_user.grid(pady=15)
 
def username_confirm(username):
   msg = auth.signup_u(username)
   global sign_in_canvas
   if msg == True:
       create_pw = True
       password_sign_up(create_pw)
   else:
       username_msg = tk.Label(sign_up_canvas, text=msg)
       username_msg.config(bg=Violet, fg=Green)
       username_msg.grid()
 
 
def password_sign_up(create_pw):
   global password
   password = tk.StringVar(sign_up_canvas)
 
   enter_pw = Label(sign_up_canvas, text = 'Password', bg = Violet, fg=Purple)
   enter_pw.config(font=Font_Comic_Sans_Lower)
   enter_pw.grid(pady=25)
 
   new_password = tk.Entry(sign_up_canvas, width=25, textvariable=password, bg=Violet)
   new_password.grid(padx=80, pady=2)
 
   confirm_pw = Button(sign_up_canvas, text = 'Sign In', bg = Violet, fg=Purple, borderwidth=0, command=lambda:password_confirm(password.get()))
   confirm_pw.config(font=Font_Comic_Sans_Lower)
   confirm_pw.grid(pady=15)
 
def password_confirm(password):
   auth.signup_p(password)
   sign_up_canvas.grid_remove()
 
   global new_account_canvas
   new_account_canvas = tk.Canvas(root)
   new_account_canvas.config(bg=Violet, highlightthickness=0)
   new_account_canvas.grid()
   congrats = tk.Label(new_account_canvas, text ='''Thank You For Making an Account''')
   congrats.config(font=Font_Comic_Sans_Lower, bg=Violet, fg=Purple)
   congrats.pack(padx=50, pady=50)
 
   home_page_after_login = tk.Button(new_account_canvas, text = 'Home Page', command=home_page)
   home_page_after_login.config(bg=Violet)
   home_page_after_login.pack()
 
   status = 'new'
   home_page(status)
 
### - Login System
 
def login_bool():
   login_canvas.grid_remove()
 
   global sign_in_canvas
   sign_in_canvas = tk.Canvas(root, bg=Violet, highlightthickness=0)
   sign_in_canvas.grid()
 
   global username
   username = tk.StringVar(sign_in_canvas)
 
   login_title = Label(sign_in_canvas, text = 'Sign In:', bg = Violet, fg=Purple)
   login_title.config(font=Font_Comic_Sans, width=18)
   login_title.grid(pady = 35)
 
   enter_user = Label(sign_in_canvas, text = 'Username', bg = Violet, fg=Purple)
   enter_user.config(font=Font_Comic_Sans_Lower)
   enter_user.grid(pady=5)
 
   new_username = tk.Entry(sign_in_canvas, width=25, text='Username', textvariable=username, bg=Violet)
   new_username.grid(padx=80, pady=2)
 
   confirm_user = Button(sign_in_canvas, text = 'Enter', bg = Violet, fg=Purple, borderwidth=0, command=lambda:username_confirm_login(username.get()))
   confirm_user.config(font=Font_Comic_Sans_Lower)
   confirm_user.grid(pady=15)
 
 
def username_confirm_login(username):
   status = auth.sign_ins_u(username)
   if status == False:
       username_msg = tk.Label(sign_in_canvas, text='Incorrect Username')
       username_msg.config(bg=Violet, fg=Green)
       username_msg.grid()
   else:
       get_password_login()
 
 
def get_password_login():
   global password
   password = tk.StringVar(sign_in_canvas)
 
   enter_pw = Label(sign_in_canvas, text = 'Password', bg = Violet, fg=Purple)
   enter_pw.config(font=Font_Comic_Sans_Lower)
   enter_pw.grid(pady=25)
 
   enter_password = tk.Entry(sign_in_canvas, width=25, textvariable=password, bg=Violet)
   enter_password.grid(padx=80, pady=2)
 
   confirm_pw = Button(sign_in_canvas, text = 'Sign In', bg = Violet, fg=Purple, borderwidth=0, command=lambda:confirm_password_login(password.get()))
   confirm_pw.config(font=Font_Comic_Sans_Lower)
   confirm_pw.grid(pady=15)
 
def confirm_password_login(password):
   auth.sign_ins_p(password)
   sign_in_canvas.grid_remove()
 
   home_page_after_login = tk.Button(sign_in_canvas, text = 'Home Page', command=home_page)
   home_page_after_login.config(bg=Violet)
   home_page_after_login.grid()
 
   status_of_user = 'old'
 
   home_page(status_of_user)
 
 
 
### - Login Page
 
login_canvas = tk.Canvas(root, bg = Violet, highlightthickness=0)
login_canvas.grid()
 
welcome = Label(login_canvas, text = 'StudyBuddy', bg = Violet, fg=Purple)
welcome.config(font=Font_Comic_Sans, width=18)
welcome.grid(pady = 50)
 
sign_up = Button(login_canvas, text = 'Sign Up', bg = Violet, fg=Purple, borderwidth=0, command=username_sign_up)
sign_up.config(font=Font_Comic_Sans_Lower)
sign_up.grid(pady=15)
 
login = Button(login_canvas, text = 'Login', bg = Violet, fg=Purple, borderwidth=0, command=login_bool)
login.config(font=Font_Comic_Sans_Lower)
login.grid(pady=15)
 
 
### - Text Windows
def home_page(status):
 
   global math_dropdown, english_dropdown, science_dropdown, social_studies_dropdown, topic, welcome
 
   if status == 'old':
       sign_in_canvas.grid_remove()
   else:
       new_account_canvas.grid_remove()
 
   print(username)
 
   welcome = Label(root, text = 'StudyBuddy', bg = Violet, fg=Purple)
   welcome.config(font=Font_Comic_Sans)
   welcome.grid(pady=50, padx = 100)
 
   topic = Label(root, text = 'Choose One Topic:', bg = Violet, fg=Purple)
   topic.config(font=Font_Comic_Sans_Lower)
   topic.grid(pady=10)
 
   math_dropdown_name = StringVar()
   math_dropdown_name.set('Math')
 
   math_dropdown = OptionMenu(root, math_dropdown_name, *math, command=start_texting)
   math_dropdown.config(bg=Violet)
   math_dropdown.grid(pady=10)
 
   english_dropdown_name = StringVar()
   english_dropdown_name.set('English')
 
   english_dropdown = OptionMenu(root, english_dropdown_name, *english, command=start_texting)
   english_dropdown.config(bg=Violet)
   english_dropdown.grid(pady=10)
 
   science_dropdown_name = StringVar()
   science_dropdown_name.set('Science')
 
   science_dropdown = OptionMenu(root, science_dropdown_name, *science, command=start_texting)
   science_dropdown.config(bg=Violet)
   science_dropdown.grid(pady=10)
 
   social_studies_dropdown_name = StringVar()
   social_studies_dropdown_name.set('Social Studies')
 
   social_studies_dropdown = OptionMenu(root, social_studies_dropdown_name, *social_studies, command=start_texting)
   social_studies_dropdown.config(bg=Violet)
   social_studies_dropdown.grid(pady=10)
 
 
def finding_person(username):
   status_person = textmain.userislooking(username)
   if status_person == True:
       text_input = tk.Entry(text_canvas, bg=Violet, textvariable=text_msg)
       text_input.pack(fill='x', side=BOTTOM)
       scrolled = ScrolledText(text_canvas, bg=Violet)
       scrolled.insert('1.0',text_msg.get())
 
   def proceedwithchat():
       from threading import Thread
       import time
       for users in (ref12.get()).keys():
           if users != username:
               scrolled.insert('1.0',"matched!\nYou are matched with user: " +str(users))
               usertotalkto = users
               time.sleep(2)
               ref12.update({username:{'looking': False}})
               break
 
 
       def sendmessage():
           #ref.update({username:{'looking':False,'chat': str(usertotalkto) + " has opened a chat with you! "}})
           chatopen = True
           while chatopen == True:
         
 
         
               texttosend = input("What do you want to say: ")
               ref12.update({username:{'looking':False,'chat': texttosend}})
               if texttosend == 'end':
                   ref12.update({username:{'looking':False,'chat':''}})
                   break
       def retrieveinfo():
           x = ""
           while True:
               if (ref12.get()[usertotalkto]) != x:
                   whattosay = str((ref12.get()[usertotalkto])).split(",")[0].split(":")[1]
                   scrolled.insert('1.0',('\n')+str(users) + " has said: "+whattosay)
                   x=(ref12.get()[usertotalkto])
 
               else:
                   x=(ref12.get()[usertotalkto])
 
               time.sleep(0.0001)
         
         
       Thread(target = retrieveinfo).start()
       Thread(target = sendmessage).start()
 
 
 
def start_texting(Subject):
 
   math_dropdown.grid_remove()
   english_dropdown.grid_remove()
   science_dropdown.grid_remove()
   social_studies_dropdown.grid_remove()
   welcome.grid_remove()
   topic.grid_remove()
 
   global text_canvas, text_msg
   text_canvas = tk.Canvas(root, bg=Violet)
   text_msg = tk.StringVar(text_canvas)
   text_canvas.pack(fill='both')
 
   start_messaging = tk.Button(text_canvas, text='Start Messaging', bg=Violet, command=lambda:finding_person(username.get()))
   start_messaging.pack(pady=10)
   #start_messaging.pack()
 
 

root.mainloop()
 
 

