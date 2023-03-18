import json
import numpy as np
import nodeLinks as nl 
import reconstructors
from convertSimData import extractRSSI
from matplotlib import pyplot as plt

def generateImage(weightsFile='defineWeightsEll.json', RSSI=[], resolution=32, lamb=0.01):
    weights = json.load(open(weightsFile))
    weights = np.array(weights)
    # print(weights.shape)
    
    # replace np.ones([130, 1]) with the RSSI values of same dimension
    rssi = np.array(RSSI) #np.ones(130)
    image = reconstructors.reconstructSVD(weights, rssi, lamb)
    image = np.split(image, resolution)
    plt.imshow(image)
    plt.show()
    return
    
    '''
    # The below is only for demo and can be removed
    # Change i in weights[i] to see different lines
    w = np.array(weights[-1])
    w = np.split(w, resolution)
    plt.imshow(w)
    plt.show()
    return
    '''

rssi = extractRSSI()
# print(*rssiValues, sep=', ')
generateImage(RSSI=rssi)