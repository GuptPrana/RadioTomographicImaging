import json
import numpy as np
import nodeLinks as nl 
import reconstructors
from convertSimData import extractRSSI
from matplotlib import pyplot as plt

def generateImage(weightsFile='defineWeightsEll.json', RSSI=[], resolution=32, lamb=0.1):
    weights = json.load(open(weightsFile))
    weights = np.array(weights)
    # print(weights.shape)
    
    # replace np.ones([130, 1]) with the RSSI values of same dimension
    rssi = np.array(RSSI) #np.ones(130)
    image = reconstructors.reconstructSVD(weights, rssi, lamb)
    image_updated = reconstructors.reconstruct_updated(weights, rssi, resolution, lamb)
    image = np.split(image, resolution)
    image_updated = np.split(image_updated, resolution)
    plt.figure(1)
    plt.imshow(image)
    plt.figure(2)
    plt.imshow(image_updated)
    plt.show()
    return
    
rssi = extractRSSI()
generateImage(RSSI=rssi)