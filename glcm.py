import cv2
import numpy as np
from skimage.feature import graycomatrix
import matplotlib.pyplot as plt

# -------------------------------------------------
# LOAD IMAGE
# -------------------------------------------------

img = cv2.imread('image.jpg', 0)

# resize if needed
img = cv2.resize(img, (128,128))

# -------------------------------------------------
# COMPUTE GLCM
# distance = 1
# angle = 0 degree
# -------------------------------------------------

glcm = graycomatrix(img,
                    distances=[1],
                    angles=[0],
                    levels=256,
                    symmetric=True,
                    normed=True)

# GLCM matrix
matrix = glcm[:, :, 0, 0]

print("GLCM Matrix\n")
print(matrix)

# -------------------------------------------------
# ENERGY
# -------------------------------------------------

energy = np.sum(matrix**2)

# -------------------------------------------------
# ENTROPY
# -------------------------------------------------

entropy = 0

rows, cols = matrix.shape

for i in range(rows):
    for j in range(cols):

        if matrix[i,j] != 0:
            entropy += matrix[i,j] * np.log2(matrix[i,j])

entropy = -entropy

# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

print("\nEnergy =", energy)
print("Entropy =", entropy)

plt.imshow(matrix, cmap='gray')
plt.title("GLCM Matrix")
plt.colorbar()
plt.show()