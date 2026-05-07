import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# ---------------- LOG TRANSFORM ----------------
c = 255 / np.log(1 + np.max(img))
log_img = c * np.log(1 + img)
log_img = np.array(log_img, dtype=np.uint8)

# ---------------- INVERSE LOG TRANSFORM ----------------
inv_log = np.exp(img / 255.0) - 1
inv_log = (inv_log / np.max(inv_log)) * 255
inv_log = np.array(inv_log, dtype=np.uint8)

# ---------------- POWER LAW (GAMMA) TRANSFORM ----------------
gamma = 0.5
power_img = np.array(255 * (img / 255) ** gamma, dtype='uint8')

plt.figure(figsize=(10,7))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(2,2,2)
plt.imshow(log_img, cmap='gray')
plt.title("Log Transform")

plt.subplot(2,2,3)
plt.imshow(inv_log, cmap='gray')
plt.title("Inverse Log")

plt.subplot(2,2,4)
plt.imshow(power_img, cmap='gray')
plt.title("Power Law")

plt.show()