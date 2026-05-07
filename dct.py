# ============================================================
# MANUAL 2D DCT FOR A GRAYSCALE IMAGE
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

# Resize for faster computation
img = cv2.resize(img, (64, 64))

M, N = img.shape

# ============================================================
# MANUAL 2D DCT
# ============================================================

dct = np.zeros((M, N))

for u in range(M):
    for v in range(N):

        # Alpha values
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
# LOG-SCALED DCT COEFFICIENTS
# ============================================================

dct_log = np.log(1 + np.abs(dct))

# ============================================================
# MANUAL IDCT
# ============================================================

reconstructed = np.zeros((M, N))

for x in range(M):
    for y in range(N):

        sum_value = 0

        for u in range(M):
            for v in range(N):

                # Alpha values
                if u == 0:
                    cu = np.sqrt(1/M)
                else:
                    cu = np.sqrt(2/M)

                if v == 0:
                    cv = np.sqrt(1/N)
                else:
                    cv = np.sqrt(2/N)

                term1 = np.cos(((2*x + 1) * u * np.pi) / (2*M))
                term2 = np.cos(((2*y + 1) * v * np.pi) / (2*N))

                sum_value += cu * cv * dct[u, v] * term1 * term2

        reconstructed[x, y] = sum_value

# ============================================================
# DISPLAY RESULTS
# ============================================================

plt.figure(figsize=(12,8))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(dct_log, cmap='gray')
plt.title("DCT Coefficients")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed Image")
plt.axis('off')

plt.tight_layout()
plt.show()