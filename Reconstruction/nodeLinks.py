import json
import numpy as np
import math 

# Define the Coordinate Plane
# Assume Wavelength = 12.5cm. Each square in grid can be delta = 0.5*12.5 = 6.25cm wide.
def generateGrid(delta=6.25,nodeFile='defineNodes.json',corners=0,ROI='e'):
    nodes = json.load(open(nodeFile))
    # Identify the corners in map
    minX, maxX = 0, 0
    minY, maxY = 0, 0
    for node in nodes['nodeList']:
        if (node[0]>maxX):
            maxX = node[0]
        elif (node[0]<minX):
            minX = node[0]
        if (node[1]>maxY):
            maxY = node[1]
        elif (node[1]<minY):
            minY = node[1]
    
    # ROI = 'b': Bresenham, 'e': ellipse
    if (ROI=='b'):
        grid = np.zeros((width, height))
        height = int((maxY-minY)/delta)+((maxY-minY)%delta>0)+1
        width = int((maxX-minX)/delta)+((maxX-minX)%delta>0)+1
        if (corners==1):
            minX = int(minX/delta)+(minX%delta>0)
            maxX = int(maxX/delta)+(maxX%delta>0)
            minY = int(minY/delta)+(minY%delta>0)
            maxY = int(maxY/delta)+(maxY%delta>0)
            return grid, minX, maxX, minY, maxY
        return grid
    else: 
        # 200/6.25 = 32 squares in the grid
        # height = int((maxY-minY)/delta)+((maxY-minY)%delta>0)
        # width = int((maxX-minX)/delta)+((maxX-minX)%delta>0)
        maxX = int((maxY-minY)/delta)+((maxY-minY)%delta>0)
        maxY = int((maxX-minX)/delta)+((maxX-minX)%delta>0)
        minX = 0
        minY = 0
        return maxX, maxY

# Use Bresenham's Line Algorithm to Generate Coordinates in Line of Sight
# Assume No Scattering
def generateWeightsBres(thisGrid, pointA, pointB):
    x1, y1 = pointA
    x2, y2 = pointB
    # Edge Cases
    if (x2==x1):
        thisGrid[x1,:] = 1
        return thisGrid
    if (x2<x1 and y2<y1):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    # distance for weight
    # w = 1/np.sqrt((x2-x1)**2+(y2-y1)**2)
    w = 1
    # Line Drawing Conditions
    slope = (y2-y1)/(x2-x1)
    ax, ay = x1, y1
    bx, by = x2, y2
    if (slope<0):
        # Reverse
        ax, ay = x1, y2
        bx, by = x2, y1
    if (abs(slope)>1):
        # Flip X and Y
        ax, ay = ay, ax
        bx, by = by, bx
    # Coordinate space
    dx = bx-ax
    dy = by-ay
    p = 2*dy-dx
    y = 0
    # x = ax + step
    # *** Set weights as 1/sqrt(d) instead of just 1 ***
    for step in range(dx+1):
        # decision parameter
        if (p>0):
            # y = Yk + 1
            p += 2*dy-2*dx
            y += 1 if (step>0) else 0
        else:
            # y = Yk
            p += 2*dy
        # Update 
        if (slope<0):
            if (abs(slope)>1):
                thisGrid[by-y, ax+step] = w
            else:
                thisGrid[ax+step, by-y] = w
        else:
            if (abs(slope)>1):
                thisGrid[ay+y, ax+step] = w
            else:
                thisGrid[ax+step, ay+y] = w

    return thisGrid

# Save the Weight Matrices into JSON Dictionary
def generateAllWeights(nodeFile='defineNodes.json', linksFile='defineLinks.json', weightsFile='defineWeights.json', delta=6.25):
    # Grid Template
    # grid, minX, maxX, minY, maxY = generateGrid(corners=1, ROI='b')
    maxX, maxY = generateGrid()
    nodes = json.load(open(nodeFile))
    links = {}
    linkCount = 0 
    for thisNode in nodes['nodeList']:
        # Identify possible links
        possibleLinks = []
        for checkNode in nodes['nodeList']:
            # Avoid interference with original list
            node = [thisNode[0], thisNode[1]]
            otherNode = [checkNode[0], checkNode[1]]
            # Conversion to Grid
            node[0] = int(node[0]/delta)+(node[0]%delta>0)
            node[1] = int(node[1]/delta)+(node[1]%delta>0)
            otherNode[0] = int(otherNode[0]/delta)+(otherNode[0]%delta>0)
            otherNode[1] = int(otherNode[1]/delta)+(otherNode[1]%delta>0)
            
            # Edge Cases
            if (node[0]==otherNode[0]):
                if (node[0]==maxY or node[0]==0):
                    # Same Edge
                    continue
                elif (node[1]==otherNode[1]): 
                    # Same Node
                    continue
            elif (node[1]==otherNode[1]):
                if (node[1]==maxX or node[1]==0):
                    # Same Edge
                    continue
            elif (otherNode in possibleLinks):
                continue
            
            if (str(otherNode) not in links):
                possibleLinks.append(otherNode)
            elif (node not in links[str(otherNode)]):
                possibleLinks.append(otherNode)
            else: 
                continue

            # Generate Weights for this Link

            # Can use pointer/reference to avoid sending grid in every function call
            # weight = generateWeightsBres(np.zeros_like(grid), node, otherNode)
            weight = generateWeights(node, otherNode, maxX, maxY)
            # x*y array --> 1*xy array (concatenate all y|x for all x)
            weightVector = weight.flatten()
            # concatenate this weight array into the weightMatrix --> numLinks*xy array
            if (linkCount == 0):
                weightMatrix = weightVector
            else:
                weightMatrix = np.vstack((weightMatrix, weightVector))
            
            linkCount += 1

        # Save the possible links to Links Dictionary
        # Saving Links (incomplete) is not really useful though
        links[str(node)] = possibleLinks

    # Save Links to JSON File for reference
    with open(linksFile, 'w') as output:
        output.write(json.dumps(links, indent=4))
    # Save Weights to JSON File for reference
    with open(weightsFile, 'w') as output:
        output.write(json.dumps(weightMatrix.tolist(), indent=4))

    return 1

# Original method to determine pixels in the LOS between 2 nodes
# if d(a,c)+d(b,c) < d(a,b) + lambda | c:center of pixel, a,b: nodes
def generateWeights(pointA, pointB, maxX, maxY):
    x1, y1 = pointA
    x2, y2 = pointB
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    lamb = 0
    dist += lamb
    # Fixed lambda vs Changing Lambda according to size

    mesh = np.mgrid[0:maxX,0:maxY]
    distX = mesh[0]
    distY = mesh[1]
    distA = math.sqrt((distX - x1)**2 + (distY - y1)**2)
    distB = math.sqrt((distX - x2)**2 + (distY - y2)**2)
    
    grid = (distA+distB)>dist
    return grid

##############################################################
# To Test: 
# print(generateAllWeights())
