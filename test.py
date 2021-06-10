import tkinter as tk
from itertools import count
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
import keyboard
from matplotlib import pyplot as plt

def tank(X, t, qin,A1,A2,R1,R2):
    h1, h2 = X
    qout1 = (h1 - h2) / R1
    qout2 = (h2) / R2
    dh1dt = (qin - qout1) / A1
    dh2dt = (qout1 - qout2) / A2
    dhdt = [dh1dt, dh2dt]
    return dhdt


# def old_gui(A1,A2,R1,R2,qin):
#     choice = int(
#         input(
#             f'1. Change A1\n2. Change A2\n3. Change R1\n4. Change R2\n5. Change Qin\n0. To plot graph\nYour choices:'))
#     while choice != 0:
#         if choice == 1:
#             A1 = float(input("Input A1 value:"))
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#         elif choice == 2:
#             A2 = float(input("Input A2 value:"))
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#         elif choice == 3:
#             R1 = float(input("Input R1 value:"))
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#         elif choice == 4:
#             R2 = float(input("Input R2 value:"))
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#         elif choice == 5:
#             qin = float(input("Input qin value:"))
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#         elif choice == 0:
#             print(f'\nA1 value:{A1}\nA2 value:{A2}\nR1 value:{R1}\nR2 value:{R2}\nQin value:{qin}\n')
#             break
#         else:
#             print("Input number 0 - 5 only")
#         choice = int(input(
#             f'1. Change A1\n2. Change A2\n3. Change R1\n4. Change R2\n5. Change Qin\n0.To plot graph\nYour choices:'))
#     return A1,A2,R1,R2,qin


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
    return parameter, A1_entry, A1_variable


def save_parameter():
    global A1
    if A1_entry.get():
        A1 = A1_entry.get()
    A1_variable.set(A1)


def live_data(i):
    global A1
    global A2
    global R1
    global R2
    global qin
    IC = [0, 0]
    t.append(t[-1] + 1)
    sol = odeint(tank, IC, t, args=(qin,A1,A2,R1,R2))
    x_vals.append(next(index))
    H1.append(sol[i][0])
    H2.append(sol[i][1])
    plt.cla()
    plt.plot(x_vals, H1, 'b-', label='Tank 1')
    plt.plot(x_vals, H2, 'r-', label='Tank 2')
    plt.axis([0, len(t), 0, 100])
    plt.legend(loc='upper right')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Height [m]')
    plt.title('Simulation of Two Tanks in Series')
    plt.tight_layout()


A1 = 66.4424
A2 = 66.4424
R1 = 1.575
R2 = 0.99
qin = 33.34
x_vals = [0]
H1 = [0]
H2 = [0]
t = [0]
index = count()

# parameter, A1_entry, A1_variable= gui(A1,A2,R1,R2,qin)
parameter, A1_entry, A1_variable = gui(A1, A2, R1, R2, qin)
while True:
    print("hi2")
    animation = FuncAnimation(plt.gcf(), live_data, interval=1000)
    print("hi3")
    plt.show()
