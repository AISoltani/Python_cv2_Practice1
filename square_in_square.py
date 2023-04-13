import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((200,200))
img[50:150,50:150] = 128
img[75:125,75:125] = 256

plt.imshow(img,'gray')
plt.show()
