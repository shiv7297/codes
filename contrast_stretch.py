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




import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# Piecewise contrast stretching points
r1 = 70
s1 = 0

r2 = 140
s2 = 255

stretch = np.zeros_like(img)

rows, cols = img.shape

for i in range(rows):
    for j in range(cols):

        r = img[i,j]

        # Region 1
        if r <= r1:
            stretch[i,j] = (s1/r1) * r

        # Region 2
        elif r1 < r <= r2:
            stretch[i,j] = ((s2-s1)/(r2-r1)) * (r-r1) + s1

        # Region 3
        else:
            stretch[i,j] = ((255-s2)/(255-r2)) * (r-r2) + s2

stretch = np.array(stretch, dtype=np.uint8)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(stretch, cmap='gray')
plt.title("Piecewise Stretching")

plt.show()