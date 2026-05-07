import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg',0)

kernel = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])

m,n = img.shape
conv = np.zeros((m-2,n-2))
corr = np.zeros((m-2,n-2))

# Flipped kernel for convolution
flip_kernel = np.flipud(np.fliplr(kernel))

for i in range(m-2):
    for j in range(n-2):

        region = img[i:i+3, j:j+3]

        # Correlation
        corr[i,j] = np.sum(region * kernel)

        # Convolution
        conv[i,j] = np.sum(region * flip_kernel)

plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(corr,cmap='gray')
plt.title("Correlation")

plt.subplot(1,3,3)
plt.imshow(conv,cmap='gray')
plt.title("Convolution")

plt.show()

print("Difference = ")
print(conv - corr)