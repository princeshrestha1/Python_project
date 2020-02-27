from tkinter import *
import viewemployee


class Home:
    def __init__(self, window):
        self.wn = window
        self.wn.geometry("520x320")
        self.wn.title("Home Page of Add and View of Employee and Department ")
        self.wn.resizable(False, False)
        self.wn.config(background="#F8F8FF")
        self.create_fields()

    def create_fields(self):
        Button(self.wn, text="Add Employee Registration Form", command = self.eprf, font=("Times New Roman", 16), bg="#4169E1", fg="white",
                   width="34",
                   height="2").place(x=48, y=80)
        Button(self.wn, text="View Employee and Department Details", command=self.view_employee, font=("Times New Roman", 16), bg="#4169E1", fg="white",
                   width="34",
                   height="2").place(x=48, y=160)

    def eprf(self):
        import employee_department_form


    def view_employee(self):
        # self.wn.destroy()
        new = Tk()
        viewemployee.View(new)
        new.mainloop()

