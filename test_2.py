import tkinter as tk
import keyboard

A1 = 66.4424
A2 = 66.4424
R1 = 1.575
R2 = 0.99
qin = 33.34


def gui(A1,A2,R1,R2,qin):
    parameter = tk.Tk()
    parameter.minsize(width=400, height=400)
    parameter.title("Adjusting Parameter")
    tk.Label(parameter, text="Current Value").place(relx=0.2, rely=0.0, anchor='nw')
    tk.Label(parameter, text="New Value").place(relx=0.5, rely=0.0, anchor='nw')
    tk.Label(parameter, text = "A1").place(relx = 0.1, rely = 0.1, anchor = 'nw')
    tk.Label(parameter, text="A2").place(relx=0.1, rely=0.2, anchor='nw')
    tk.Label(parameter, text="R1").place(relx=0.1, rely=0.3, anchor='nw')
    tk.Label(parameter, text="R2").place(relx=0.1, rely=0.4, anchor='nw')
    tk.Label(parameter, text="qin").place(relx=0.1, rely=0.5, anchor='nw')

    A1_entry = tk.Entry(parameter, width = 10)
    A1_entry.place(relx = 0.5, rely = 0.1, anchor = 'nw')
    A2_entry = tk.Entry(parameter, width=10)
    A2_entry.place(relx=0.5, rely=0.2, anchor='nw')
    R1_entry = tk.Entry(parameter, width=10)
    R1_entry.place(relx=0.5, rely=0.3, anchor='nw')
    R2_entry = tk.Entry(parameter, width=10)
    R2_entry.place(relx=0.5, rely=0.4, anchor='nw')
    qin_entry = tk.Entry(parameter, width=10)
    qin_entry.place(relx=0.5, rely=0.5, anchor='nw')

    A1_variable = tk.StringVar()
    A1_variable.set(A1)
    tk.Label(parameter, textvariable = A1_variable).place(relx = 0.2, rely = 0.1, anchor = 'nw')
    A2_variable = tk.StringVar()
    A2_variable.set(A2)
    tk.Label(parameter, textvariable=A2_variable).place(relx=0.2, rely=0.2, anchor='nw')
    R1_variable = tk.StringVar()
    R1_variable.set(R1)
    tk.Label(parameter, textvariable=R1_variable).place(relx=0.2, rely=0.3, anchor='nw')
    R2_variable = tk.StringVar()
    R2_variable.set(R2)
    tk.Label(parameter, textvariable=R2_variable).place(relx=0.2, rely=0.4, anchor='nw')
    qin_variable = tk.StringVar()
    qin_variable.set(qin)
    tk.Label(parameter, textvariable=qin_variable).place(relx=0.2, rely=0.5, anchor='nw')

    tk.Button(parameter, text="Save", command=save_parameter).place(relx=0.5, rely=0.7, anchor="s")

    return parameter, A1_entry, A1_variable, A2_entry, A2_variable, R1_entry, R1_variable, R2_entry, R2_variable, qin_entry, qin_variable


def save_parameter():
    global A1
    global A2
    global R1
    global R2
    global qin
    if A1_entry.get():
        A1 = A1_entry.get()
    if A2_entry.get():
        A2 = A2_entry.get()
    if R1_entry.get():
        R1 = R1_entry.get()
    if R2_entry.get():
        R2 = R2_entry.get()
    if qin_entry.get():
        qin = qin_entry.get()
    A1_variable.set(A1)
    A2_variable.set(A2)
    R1_variable.set(R1)
    R2_variable.set(R2)
    qin_variable.set(qin)

parameter, A1_entry, A1_variable, A2_entry, A2_variable, R1_entry, R1_variable, R2_entry, R2_variable, qin_entry, qin_variable= gui(A1,A2,R1,R2,qin)
parameter.mainloop()
