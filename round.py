import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cm.png',0)
n= round(img.shape[1]/2)
img[:,n:]=0
plt.imshow(img,'gray')
plt.show()
