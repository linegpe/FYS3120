import numpy as np
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,xlabel,ylabel

m = 1
R = 1
g = 1
omega = 1.5

def Hamiltonian(theta,p):
	return p**2/(2*m*R) - m*g*R*np.cos(theta) - 0.5*m*omega**2*R**2*(np.sin(theta))**2

x = np.arange(-np.pi,np.pi,0.1)
y = np.arange(-2.5,2.5,0.1)
X,Y = meshgrid(x, y) # grid of point
Z = Hamiltonian(X, Y) # evaluation of the function on the grid

cset = contour(X,Y,Z,np.arange(-1.5,1.5,0.1),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=15)
colorbar()
xlabel("Theta",fontsize=15)
ylabel("Momentum",fontsize=15)
show()