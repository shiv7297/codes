import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# Zoom In
zoom_in = cv2.resize(img, None, fx=2, fy=2)

# Zoom Out
zoom_out = cv2.resize(img, None, fx=0.5, fy=0.5)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(zoom_in, cmap='gray')
plt.title("Zoom In")

plt.subplot(1,3,3)
plt.imshow(zoom_out, cmap='gray')
plt.title("Zoom Out")

plt.show()