import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('cm.jpg',0)
n = (img.shape[1]/2)
img[:,round(n)-1:round(n)+1] = 255
plt.imshow(img,'gray')
plt.show()

