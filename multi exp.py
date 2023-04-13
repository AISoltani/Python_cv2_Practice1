import cv2
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,100)

z = np.exp(-X)
z1 = np.exp(-3*X)


plt.plot(z1)
plt.plot(z)
plt.show()
