# ============================================================
# MANUAL HISTOGRAM EQUALIZATION
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

M, N = img.shape

# ============================================================
# HISTOGRAM
# ============================================================

hist = np.zeros(256)

for i in range(M):
    for j in range(N):

        pixel = img[i,j]
        hist[pixel] += 1

# ============================================================
# NORMALIZED HISTOGRAM
# ============================================================

hist_norm = hist / (M*N)

# ============================================================
# CDF (CUMULATIVE DISTRIBUTION FUNCTION)
# ============================================================

cdf = np.zeros(256)

cdf[0] = hist_norm[0]

for i in range(1,256):

    cdf[i] = cdf[i-1] + hist_norm[i]

# ============================================================
# TRANSFORMATION FUNCTION
# ============================================================

transform = np.zeros(256)

for i in range(256):

    transform[i] = round(255 * cdf[i])

# ============================================================
# APPLY TRANSFORMATION
# ============================================================

equalized = np.zeros((M,N), dtype=np.uint8)

for i in range(M):
    for j in range(N):

        equalized[i,j] = transform[img[i,j]]

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(equalized, cmap='gray')
plt.title("Histogram Equalized")
plt.axis('off')

plt.tight_layout()
plt.show()

# ============================================================
# HISTOGRAM PLOTS
# ============================================================

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(hist)
plt.title("Original Histogram")

# Equalized histogram
hist2 = np.zeros(256)

for i in range(M):
    for j in range(N):

        hist2[equalized[i,j]] += 1

plt.subplot(1,2,2)
plt.plot(hist2)
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()