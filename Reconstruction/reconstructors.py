'''
Implement reconstruction algorithms

SVD
y = Wx + n. Use least squares to minimize n --> x = argmin(x)(W_inv*y)
y: RSSI, W: transfer matrix, x: reconstructed image, n: noise
'''

import numpy as np

def reconstructSVD(weights, rssi, buffer):
    # SVD of Weights
    U, S, Vt = np.linalg.svd(weights, full_matrices=False)
    # Inverse Problem: y = W*x --> x = W_inv*y
    S_inv = np.diag(np.reciprocal(S))
    W_inv = np.dot(np.dot(Vt.T, S_inv), U.T)
    return np.dot(W_inv, rssi)