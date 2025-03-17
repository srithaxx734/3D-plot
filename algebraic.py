import matplotlib.pyplot as plt
import numpy as np
b=plt.axes(projection="3d")

# x=[10,20,30,40,50,60,70,80,90]
# y=[24,68,74,78,89,23,53,75,35]

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
x,y=np.meshgrid(x,y)
# z=2*x**2 +4*y**2 -5*y -400   #QUADRATIC EQUATION
# z=2*x**3 +4*y**2 -5*y -400   # CUBIC EQUATION
z=2*x**4 +4*y**3 -5*y -400   #QUATRIC EQUATION
g=plt.colormaps()

k=random.choice(g)
b.set_title(f"colour pick : {k}")
b.plot_surface(x,y,z,cmap=k)   #viridis,plasma,inferno,magma
b.set_xlabel("X AXIS")
b.set_ylabel("Y AXIS")
plt.show()
