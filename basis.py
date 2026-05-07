import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# BASIS IMAGE SIZE
# ============================================================

N = 8

# Choose frequencies
u = 2
v = 3

basis = np.zeros((N, N))

# ============================================================
# GENERATE DCT BASIS IMAGE
# ============================================================

for x in range(N):
    for y in range(N):

        if u == 0:
            cu = np.sqrt(1/N)
        else:
            cu = np.sqrt(2/N)

        if v == 0:
            cv = np.sqrt(1/N)
        else:
            cv = np.sqrt(2/N)

        basis[x, y] = (
            cu * cv *
            np.cos(((2*x + 1) * u * np.pi) / (2*N)) *
            np.cos(((2*y + 1) * v * np.pi) / (2*N))
        )

# ============================================================
# DISPLAY BASIS IMAGE
# ============================================================

plt.imshow(basis, cmap='gray')
plt.title(f"DCT Basis Image ({u},{v})")
plt.colorbar()
plt.show()