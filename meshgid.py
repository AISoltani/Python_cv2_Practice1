import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

p=cv2.imread('cm.png',0)
m= round(p.shape[0]/2)
n= round(p.shape[1]/2)
k=np.arange(-m,m)
k1=np.arange(-n,n)
x,y=np.meshgrid(k,k1)
#z=np.exp(-(x**2+y**2)/10000)
z=(x+y)/5
q=p*z
plt.imshow(q,'gray')
plt.show()




