# ============================================================
# MANUAL HIGH PASS FILTER
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

# Small size for manual computation
img = cv2.resize(img, (32,32))

M, N = img.shape

# ============================================================
# MANUAL DFT
# ============================================================

dft = np.zeros((M,N), dtype=complex)

for u in range(M):
    for v in range(N):

        sum_value = 0

        for x in range(M):
            for y in range(N):

                angle = -2j * np.pi * ((u*x/M) + (v*y/N))

                sum_value += img[x,y] * np.exp(angle)

        dft[u,v] = sum_value

# ============================================================
# MANUAL SHIFT
# ============================================================

shifted = np.zeros((M,N), dtype=complex)

for u in range(M):
    for v in range(N):

        new_u = (u + M//2) % M
        new_v = (v + N//2) % N

        shifted[new_u,new_v] = dft[u,v]

# ============================================================
# HIGH PASS FILTER
# Remove center frequencies
# ============================================================

filtered = shifted.copy()

center_x = M // 2
center_y = N // 2

size = 5

for i in range(center_x - size, center_x + size):
    for j in range(center_y - size, center_y + size):

        filtered[i,j] = 0

# ============================================================
# MANUAL INVERSE SHIFT
# ============================================================

inverse_shift = np.zeros((M,N), dtype=complex)

for u in range(M):
    for v in range(N):

        old_u = (u + M//2) % M
        old_v = (v + N//2) % N

        inverse_shift[old_u,old_v] = filtered[u,v]

# ============================================================
# MANUAL IDFT
# ============================================================

reconstructed = np.zeros((M,N), dtype=complex)

for x in range(M):
    for y in range(N):

        sum_value = 0

        for u in range(M):
            for v in range(N):

                angle = 2j * np.pi * ((u*x/M) + (v*y/N))

                sum_value += inverse_shift[u,v] * np.exp(angle)

        reconstructed[x,y] = sum_value / (M*N)

reconstructed = np.abs(reconstructed)

# ============================================================
# MAGNITUDE SPECTRUM
# ============================================================

magnitude = np.log(1 + np.abs(filtered))

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(12,8))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(magnitude, cmap='gray')
plt.title("High Pass Spectrum")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(reconstructed, cmap='gray')
plt.title("High Pass Filtered")
plt.axis('off')

plt.tight_layout()
plt.show()