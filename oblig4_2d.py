import numpy as np
import matplotlib.pyplot as plt
import math

# Defining constants
g = 1
R = 1
omega_er = np.sqrt(g/R)
omega = [0.5,1.5]
N = 100
theta = np.linspace(-np.pi,np.pi,N)
m = 1
#potential = np.zeros(N)

def potential(theta,omega):
	return -m*g*R*np.cos(theta)-0.5*m*omega**2*R**2*(np.sin(theta))**2

hold="on"
plt.xlabel("Theta",fontsize=15)
plt.ylabel("Potential",fontsize=15)
plt.plot(theta,potential(theta,omega[0]),label="omega=0.5")
plt.plot(theta,potential(theta,omega[1]),label="omega=1.5")
plt.legend(fontsize=15)
plt.show()