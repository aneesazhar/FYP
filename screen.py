import tkinter
from tkinter import *
import screen_client

root = Tk()
root.geometry("300x200")
label_student = Label(root, text="Student")
label_student.grid(row=0, column=0)
name = Entry()
name.grid(row=2, column=1)

teacher_ip = Entry(root)
teacher_ip.grid(row=4, column=1)
label_name = Label(root, text="Name =")
label_name.grid(row=2, column=0)
label_teacher_ip = Label(root, text="Ip Address(Teacher) =")
label_teacher_ip.grid(row=4, column=0)

mybutton = Button(root, text="Connect", command=lambda: main_button())
mybutton.grid(row=6, column=1)

myinstruction = Label(root, text="After connecting, press q to exit")
myinstruction.grid(row=6, column=0)

mylabel = Label(root, text="   ")
mylabel.grid(row=3, column=0)
mylabel = Label(root, text="   ")
mylabel.grid(row=5, column=1)
mylabel = Label(root, text="   ")
mylabel.grid(row=1, column=0)


def main_button():
    root.destroy()
    screen_client.student_screen_show()


root.mainloop()
