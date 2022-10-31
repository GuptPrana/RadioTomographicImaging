import json
import numpy as np

# Define the Coordinate Plane
# Assume Rectangular Arrangment of Nodes
# Assume Wavelength = 12.5cm. Each square in grid can be delta = 0.5*12.5 = 6.25cm wide.
def generateGrid(delta=6.25,nodeFile='defineNodes.json',corners=0):
    nodes = json.load(open(nodeFile))
    
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

    height = int((maxY-minY)/delta)+((maxY-minY)%delta>0)
    width = int((maxX-minX)/delta)+((maxX-minX)%delta>0)
    grid = np.zeros((width, height))
    # axisX = np.linspace(minX, maxX, num=int(width/delta)+(width%delta>0), endpoint=True)
    # axisY = np.linspace(minY, maxY, num=int(height/delta)+(height%delta>0), endpoint=True)
    # gridX, gridY = np.meshgrid(axisX, axisY)
    if (corners==1):
        return grid, minX, maxX, minY, maxY
    return grid

# Use Bresenham's Line Algorithm to Generate Coordinates in Line of Sight
# Assume No Scattering
def generateWeights(thisGrid, x1, y1, x2, y2):
    # Edge Cases
    if (x2==x1):
        thisGrid[x1,:] = 1
        return thisGrid
    if (x2<x1 and y2<y1):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    # distance for weight
    w = 1/np.sqrt((x2-x1)**2+(y2-y1)**2)
    # print(w)
    # Line Drawing Conditions
    slope = (y2-y1)/(x2-x1)
    ax, ay = x1, y1
    bx, by = x2, y2
    if (slope<0):
        # Reverse
        ax, ay = x2, y2
        bx, by = x1, y1
    if (abs(slope)>1):
        # Flip X and Y
        ax, ay = ay, ax
        bx, by = by, bx
    # print(ax, ay, bx, by)
    # print(slope)
    # Coordinate space
    dx = bx-ax
    dy = abs(by-ay)
    p = 2*dy-dx
    y = ay
    # x = ax + step

# Should the weight be =1 or =1/sqrt(d)
    for step in range(dx+1):
        # decision parameter
        if (p>0):
            # y = Yk + 1
            p += 2*dy-2*dx
            if (slope<0):
                y -= 1
            else:
                y += 1
        else:
            # y = Yk
            p += 2*dy
        # Update 
        if (slope<0):
            if (abs(slope)>1):
                thisGrid[y, bx-step] = 1
            else:
                thisGrid[bx-step, y] = 1
        else:
            if (abs(slope)>1):
                thisGrid[y, ax+step] = 1
            else:
                thisGrid[ax+step, y] = 1
        # print(ax+step, y)
    return thisGrid

'''
# Save the Weight Matrices into JSON Dictionary
def generateAllWeights(numLinks=0, nodeFile='defineNodes.json'):
    # Grid Template
    grid, minX, maxX, minY, maxY = generateGrid(corners=1)
    nodes = json.load(open(nodeFile))
    
    for node in nodes:
        possibleLinks = []
        xRow, yRow = 0, 0
        if (node[0]==maxX):
            xRow = 1
        if (node[1]==maxY):
            yRow = 1
        
    if node[0]==thisNode[0]:
        pass
    elif node[1]==thisNode[1]:
        pass

    for link in range(numLinks):
        thisGrid = np.zeros_like(grid)
        thisGrid = generateWeights(np.zeros_like(grid), )
'''



 