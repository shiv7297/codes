ximport cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

threshold_value = 127

ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(thresh, cmap='gray')
plt.title("Thresholded")

plt.show()