from tkinter import *
import os
from tkinter import messagebox as m_box
import Home_add_view


class Register:

    def register(self):
        global regwin
        regwin = Toplevel(mainwindow)
        regwin.geometry("549x470")
        regwin.title("Registration Form Page")
        regwin.resizable(False, False)
        regwin.config(background="#F8F8FF")
        main_title = Label(regwin, text="Registration Form", font=("Times New Roman", 16, "underline"), bg="#4169E1",
                           fg="white", width="500",
                           height="2")
        main_title.pack()

        global username
        global password
        global username_entry
        global password_entry

        Label(regwin, text="Please enter your details below", font=("Arial", 12), bg="#4169E1", fg="white", width="500",
              height="1").pack()
        Label(regwin, text="").pack()
        username_label = Label(regwin, text="Username", bg="#F5F5F5")
        username_label.place(x=244, y=160)
        password_label = Label(regwin, text="Password", bg="#F5F5F5")
        password_label.place(x=245, y=210)

        password = StringVar()
        username = StringVar()

        password_entry = Entry(regwin, textvariable=password, width="40")
        username_entry = Entry(regwin, textvariable=username, width="40")

        username_entry.place(x=155, y=185)
        password_entry.place(x=155, y=235)

        registration_btn = Button(regwin, text="Register Here", width="25", height="2", bg="#e6e6e6", fg="#4169E1",
                                  activebackground="#4169E1", activeforeground="white",
                                  state=ACTIVE, command=registrtonsuccess)
        registration_btn.place(x=185, y=305)

        reset = Button(regwin, text='Reset', width="25", height="2", command=settozero, bg="#e6e6e6", fg="#4169E1",
                       activebackground="#4169E1", activeforeground="white",
                       state=ACTIVE)
        reset.place(x=185, y=365)

        regwin.mainloop()


r1 = Register()


def settozero():
    password_entry.delete(0, END)
    username_entry.delete(0, END)


def login():
    global loginwin
    global username
    global password

    global username_verify
    global pwd_verify

    username_verify = StringVar()
    pwd_verify = StringVar()

    global e1
    global e2

    loginwin = Toplevel(mainwindow)
    loginwin.geometry("549x470")
    loginwin.title("Registration Form Page")
    loginwin.resizable(False, False)
    loginwin.config(background="#F8F8FF")
    main_title = Label(loginwin, text="Login Form", font=("Times New Roman", 16, "underline"), bg="#4169E1",
                       fg="white", width="500",
                       height="3")
    main_title.pack()

    username_label = Label(loginwin, text="Username", bg="#F5F5F5")
    username_label.place(x=244, y=160)
    username_verify = StringVar()
    e1 = Entry(loginwin, textvariable=username_verify, width="40")
    e1.place(x=155, y=185)
    pwd_verify = StringVar()
    password_label = Label(loginwin, text="Password", bg="#F5F5F5")
    password_label.place(x=245, y=210)

    e2 = Entry(loginwin, show="*", textvariable=pwd_verify, width="40")
    e2.place(x=155, y=235)
    verifyy = Button(loginwin, text="Verify", width="25", height="2", bg="#e6e6e6", fg="#4169E1",
                     activebackground="#4169E1", activeforeground="white",
                     state=ACTIVE, command=loginverification)
    verifyy.place(x=185, y=305)
    #
    # add = Button(loginwin, text="Add", width="25", height="2", bg="#e6e6e6", fg="#4169E1", activebackground="#4169E1",
    #              activeforeground="white",
    #              state=ACTIVE, command=employee_reg)
    # add.place(x=195, y=365)

    loginwin.mainloop()


def employee_reg():
    import employee_department_form


def registrtonsuccess():
    global success

    username_info = username.get()
    password_info = password.get()
    print(password_info, username_info)

    if username_info == '' or password_info == '':
        m_box.showerror('Error', 'Fill all the entries')
    elif len(password_info) < 6:
        m_box.showerror('Error', 'Password must be six digit')
    elif len(username_info) < 6:
        m_box.showerror('Error', 'Username must be six digit')
    else:
        file = open(username_info, "w")
        file.write(username_info)
        file.write(',')
        file.write(password_info)
        file.write(',\n')
        file.close()
        print(" New user registered.  Password: {} | Username: {}".format(password_info, username_info))
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        m_box.showinfo('success','Registration Success')


def loginverification():
    username = username_verify.get()
    password = pwd_verify.get()
    e1.delete(0, END)
    e2.delete(0, END)

    listof_files = os.listdir()
    if username in listof_files:
        with open(username, "r") as user:
            user_pass = user.readlines()[0]
            print(user_pass)
            if password in user_pass:
                loginissucess()
            else:
                wrongpassword()

    else:
        print("user not found")
        usernotregistered()


def loginissucess():
    global loginsuccesswin
    loginsuccesswin = Toplevel(loginwin)
    loginsuccesswin.title("Success")
    loginsuccesswin.geometry("150x100")
    Label(loginsuccesswin, text="Login is Successful").pack()
    Button(loginsuccesswin, text="OK", command=move_to_home).pack()
def move_to_home():
    mainwindow.destroy()
    new = Tk()
    home = Home_add_view.Home(new)
    new.mainloop()

def wrongpassword():
    global wrongpasscodewin
    wrongpasscodewin = Toplevel(loginwin)
    wrongpasscodewin.title("Success")
    wrongpasscodewin.geometry("150x100")
    Label(wrongpasscodewin, text="Invalid Password ").pack()
    Button(wrongpasscodewin, text="OK", command=deletewrongpassword).pack()


def usernotregistered():
    global usernotregstrdwin
    usernotregstrdwin = Toplevel(loginwin)
    usernotregstrdwin.title("usernotregistrdSuccess")
    usernotregstrdwin.geometry("150x100")
    Label(usernotregstrdwin, text="User Not Found").pack()
    Button(usernotregstrdwin, text="OK", command=deleteusernotregistrd).pack()


def deleteloginissuccess():
    loginsuccesswin.destroy()


def deletewrongpassword():
    wrongpasscodewin.destroy()


def deleteusernotregistrd():
    usernotregstrdwin.destroy()


def usermanagescreen():
    global mainwindow
    mainwindow = Tk()
    mainwindow.geometry("590x410")
    mainwindow.title("User Management")
    mainwindow.resizable(False, True)
    mainwindow.config(background="#F8F8FF")
    main_title = Label(text="Login/Register Form", font=("Times New Roman", 16, "underline"), bg="#4169E1", fg="white",
                       width="500",
                       height="2")
    loginbutton = Button(mainwindow, text="LOGIN", height=3, width=30, bg="#e6e6e6", fg="#4169E1",
                         activebackground="#4169E1", activeforeground="white",
                         state=ACTIVE, command=login)
    loginbutton.place(x=187, y=155)
    registerbutton = Button(mainwindow, text="REGISTRATION", height=3, width=30, bg="#e6e6e6", fg="#4169E1",
                            activebackground="#4169E1", activeforeground="white",
                            state=ACTIVE, command=r1.register)
    registerbutton.place(x=187, y=230)
    main_title.pack()

    mainwindow.mainloop()


usermanagescreen()
