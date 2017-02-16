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
	return m*g*R*np.cos(theta)-0.5*m*omega**2*R**2*(np.sin(theta))**2

#plt.plot()

