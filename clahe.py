# ============================================================
# CLAHE
# ============================================================

import cv2
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

# ============================================================
# APPLY CLAHE
# ============================================================

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

clahe_img = clahe.apply(img)

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(clahe_img, cmap='gray')
plt.title("CLAHE Image")
plt.axis('off')

plt.tight_layout()
plt.show()







# ============================================================
# MANUAL CLAHE (SIMPLIFIED VERSION)
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# READ IMAGE
# ------------------------------------------------

img = cv2.imread('image.jpg', 0)

# Resize for simplicity
img = cv2.resize(img, (256,256))

M, N = img.shape

# ============================================================
# PARAMETERS
# ============================================================

tile_size = 32
clip_limit = 40

output = np.zeros((M,N), dtype=np.uint8)

# ============================================================
# PROCESS EACH TILE
# ============================================================

for row in range(0, M, tile_size):
    for col in range(0, N, tile_size):

        # ------------------------------------------------
        # EXTRACT TILE
        # ------------------------------------------------

        tile = img[row:row+tile_size, col:col+tile_size]

        h, w = tile.shape

        # ------------------------------------------------
        # HISTOGRAM
        # ------------------------------------------------

        hist = np.zeros(256)

        for i in range(h):
            for j in range(w):

                pixel = tile[i,j]
                hist[pixel] += 1

        # ------------------------------------------------
        # CLIPPING
        # ------------------------------------------------

        excess = 0

        for i in range(256):

            if hist[i] > clip_limit:

                excess += hist[i] - clip_limit
                hist[i] = clip_limit

        # ------------------------------------------------
        # REDISTRIBUTE EXCESS
        # ------------------------------------------------

        redistribute = excess // 256

        for i in range(256):

            hist[i] += redistribute

        # ------------------------------------------------
        # NORMALIZE HISTOGRAM
        # ------------------------------------------------

        hist = hist / (h*w)

        # ------------------------------------------------
        # COMPUTE CDF
        # ------------------------------------------------

        cdf = np.zeros(256)

        cdf[0] = hist[0]

        for i in range(1,256):

            cdf[i] = cdf[i-1] + hist[i]

        # ------------------------------------------------
        # TRANSFORMATION FUNCTION
        # ------------------------------------------------

        transform = np.zeros(256)

        for i in range(256):

            transform[i] = round(255 * cdf[i])

        # ------------------------------------------------
        # APPLY TRANSFORMATION
        # ------------------------------------------------

        equalized_tile = np.zeros((h,w), dtype=np.uint8)

        for i in range(h):
            for j in range(w):

                equalized_tile[i,j] = transform[tile[i,j]]

        # ------------------------------------------------
        # PLACE TILE BACK
        # ------------------------------------------------

        output[row:row+h, col:col+w] = equalized_tile

# ============================================================
# DISPLAY
# ============================================================

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(output, cmap='gray')
plt.title("Manual CLAHE")
plt.axis('off')

plt.tight_layout()
plt.show()