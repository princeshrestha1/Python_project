from tkinter import *
from tkinter import messagebox


mywindowd = Tk()
mywindowd.geometry("1100x650")
mywindowd.title("Employee and Department Form")
mywindowd.resizable(False, False)
mywindowd.config(background="#F8F8FF")

frame1 = Frame(mywindowd)
frame1.config(height=650, width=550, background="#F5F5F5")
frame1.place(x=0, y=0)

frame2 = Frame(mywindowd)
frame2.config(height=650, width=550)
frame2.place(x=550, y=0)
main_title = Label(frame2, text="Department Form", font=("Times New Roman", 16, "underline"), bg="#4169E1", fg="white",
                   width="40",
                   height="2").place(x=25, y=30)
main_title1 = Label(frame1, text="Employee Register Form", font=("Times New Roman", 16, "underline"), bg="#4169E1",
                    fg="white", width="40",
                    height="2").place(x=25, y=30)



department = Label(frame2, text="Department", bg="white", fg="white", activebackground="#F5F5F5",
                   activeforeground="#000000", state=ACTIVE)
department.place(x=228, y=110)
departmentcode = Label(frame2, text="Department code", bg="#F5F5F5")
departmentcode.place(x=215, y=170)

department_name = StringVar()
department_entry = Entry(frame2, textvariable=department_name, width="30")
department_entry.place(x=175, y=135)

department_code = StringVar()
department_code_entry = Entry(frame2, textvariable=department_code, width="30")
department_code_entry.place(x=175, y=195)


employee_id = StringVar(mywindowd)
# password = StringVar()
employee_name = StringVar(mywindowd)
age = StringVar(mywindowd)
email = StringVar(mywindowd)
contact = StringVar(mywindowd)
address = StringVar(mywindowd)
department_info = StringVar(mywindowd)
drop_down = StringVar(mywindowd)


def send_data():
    try:
        employee_identity_info = employee_id.get()
        employee_name_info = employee_name.get()
        gender_info = gender.get()
        department_information = drop_down.get()
        age_info = str(age.get())
        email_info = email.get()
        contact_info = contact.get()
        address_info = address.get()
        with open("employees/Registration_Details.txt", "a+") as file:
            file.write(employee_identity_info + ',')
            file.write(employee_name_info + ',')
            file.write(gender_info + ',')
            file.write(email_info + ',')
            file.write(contact_info + ',')
            file.write(age_info + ',')
            file.write(address_info + ',')
            file.write(department_information + '\n')
        messagebox.showinfo("Done", "Employee Registered")
    except:
        messagebox.showinfo('error','invalid inputs')
    # with open("employees/Registration_Details.txt", "a+") as file:
    #     file.write(employee_identity_info + ',')
    #     file.write(employee_name_info + ',')
    #     file.write(gender_info + ',')
    #     file.write(email_info + ',')
    #     file.write(contact_info + ',')
    #     file.write(age_info + ',')
    #     file.write(address_info + ',')
    #     file.write(department_information + '\n')
    #
    # messagebox.showinfo("Done", "Employee Registered")


def settozero():

    employeeid_entry.delete(0, END)
    male.deselect()
    female.deselect()
    # password_entry.delete(0, END)
    username_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    department_entry.delete(0, END)
    department_code_entry.delete(0, END)
    drop_down.set("Choose Department")


def department_details():
    with open("departments.txt", "a+") as departments:
        departments.write(str(department_code.get()) + "\n")
        departments.write(department_name.get())
    messagebox.showinfo("Done", "Department added")
    # settozero()
    mywindowd.destroy()


employee_identity_label = Label(frame1, text="Employee ID", bg="white", fg="white", activebackground="#F5F5F5",
                           activeforeground="#000000", state=ACTIVE)
employee_identity_label.place(x=21, y=89)
username_label = Label(frame1, text="Employee Name", bg="#F5F5F5")
username_label.place(x=21, y=169)
age_label = Label(frame1, text="Age", bg="#F5F5F5")
age_label.place(x=325, y=89)
email_label = Label(frame1, text="Email", bg="#F5F5F5")
email_label.place(x=325, y=169)
contact_label = Label(frame1, text="Contact No.", bg="#F5F5F5")
contact_label.place(x=325, y=219)
address_label = Label(frame1, text="Address", bg="#F5F5F5")
address_label.place(x=21, y=269)
department_name_label = Label(frame1, text="Department", bg="#F5F5F5")
department_name_label.place(x=325, y=269)

OPTIONS = ['Manager', 'Asssistant Manager', 'Teller', 'Director', 'Head Manager', 'Finance Department']
drop_down.set('Choose Department')
droplist = OptionMenu(frame1, drop_down, *OPTIONS)
droplist.config(width=19)
droplist.place(x=325, y=292)

employeeid_entry = Entry(frame1, textvariable=employee_id, width="35")
username_entry = Entry(frame1, textvariable=employee_name, width="35")
age_entry = Entry(frame1, textvariable=age, width="35")
email_entry = Entry(frame1, textvariable=email, width="35")
contact_entry = Entry(frame1, textvariable=contact, width="35")
address_entry = Entry(frame1, textvariable=address, width="35")

employeeid_entry.place(x=23, y=115)
username_entry.place(x=23, y=195)
age_entry.place(x=325, y=115)
email_entry.place(x=325, y=195)
contact_entry.place(x=325, y=243)
address_entry.place(x=23, y=292)

gender = StringVar()
male = Radiobutton(frame1, text='Male', variable=gender, value='Male')
male.place(x=23, y=140)
female = Radiobutton(frame1, text='Female', variable=gender, value='Female')

female.place(x=115, y=140)

submit_btn = Button(mywindowd, text="Submit Here", width="15", height="2", command=send_data, bg="#e6e6e6",
                    fg="#4169E1", activebackground="#4169E1", activeforeground="white",
                    state=ACTIVE)
submit_btn.place(x=25, y=500)

submitdepartmentdetails = Button(frame2, text="Add Here", width="20", height="2", bg="#e6e6e6", fg="#4169E1",
                                 activebackground="#4169E1", activeforeground="white",
                                 state=ACTIVE, command=department_details)
submitdepartmentdetails.place(x=197, y=255)

quitButton = Button(mywindowd, text='Quit', width="15", height="2", command=mywindowd.quit, bg="#e6e6e6",
                    fg="#4169E1", activebackground="#4169E1", activeforeground="white",
                    state=ACTIVE)
quitButton.place(x=220, y=500)

reset = Button(mywindowd, text='Reset', width="15", height="2", command=settozero, bg="#e6e6e6", fg="#4169E1",
               activebackground="#4169E1", activeforeground="white",
               state=ACTIVE)
reset.place(x=410, y=500)

clear = Button(frame2, text='Clear', width="20", height="2", command=settozero, bg="#e6e6e6", fg="#4169E1",
               activebackground="#4169E1", activeforeground="white",
               state=ACTIVE)
clear.place(x=197, y=315)

mywindowd.mainloop()
