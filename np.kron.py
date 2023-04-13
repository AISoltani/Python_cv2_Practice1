import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.ones((200,20))
colors = np.linspace(0,255,10)
img = np.kron(colors,img)
plt.imshow(img,'gray')
plt.show()
