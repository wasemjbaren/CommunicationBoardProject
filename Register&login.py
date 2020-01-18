import Requests
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import shutil
import os
import glob
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
user = 0
try:
    file = open('connected.txt', 'r')
    user = int(file.read())
except (FileNotFoundError, ValueError):
    user = 0


root = tk.Tk()
root.title('Communication board')
main = tk.Frame(root)

class variables:
    def __init__(self):
        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()
        self.FIRSTNAME = tk.StringVar()
        self.LASTNAME = tk.StringVar()
        self.ISADMIN = tk.StringVar()
        self.PHONE = tk.StringVar()
        self.NAME = tk.StringVar()
        self.CITY = tk.StringVar()
        self.BIRTHDAY = tk.StringVar()
        self.SITS = tk.StringVar()
        self.ENTRY = tk.StringVar()
        self.DATE = tk.StringVar()

    def resetVariables(self):
        self.USERNAME.set("")
        self.PASSWORD.set("")
        self.FIRSTNAME.set("")
        self.LASTNAME.set("")
        self.ISADMIN.set("")
        self.PHONE.set("")
        self.PHONE.set("")
        self.NAME.set("")
        self.CITY.set("")
        self.BIRTHDAY.set("")
        self.SITS.set("")
        self.ENTRY.set("")
        self.DATE.set("")
vars = variables()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width
height =screen_height
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

def RegisterForm(flag):
    RegisterFrame = tk.Frame(root)
    RegisterFrame.pack(side=tk.TOP, pady=40)
    lbl_username = tk.Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = tk.Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = tk.Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = tk.Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_rule = tk.Label(RegisterFrame, text="Is Admin?:", font=('arial', 18), bd=18)
    lbl_rule.grid(row=5)
    lbl_phone = tk.Label(RegisterFrame, text="Phone", font=('arial', 18), bd=18)
    lbl_phone.grid(row=6)
    lbl_result2 = tk.Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=7, columnspan=2)
    username = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
    username.grid(row=1, column=1)
    password = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    rule = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.ISADMIN, width=15)
    rule.grid(row=5, column=1)
    rule = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.PHONE, width=15)
    rule.grid(row=6, column=1)
    register = tk.Button(RegisterFrame, text="Register", font=('arial', 18), width=35)#need command
    register.bind('<Button-1>', lambda event, frame=RegisterFrame, flag=flag: Register(frame, flag))
    register.grid(row=7, columnspan=2, pady=20)
    if flag:
        login = tk.Button(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        login.grid(row=0, sticky=tk.W)
        login.bind('<Button-1>', lambda event, frame=RegisterFrame: ToggleToLogin(RegisterFrame))
    else:
        back_button(RegisterFrame)


def LoginForm():
    LoginFrame = tk.Frame(root)
    LoginFrame.pack(side=tk.TOP, pady=80)
    s=0
    try:
        f = open('connected.txt', 'r')
        f = f.read()
        s = int(f)
    except (FileNotFoundError, ValueError):
        s = 0
    if s != 0:
        toggle_to_main_page(LoginFrame, False)
    else:
        l = tk.Label(LoginFrame, text="Communication Board", fg='red', font=('arial', 40), bd=18)
        l.grid(row=0)
        lbl_username = tk.Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = tk.Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = tk.Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = tk.Entry(LoginFrame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
        username.grid(row=1, column=1)
        password = tk.Entry(LoginFrame, font=('arial', 20), textvariable=vars.PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = tk.Button(LoginFrame, text="Login", font=('arial', 18), width=35)#updated
        btn_login.grid(row=4, columnspan=2, pady=20)
        btn_reg = tk.Button(LoginFrame, text="Forgot Password", font=('arial', 18), width=35)
        btn_reg.grid(row=5, columnspan=2, pady=20)
        lbl_register = tk.Button(LoginFrame, text="Register", font=('arial', 18), width=35)
        lbl_register.grid(row=6, columnspan=2)
        lbl_register.bind('<Button-1>', lambda event, frame=LoginFrame: ToggleToRegister(frame, True))
        btn_login.bind('<Button-1>', lambda event, frame=LoginFrame, flag=True: toggle_to_main_page(LoginFrame, True))
        btn_reg.bind('<Button-1>', lambda event, frame=LoginFrame: toggle_to_forgot(LoginFrame))


def ForgotForm():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    lbl_message = tk.Label(frame, text='Please Enter the following information', font=('arial', 25), bd=18)
    lbl_message.grid(row=1)
    lbl_username = tk.Label(frame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=2)
    lbl_phone = tk.Label(frame, text="Phone: ", font=('arial', 25), bd=18)
    lbl_phone.grid(row=3)
    lbl_pass = tk.Label(frame, text="new password", font=('arial', 25), bd=18)
    lbl_pass.grid(row=4)
    username = tk.Entry(frame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
    username.grid(row=2, column=1)
    phone = tk.Entry(frame, font=('arial', 20), textvariable=vars.PHONE, width=15)
    phone.grid(row=3, column=1)
    password = tk.Entry(frame, font=('arial', 20), textvariable=vars.PASSWORD, width=15)
    password.grid(row=4, column=1)
    login = tk.Button(frame, text="Login", fg="Blue", font=('arial', 12))
    login.grid(row=0, sticky=tk.W)
    login.bind('<Button-1>', lambda event, frame=frame: ToggleToLogin(frame))



    reset = tk.Button(frame, text="Reset Password", font=('arial', 12), width=35)
    reset.grid(row=5, sticky=tk.W)
    reset.bind('<Button-1>', lambda event, frame=frame: resetPass(frame))


def resetPass(frame):
    if(Requests.ResetPass(vars.USERNAME.get(), vars.PHONE.get(), vars.PASSWORD.get())):
        vars.resetVariables()
        frame.destroy()
        LoginForm()
    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')





def ToggleToLogin(frame):
    frame.destroy()
    LoginForm()
