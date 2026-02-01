

import numpy as np
import matplotlib . pyplot as plt

R = 2000  # Ohms (increased from 1000 Ohms)
C = 2e-6  # Farads (increased from 1e-6 Farads)
V = 5     #Volts

t = np.linspace(0, 0.04, 1000) # Increased time range to observe the full discharge
Vc = V * np.exp(-t / (R*C))

plt.plot(t, Vc)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title("RC Discharging Curve with New R and C")
plt.show()

"""# New Section
Capacitor


"""