# ============================================================
# RECONSTRUCT IMAGE USING ONLY FEW DCT BASIS IMAGES
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

# Resize small for manual computation
img = cv2.resize(img, (32, 32))

M, N = img.shape

# ============================================================
# MANUAL DCT
# ============================================================

dct = np.zeros((M, N))

for u in range(M):
    for v in range(N):

        if u == 0:
            cu = np.sqrt(1/M)
        else:
            cu = np.sqrt(2/M)

        if v == 0:
            cv = np.sqrt(1/N)
        else:
            cv = np.sqrt(2/N)

        sum_value = 0

        for x in range(M):
            for y in range(N):

                term1 = np.cos(((2*x + 1) * u * np.pi) / (2*M))
                term2 = np.cos(((2*y + 1) * v * np.pi) / (2*N))

                sum_value += img[x, y] * term1 * term2

        dct[u, v] = cu * cv * sum_value

# ============================================================
# RECONSTRUCT USING ONLY FEW BASIS IMAGES
# ============================================================

reconstructed = np.zeros((M, N))

# ------------------------------------------------
# KEEP ONLY SELECTED BASIS IMAGES
# Example:
# (0,0) -> DC component
# (1,0) -> horizontal variation
# ------------------------------------------------

selected_basis = [(0,0), (1,0)]

for x in range(M):
    for y in range(N):

        sum_value = 0

        for (u,v) in selected_basis:

            if u == 0:
                cu = np.sqrt(1/M)
            else:
                cu = np.sqrt(2/M)

            if v == 0:
                cv = np.sqrt(1/N)
            else:
                cv = np.sqrt(2/N)

            basis = (
                cu * cv *
                np.cos(((2*x + 1) * u * np.pi) / (2*M)) *
                np.cos(((2*y + 1) * v * np.pi) / (2*N))
            )

            sum_value += dct[u,v] * basis

        reconstructed[x,y] = sum_value

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed using 2 Basis Images")
plt.axis('off')

plt.tight_layout()
plt.show()