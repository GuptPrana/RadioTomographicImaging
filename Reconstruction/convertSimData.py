# Convert Simulation RSSI Data to test Image Reconstruction 
'''
Simulation Details
- 20 Nodes in square formation
- Origin is bottom-left corner
- Count index in counter-clockwise direction
Our Reconstruction Details
- Check defineLinks.json
- Origin is top-left corner
- Order of values in RSSI Array: Top, Bottom, Left, Right(empty)
'''

import numpy as np

def extractRSSI(filename='./rssiSim.csv'):
    rssiValues = np.array([])
    data = np.genfromtxt(filename, delimiter=',')

    # top row
    rssiValues = np.concatenate((rssiValues, data[5:14,15]))
    # print(rssiValues.shape)
    i = 0
    for t in range(14, 10, -1):
        i += 1
        rssiValues = np.concatenate((rssiValues, data[0+i:14+i,t]))
    # print(rssiValues.shape)
    rssiValues = np.concatenate((rssiValues, data[5:14,10]))
    # bottom row
    rssiValues = np.concatenate((rssiValues, data[8:4:-1,0]))
    i = -1
    for b in range(1, 5):
        i += 1
        rssiValues = np.concatenate((rssiValues, data[14-i:18-i,b]))
    # print(rssiValues.shape)
    i = -1
    for b in range(1, 5):
        i += 1
        rssiValues = np.concatenate((rssiValues, data[7-i:3-i:-1,b]))
    rssiValues = np.concatenate((rssiValues, data[10:14,5]))
    # print(rssiValues.shape)
    # left column
    i = -1
    for l in range(16, 20):
        i += 1
        rssiValues = np.concatenate((rssiValues, data[12-i:8-i:-1,l]))

    print(*rssiValues, sep=', ')
    return rssiValues

# extractRSSI()
