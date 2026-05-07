import numpy as np
import matplotlib.pyplot as plt

N = 8

plt.figure(figsize=(8,8))

for u in range(N):
    for v in range(N):

        basis = np.zeros((N,N))

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

                basis[x,y] = (
                    cu * cv *
                    np.cos(((2*x+1)*u*np.pi)/(2*N)) *
                    np.cos(((2*y+1)*v*np.pi)/(2*N))
                )

        plt.subplot(N,N,u*N+v+1)
        plt.imshow(basis, cmap='gray')
        plt.axis('off')

plt.tight_layout()
plt.show()