# 1. Initialize graphics and import libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import time

# 2. Fix parameter values
A1 = 66.4424
A2 = 66.4424
R1 = 1.575
R2 = 0.99
qin = 33.34


# 3. Write a function to evaluate RHS of the differential equations
def tank(X, t, qin=0):
    h1, h2 = X
    qout1 = (h1 - h2) / R1
    qout2 = (h2) / R2
    dh1dt = (qin - qout1) / A1
    dh2dt = (qout1 - qout2) / A2
    # print(t)
    # print(qin)
    # print([dh1dt, dh2dt])
    dhdt = [dh1dt, dh2dt]
    return dhdt


# 4. Choose initial conditions and time grid
IC = [0, 0]
t = np.linspace(0, 100, 100)

# 5. Perform the simulation by numerical solution of the differential equations
sol = odeint(tank, IC, t, args=(qin,))
H1 = np.zeros(100)
H2 = np.zeros(100)
# print(H1)
# 6. Prepare visualizations and post-processing
for i in range(len(t)):
    plt.clf()
    H1[i] = H1[i] + sol[i][0]
    H2[i] = H2[i] + sol[i][1]
    # print(H1[i])
    plt.figure(1)
    plt.plot(t, H1, 'b-', label='Tank 1')
    plt.plot(t, H2, 'r-', label='Tank 2')
    plt.axis([0, 100, 0, 100])
    plt.legend(loc='upper right')
    plt.xlabel('Time')
    plt.ylabel('Height [m]')
    plt.title('Simulation of Two Tanks in Series')
    # plt.show()
    time.sleep(0.01)
# print(t, H1, H2)
plt.show()
# 7 Date extraction from Python to Microsoft Excel

# df = pd.DataFrame({'time': t, 'Height Tank 1 ': H1, 'Height Tank 2': H2})
# writer = pd.ExcelWriter('Tank.xlsx', engine='xlsxwriter')
# export_data = df.to_excel(writer, sheet_name='Tank')
# writer.save()