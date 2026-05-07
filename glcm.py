import cv2
import numpy as np
from skimage.feature import graycomatrix
import matplotlib.pyplot as plt

# -------------------------------------------------
# LOAD IMAGE
# -------------------------------------------------

img = cv2.imread('image.jpg', 0)

# resize if needed
img = cv2.resize(img, (128,128))

# -------------------------------------------------
# COMPUTE GLCM
# distance = 1
# angle = 0 degree
# -------------------------------------------------

glcm = graycomatrix(img,
                    distances=[1],
                    angles=[0],
                    levels=256,
                    symmetric=True,
                    normed=True)

# GLCM matrix
matrix = glcm[:, :, 0, 0]

print("GLCM Matrix\n")
print(matrix)

# -------------------------------------------------
# ENERGY
# -------------------------------------------------

energy = np.sum(matrix**2)

# -------------------------------------------------
# ENTROPY
# -------------------------------------------------

entropy = 0

rows, cols = matrix.shape

for i in range(rows):
    for j in range(cols):

        if matrix[i,j] != 0:
            entropy += matrix[i,j] * np.log2(matrix[i,j])

entropy = -entropy

# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

print("\nEnergy =", energy)
print("Entropy =", entropy)

plt.imshow(matrix, cmap='gray')
plt.title("GLCM Matrix")
plt.colorbar()
plt.show()





import numpy as np

def compute_glcm(image, distances, angles, levels=16, symmetric=True, normed=True):
    """
    Manually compute GLCM (Gray Level Co-occurrence Matrix)
    """

    h, w = image.shape

    # shape => (levels, levels, num_distances, num_angles)
    glcm = np.zeros((levels, levels, len(distances), len(angles)),
                    dtype=np.float64)

    for d_idx, distance in enumerate(distances):

        for a_idx, angle in enumerate(angles):

            # Calculate offset using angle
            dx = int(round(np.cos(angle) * distance))
            dy = int(round(np.sin(angle) * distance))

            for row in range(h):
                for col in range(w):

                    new_row = row + dy
                    new_col = col + dx

                    # Check bounds
                    if (0 <= new_row < h) and (0 <= new_col < w):

                        i = image[row, col]
                        j = image[new_row, new_col]

                        glcm[i, j, d_idx, a_idx] += 1

                        # Make symmetric
                        if symmetric:
                            glcm[j, i, d_idx, a_idx] += 1

            # Normalize
            if normed:
                total = np.sum(glcm[:, :, d_idx, a_idx])
                if total > 0:
                    glcm[:, :, d_idx, a_idx] /= total

    return glcm


def compute_glcm_property(glcm, prop):
    """
    Manually compute GLCM properties
    """

    levels = glcm.shape[0]
    num_distances = glcm.shape[2]
    num_angles = glcm.shape[3]

    result = np.zeros((num_distances, num_angles))

    for d in range(num_distances):
        for a in range(num_angles):

            P = glcm[:, :, d, a]

            value = 0

            if prop == 'contrast':

                for i in range(levels):
                    for j in range(levels):
                        value += ((i - j) ** 2) * P[i, j]

            elif prop == 'energy':

                for i in range(levels):
                    for j in range(levels):
                        value += P[i, j] ** 2

                value = np.sqrt(value)

            elif prop == 'homogeneity':

                for i in range(levels):
                    for j in range(levels):
                        value += P[i, j] / (1 + abs(i - j))

            elif prop == 'correlation':

                # Mean
                mu_i = 0
                mu_j = 0

                for i in range(levels):
                    for j in range(levels):
                        mu_i += i * P[i, j]
                        mu_j += j * P[i, j]

                # Standard deviation
                sigma_i = 0
                sigma_j = 0

                for i in range(levels):
                    for j in range(levels):
                        sigma_i += ((i - mu_i) ** 2) * P[i, j]
                        sigma_j += ((j - mu_j) ** 2) * P[i, j]

                sigma_i = np.sqrt(sigma_i)
                sigma_j = np.sqrt(sigma_j)

                # Correlation
                numerator = 0

                for i in range(levels):
                    for j in range(levels):
                        numerator += ((i - mu_i) *
                                      (j - mu_j) *
                                      P[i, j])

                if sigma_i * sigma_j != 0:
                    value = numerator / (sigma_i * sigma_j)
                else:
                    value = 0

            result[d, a] = value

    return result


def extract_glcm_features(image):

    # Quantize image to 16 gray levels
    image = (image / 16).astype(np.uint8)

    distances = [1, 2]
    angles = [0, np.pi/4, np.pi/2]

    glcm = compute_glcm(
        image,
        distances=distances,
        angles=angles,
        levels=16,
        symmetric=True,
        normed=True
    )

    features = []

    props = ['contrast', 'energy', 'homogeneity', 'correlation']

    for prop in props:
        values = compute_glcm_property(glcm, prop)
        features.extend(values.flatten())

    return features


# Example Usage
if __name__ == "__main__":

    # Example grayscale image
    image = np.array([
        [10, 20, 30, 40],
        [20, 30, 40, 50],
        [30, 40, 50, 60],
        [40, 50, 60, 70]
    ], dtype=np.uint8)

    features = extract_glcm_features(image)

    print("GLCM Features:")
    print(features)