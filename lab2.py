import numpy as np
import matplotlib.pyplot as plt

R = 1000
C = 1e-6
V = 5

t = np.linspace(0, 0.01, 1000)
Vc = V * (1 - np.exp(-t / (R * C)))

plt.plot(t, Vc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Charging Curve")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

V = 10.0
R = 1000.0
C = 0.001

tau = R * C
t = np.linspace(0, 5 * tau, 100)

Vc_charge = V * (1 - np.exp(-t / (R * C)))
Vc_discharge = V * np.exp(-t / (R * C))

plt.figure(figsize=(8, 5))
plt.plot(t, Vc_charge, color="blue", label="Charging")
plt.plot(t, Vc_discharge, color="red", label="Discharging")
plt.title("Capacitor Voltage vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)
plt.show()
