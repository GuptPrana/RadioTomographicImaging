'''
Implement reconstruction algorithms

y = Wx + n. Use least squares to minimize n --> x = argmin(x)(W_inv*y)
y: RSSI, W: transfer matrix, x: reconstructed image, n: noise
'''

import numpy as np
# import scipy.sparse.linalg as linalg

def reconstructSVD(weights, rssi, lamb=0.1):
    # SVD of Weights
    # weights = np.ones([130, 1089])
    # print(weights)
    U, S, Vt = np.linalg.svd(weights, full_matrices=False)
    # print(U.shape, S.shape, Vt.shape)
    # Inverse Problem: y = W*x --> x = W_inv*y
    # S_inv = np.diag(np.reciprocal(S)) 
    S_inv = np.reciprocal(S)+lamb*np.ones(S.shape)
    # Ridge
    S_inv = np.diag(S_inv)
    W_inv = np.dot(np.dot(Vt.T, S_inv), U.T)
    # print(W_inv.shape)
    return np.dot(W_inv, rssi)


def reconstruct_updated(weights, rssi, res=32, lamb=0.1):
    output = np.linalg.solve((np.matmul(weights.T, weights) + lamb*np.eye(res ** 2)),  (np.matmul(weights.T, rssi)))
    return output