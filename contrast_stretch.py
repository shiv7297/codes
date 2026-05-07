import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

r1 = np.min(img)
r2 = np.max(img)

stretch = ((img - r1) / (r2 - r1)) * 255
stretch = np.array(stretch, dtype=np.uint8)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(stretch, cmap='gray')
plt.title("Contrast Stretching")

plt.show()