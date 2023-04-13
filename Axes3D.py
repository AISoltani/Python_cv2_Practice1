import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure()
ax=fig.add_subplot(111,projection='3d')
k = np.arange(-10,10,0.1)
x,y=np.meshgrid(k,k)

z=np.exp(-(x**2+y**2))
ax.plot_surface(x,y,z)
plt.show()
