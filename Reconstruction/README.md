# Reconstruction Algorithm

* Singular Value Decomposition of Weight Matrices for Inverse Problem (i.e. x = y * W_inv) where y: RSSI values, x: reconstructed image pixel intensities

## File Description

* nodeLinks.py generates the weight matrix for every link in the wireless network. Weights saved to defineWeights.json to avoid redundant computation. 
* reconstructor.py has the reconstruction algorithms.
* imaging.py produces the images from the RSSI values and Weights.
* defineNodes.json contains defined absolute positions of WiFi modules in CENTIMETERS. Current configuration: 20 Nodes 40cm apart in Square arrangement.

## Notes
* To change weights from 1 to 1/d | d = distance between two nodes, simply set grid[i,y] =w instead of =1 in generateWeights
* 130 Links are generated instead of 190 (paper suggests k(k-1)/2 links | k: number of nodes
