import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = np.linspace(-10, 10, 100)
n = int(input())
y = 1/(1+X**(2*n))
plt.plot(y)
plt.show()
