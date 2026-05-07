# ============================================================
# MANUAL HISTOGRAM SPECIFICATION
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ INPUT AND REFERENCE IMAGES
# ------------------------------------------------

img = cv2.imread('image1.jpg', 0)

reference = cv2.imread('image2.jpg', 0)

reference = cv2.resize(reference, (img.shape[1], img.shape[0]))

M, N = img.shape

# ============================================================
# HISTOGRAMS
# ============================================================

hist1 = np.zeros(256)
hist2 = np.zeros(256)

for i in range(M):
    for j in range(N):

        hist1[img[i,j]] += 1
        hist2[reference[i,j]] += 1

# ============================================================
# NORMALIZED HISTOGRAMS
# ============================================================

hist1 = hist1 / (M*N)
hist2 = hist2 / (M*N)

# ============================================================
# CDF
# ============================================================

cdf1 = np.zeros(256)
cdf2 = np.zeros(256)

cdf1[0] = hist1[0]
cdf2[0] = hist2[0]

for i in range(1,256):

    cdf1[i] = cdf1[i-1] + hist1[i]
    cdf2[i] = cdf2[i-1] + hist2[i]

# ============================================================
# MAPPING
# ============================================================

mapping = np.zeros(256, dtype=np.uint8)

for i in range(256):

    diff = abs(cdf1[i] - cdf2[0])
    index = 0

    for j in range(256):

        new_diff = abs(cdf1[i] - cdf2[j])

        if new_diff < diff:

            diff = new_diff
            index = j

    mapping[i] = index

# ============================================================
# APPLY MAPPING
# ============================================================

specified = np.zeros((M,N), dtype=np.uint8)

for i in range(M):
    for j in range(N):

        specified[i,j] = mapping[img[i,j]]

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Input Image")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(reference, cmap='gray')
plt.title("Reference Image")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(specified, cmap='gray')
plt.title("Histogram Specification")
plt.axis('off')

plt.tight_layout()
plt.show()