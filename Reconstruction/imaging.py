import json
import numpy as np
import nodeLinks as nl 
import reconstructors
from matplotlib import pyplot as plt

def generateImage(weightsFile='defineWeights.json', RSSI=[], resolution=32):
    weights = json.load(open(weightsFile))
    weights = np.array(weights)
    print(weights.shape)

    w = np.array(weights[0])
    w = np.split(w, resolution)
    print(len(w))
    print(len(w[0]))
    plt.imshow(w)
    plt.show()
    '''
    image = reconstructors.reconstructSVD(weights, np.ones([130, 1]))
    image = np.split(image, resolution)
    plt.imshow(image)
    plt.show()
    '''
    return
    
generateImage()