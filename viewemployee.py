from tkinter import Tk
from tkinter import *
from tkinter import messagebox


class View:
    """ View
            This class is declared for vieweing the details of employee
    """
    def __init__(self, window):
        self.wn = window
        self.wn.geometry('480x200+500+300')
        self.wn.title("All Employees")
        self.wn.resizable(False, False)
        self.employee_details = []
        with open("C:\\Users\\User\\PycharmProjects\\gettingstarted1\\employees\\Registration_Details.txt") as all_employees:
            for lines in all_employees:
                self.employee_details.append(lines.split(","))
        self.allemployees_window()

    def allemployees_window(self):
        self.search_id = StringVar(self.wn)
        Label(self.wn, text="Enter your Employee ID", font=("Times New Roman", 16)).place(x=30, y=49)
        Entry(self.wn, text="Enter ID", textvariable=self.search_id, font=("Times New Roman", 16),width=24).place(x=28, y=100)
        Button(self.wn, text="Search", font=("Times New Roman", 16, "underline"), bg="#4169E1", fg="white", command = self.search_employee,width=10).place(x=300, y=92)

    def search_employee(self):
        i = 0
        for employee in self.employee_details:
            print(self.search_id.get())
            print(employee[0])
            if self.search_id.get() == employee[0]:
                self.create_new_win(employee)
                break
            else:
                i += 1
        else:
            messagebox.showerror("ERROR","No Employee on the database.")

    def create_new_win(self, employee):
        new = Tk()
        new.title("Employee_department_details")
        new.geometry('600x450')
        new.config(background="#F8F8FF")

        main_title = Label(new, text="Details About Employee and Department", font=("Times New Roman", 16, "underline"),
                            bg="#4169E1",
                            fg="white", width="46",
                            height="2").place(x=18, y=20)

        details_line = ['Employee ID','Gender','Name', 'Email','Contact','Age','Address','Department']
        y=100
        count=0
        for details in employee:
            Label(new, text=details_line[count], font=("Times New Roman", 16),bg="#e6e6e6", fg="#4169E1",
                            activebackground="#4169E1", activeforeground="white",
                            state=ACTIVE, width = 15).place(x=10, y=y)
            Label(new, text = ":", font=("Times New Roman", 16), bg="#e6e6e6", fg="#4169E1",
                            activebackground="#4169E1", activeforeground="#000000",
                            state=ACTIVE).place(x=170, y=y)
            Label(new, text=details, font=("Times New Roman", 16)).place(x=220,y=y)
            y += 40
            count += 1

        new.mainloop()



