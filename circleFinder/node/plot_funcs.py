#This contains functions for plotting. Might get around to formatting this.

import math

import matplotlib.pyplot as plt


# When passed details it returns an array containing the Cartesian points lying 
# evenly around the circumference.
#
# x           - The x coord of the centre circle.
# y           - The y coord of the centre circle.
# radius      - The radius of the circle.
# samples     - The number of points to take.
#
# Returns:
# (x,y)[]     - The array of points on the circumference in (x,y) form.
def getCircle(x, y, radius, samples):
    inc =  (2 * math.pi)/samples
    ret = []
    for i in range(samples):
        ret.append((radius * math.cos(i * inc) + x, radius * math.sin(i * inc) + y))
    return ret


# When passed details it plots a line circle with 100 lines.
#
# x           - The x coord of the centre circle.
# y           - The y coord of the centre circle.
# radius      - The radius of the circle.
def plotCircle(x,y,radius):
    samples = 50
    inc =  (2 * math.pi)/samples
    ret = []
    for i in range(samples):
        ret.append((radius * math.cos(i * inc) + x, radius * math.sin(i * inc) + y))
    for i in range(len(ret)-1) :
        plt.plot( ((ret[i])[0], (ret[i+1])[0]),((ret[i])[1], (ret[i+1])[1]))
    plt.plot( ((ret[0])[0], (ret[samples-1])[0]),((ret[0])[1], (ret[samples-1])[1]))

# Plots a grid.
#
# px          - The maximum x.
# nx          - The minimum x.
# py          - The maximum y.
# ny          - The minimum y.
# res         - The spacing between each line.
def plotAxis(px,nx,py,ny, res):

    for x in range(0,px +1, res):
        plt.plot((x, x), (ny, py))
    for x in range(0,nx -1, -res):
        plt.plot((x, x), (ny, py))
    
    for y in range(0,py+1, res):
        plt.plot((nx, px), (y, y))
    for y in range(0,ny-1, -res):
        plt.plot((nx, px), (y, y))
    

def plotWorld(data, maxDist, printCentre, pstr):
    #Array holding all the data points
    points = []    
    #convert scanner infomation into Cartesian points. Ignore points out of scanner range.
    for i in range(len(data.ranges)):
        if data.ranges[i] <= maxDist:
            points.append((data.ranges[i] * math.cos(data.angle_min + i*data.angle_increment), data.ranges[i] * math.sin(data.angle_min + i*data.angle_increment)))
    #plot all the points
    for i in points:
        plt.plot(i[0], i[1], pstr)
    if printCentre:
        plt.plot(0,0,'ro')
        
        
def plotLineBetween(p1, p2, multi):
    xx = (p1[0] + p2[0])/2
    yy = (p1[1] + p2[1])/2
    plt.plot((0, multi * xx), (0, multi * yy))
    
