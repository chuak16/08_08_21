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
    tk.Label(parameter, text = "A1").place(relx = 0.1, rely = 0.1, anchor = 'nw')
    A1_entry = tk.Entry(parameter, width = 10)
    A1_entry.place(relx = 0.4, rely = 0.1, anchor = 'nw')
    A1_variable = tk.StringVar()
    A1_variable.set(A1)
    tk.Label(parameter, textvariable = A1_variable).place(relx = 0.2, rely = 0.1, anchor = 'nw')
    tk.Button(parameter, text="Save", command=save_parameter).place(relx=0.5, rely=0.6, anchor="s")
    print("hi")
    return parameter, A1_entry, A1_variable


def save_parameter():
    global A1
    if A1_entry.get():
        A1 = A1_entry.get()
    A1_variable.set(A1)
    print("hi2")



parameter, A1_entry, A1_variable= gui(A1,A2,R1,R2,qin)
while True:
    if keyboard.is_pressed("p"):
        parameter.mainloop()
