import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cm.jpg',0)
img = np.concatenate((img,img),1)
img1 = np.concatenate((img,img),0)
plt.imshow(img,'gray')
plt.figure()
plt.imshow(img1,'gray')
plt.show()
