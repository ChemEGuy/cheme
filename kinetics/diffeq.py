
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Function that contains our differential equations
def reactions(y, t, rates):
    A, B, C = y
    k1, k2 = rates
    diffeqs = [-k1*A,
                k1*A - k2*B,
                k2*B]
    return diffeqs


# Initial concentrations: A0, B0, C0
x0 = [10, 0, 0]

# Rate constants: k1, k2
rates = [1, 1]

# End time and time step
t_end = 10
t_step = 0.01

# Create array of time values
t = np.arange(0, t_end, t_step)

# Solve using odeint from scipy.integrate
soln = odeint(func=reactions, y0=x0, t=t, args=(rates,))

# Plot the results
plt.plot(t, soln[:,0])
plt.plot(t, soln[:,1])
plt.plot(t, soln[:,2])
plt.xlabel('time')
plt.ylabel('concentration')
plt.legend(['A','B','C'])
plt.show()


# Extra space
