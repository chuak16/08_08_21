import tkinter as tk
from itertools import count
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from xlsxwriter import Workbook

def tank(X, t, qin,A1,A2,R1,R2):
    h1, h2 = X
    qout1 = (h1 - h2) / R1
    qout2 = (h2) / R2
    dh1dt = (qin - qout1) / A1
    dh2dt = (qout1 - qout2) / A2
    dhdt = [dh1dt, dh2dt]
    return dhdt


def gui(A1,A2,R1,R2,qin):
    parameter = tk.Tk()
    parameter.minsize(width=1000, height=500)
    parameter.title("Adjusting Parameter")
    tk.Label(parameter, text="Current Value").place(relx=0.15, rely=0.05, anchor='nw')
    tk.Label(parameter, text="New Value").place(relx=0.25, rely=0.05, anchor='nw')
    tk.Label(parameter, text = "A1").place(relx = 0.1, rely = 0.1, anchor = 'nw')
    tk.Label(parameter, text="A2").place(relx=0.1, rely=0.2, anchor='nw')
    tk.Label(parameter, text="R1").place(relx=0.1, rely=0.3, anchor='nw')
    tk.Label(parameter, text="R2").place(relx=0.1, rely=0.4, anchor='nw')
    tk.Label(parameter, text="qin").place(relx=0.1, rely=0.5, anchor='nw')
    A1_entry = tk.Entry(parameter, width = 10)
    A1_entry.place(relx = 0.25, rely = 0.1, anchor = 'nw')
    A2_entry = tk.Entry(parameter, width=10)
    A2_entry.place(relx=0.25, rely=0.2, anchor='nw')
    R1_entry = tk.Entry(parameter, width=10)
    R1_entry.place(relx=0.25, rely=0.3, anchor='nw')
    R2_entry = tk.Entry(parameter, width=10)
    R2_entry.place(relx=0.25, rely=0.4, anchor='nw')
    qin_entry = tk.Entry(parameter, width=10)
    qin_entry.place(relx=0.25, rely=0.5, anchor='nw')
    A1_variable = tk.StringVar()
    A1_variable.set(A1)
    tk.Label(parameter, textvariable = A1_variable).place(relx = 0.15, rely = 0.1, anchor = 'nw')
    A2_variable = tk.StringVar()
    A2_variable.set(A2)
    tk.Label(parameter, textvariable=A2_variable).place(relx=0.15, rely=0.2, anchor='nw')
    R1_variable = tk.StringVar()
    R1_variable.set(R1)
    tk.Label(parameter, textvariable=R1_variable).place(relx=0.15, rely=0.3, anchor='nw')
    R2_variable = tk.StringVar()
    R2_variable.set(R2)
    tk.Label(parameter, textvariable=R2_variable).place(relx=0.15, rely=0.4, anchor='nw')
    qin_variable = tk.StringVar()
    qin_variable.set(qin)
    tk.Label(parameter, textvariable=qin_variable).place(relx=0.15, rely=0.5, anchor='nw')
    tk.Button(parameter, text="Change Value", command=save_parameter).place(relx=0.22, rely=0.6, anchor="s")
    return parameter, A1_entry, A1_variable, A2_entry, A2_variable, R1_entry, R1_variable, R2_entry, R2_variable, qin_entry, qin_variable


def save_parameter():
    global A1
    global A2
    global R1
    global R2
    global qin
    if A1_entry.get():
        A1 = float(A1_entry.get())
    if A2_entry.get():
        A2 = float(A2_entry.get())
    if R1_entry.get():
        R1 = float(R1_entry.get())
    if R2_entry.get():
        R2 = float(R2_entry.get())
    if qin_entry.get():
        qin = float(qin_entry.get())
    A1_variable.set(A1)
    A2_variable.set(A2)
    R1_variable.set(R1)
    R2_variable.set(R2)
    qin_variable.set(qin)


def live_data(i):
    global A1
    global A2
    global R1
    global R2
    global qin
    IC = [0, 0]
    x_vals.append(next(index))
    sol = odeint(tank, IC, x_vals, args=(qin,A1,A2,R1,R2))
    H1.append(sol[i][0])
    H2.append(sol[i][1])
    plt.cla()
    plt.plot(x_vals, H1, 'b-', label='Tank 1')
    plt.plot(x_vals, H2, 'r-', label='Tank 2')
    plt.legend(loc='upper right')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Height [m]')
    plt.title('Simulation of Two Tanks in Series')


A1 = 66.4424
A2 = 66.4424
R1 = 1.575
R2 = 0.99
qin = 33.34
x_vals = []
H1 = []
H2 = []
index = count()

parameter, A1_entry, A1_variable, A2_entry, A2_variable, R1_entry, R1_variable, R2_entry, R2_variable, qin_entry, qin_variable= gui(A1,A2,R1,R2,qin)
canvas = FigureCanvasTkAgg(plt.gcf(), master=parameter)
canvas.get_tk_widget().place(relx=0.35, rely=0.0, anchor='nw')
animation = FuncAnimation(plt.gcf(), live_data, interval=10)
parameter.mainloop()

df=pd.DataFrame({'time':x_vals,'Height Tank 1 ':H1, 'Height Tank 2':H2})
writer=pd.ExcelWriter('Tank.xlsx',engine='xlsxwriter')
export_data=df.to_excel(writer,sheet_name='Tank')
writer.save()