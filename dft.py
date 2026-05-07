# ============================================================
# 1. IMPLEMENT 2D DFT MANUALLY FOR A GRAYSCALE IMAGE
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Read image in grayscale
# -----------------------------
img = cv2.imread('image.jpg', 0)

# Resize for faster manual DFT
img = cv2.resize(img, (64, 64))

M, N = img.shape

# ============================================================
# MANUAL 2D DFT
# ============================================================

dft = np.zeros((M, N), dtype=complex)

for u in range(M):
    for v in range(N):

        sum_value = 0

        for x in range(M):
            for y in range(N):

                angle = -2j * np.pi * ((u*x/M) + (v*y/N))

                sum_value += img[x, y] * np.exp(angle)

        dft[u, v] = sum_value

# ============================================================
# SHIFT ZERO FREQUENCY TO CENTER
# ============================================================

# ============================================================
# MANUAL FFT SHIFT USING LOOPS ONLY
# ============================================================

import numpy as np

M, N = dft.shape

shifted = np.zeros((M, N), dtype=complex)

for u in range(M):
    for v in range(N):

        # Shift indices
        new_u = (u + M//2) % M
        new_v = (v + N//2) % N

        shifted[new_u, new_v] = dft[u, v]

# ============================================================
# MANUAL INVERSE SHIFT USING LOOPS ONLY
# ============================================================

inverse_shift = np.zeros((M, N), dtype=complex)

for u in range(M):
    for v in range(N):

        # Reverse shift indices
        old_u = (u + M//2) % M
        old_v = (v + N//2) % N

        inverse_shift[old_u, old_v] = shifted[u, v]

# ============================================================
# MAGNITUDE SPECTRUM
# ============================================================

magnitude = np.abs(dft_shift)

# Log scaling
magnitude_log = np.log(1 + magnitude)

# ============================================================
# PHASE SPECTRUM
# ============================================================

phase = np.angle(dft_shift)

# ============================================================
# MANUAL IDFT
# ============================================================

reconstructed = np.zeros((M, N), dtype=complex)

# Undo shift
idft_input = np.fft.ifftshift(dft_shift)

for x in range(M):
    for y in range(N):

        sum_value = 0

        for u in range(M):
            for v in range(N):

                angle = 2j * np.pi * ((u*x/M) + (v*y/N))

                sum_value += idft_input[u, v] * np.exp(angle)

        reconstructed[x, y] = sum_value / (M * N)

# Take real values
reconstructed = np.real(reconstructed)

# ============================================================
# DISPLAY RESULTS
# ============================================================

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(magnitude_log, cmap='gray')
plt.title("DFT Magnitude Spectrum")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(phase, cmap='gray')
plt.title("DFT Phase Spectrum")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed Image")
plt.axis('off')

plt.tight_layout()
plt.show()