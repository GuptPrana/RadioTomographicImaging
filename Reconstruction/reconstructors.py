'''
Implement reconstruction algorithms

y = Wx + n. Use least squares to minimize n --> x = argmin(x)(W_inv*y)
y: RSSI, W: transfer matrix, x: reconstructed image, n: noise
'''

import numpy as np
import scipy.sparse.linalg as linalg
'''
def reconstructSVD(weights, rssi):
    # SVD of Weights
    # weights = np.ones([130, 1089])
    # print(weights)
    U, S, Vt = np.linalg.svd(weights, full_matrices=False)
    # print(U.shape, S.shape, Vt.shape)
    # Inverse Problem: y = W*x --> x = W_inv*y
    S_inv = np.diag(np.reciprocal(S))
    W_inv = np.dot(np.dot(Vt.T, S_inv), U.T)
    # print(W_inv.shape)
    print(W_inv)
    return np.dot(W_inv, rssi)
'''   

def reconstructSVD(weights, rssi):
    # SVD of Weights
    weights = np.ones([130, 1089])
    # print(weights.shape)
    # weights = np.random.rand(130, 1089)
    # print(weights.shape)
    U, S, Vt = linalg.svds(weights, 10)
    # U, S, Vt = np.linalg.svd(weights, full_matrices=False)
    # print(U.shape, S.shape, Vt.shape)
    # Inverse Problem: y = W*x --> x = W_inv*y
    S_inv = np.diag(np.reciprocal(S))
    W_inv = np.dot(np.dot(Vt.T, S_inv), U.T)
    # print(W_inv.shape)
    return np.dot(W_inv, rssi)