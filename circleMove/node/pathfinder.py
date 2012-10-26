#! /usr/bin/env python
#Reads data from a file containing:
# Line 1: Robot starting position (x y theta)
# Lines 2-6: Goal coordinates (x y)
import string
import math
from pylab import *
from numpy import *

class point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dCal(fromPoint, toPoint):
    #Calculate distance between points
    d = math.pow(float(fromPoint.x) - float(toPoint.x), 2)
    d += math.pow(float(fromPoint.y) - float(toPoint.y), 2)
    d = math.sqrt(d)
    return d

def thetaCal(fromPoint, toPoint, d):
    # Calculate the angle between the lines
    theta = math.asin((float(toPoint.y) - float(fromPoint.y))/d)
    theta = (theta / math.pi) * 180
    return theta

def cost(fromPoint, toPoint, curTheta):
    #Variable multipliers for distance and angle (can be altered for weighting)
    dMul = 1
    aMul = 1

    #Get distance
    d = dCal(fromPoint, toPoint)
    #Calculate required angle shift in degrees
    # First get the angle to the goal point
    theta = thetaCal(fromPoint, toPoint, d)
    # Then subtract the robot's current theta
    theta = math.fabs(theta - float(curTheta))
    # Finally, keep theta between -180 and 180
    while theta <= -180:
        theta += 360
    while theta > 180:
        theta -= 360

    return dMul*d+aMul*math.fabs(theta)

def finder(X, points):
    goals = []
    path = []

    #Read robot start position from file "points"
    f = open(points)
    #line = string.split(f.readline(), " ")
                #start = point(line[0], line[1])
                #curTheta = float(line[2]) / math.pi * 180
    #X = array((1,2,1))
    start = point(X[0],X[1])
    curTheta = float(X[2]) / math.pi * 180

    #Read goal coordinates from open file
    for lines in f:
        line = string.split(lines, " ")
        goals.append(point(line[0], string.split(line[1], "\n")[0]))

    #Record robort start and remove from list
    path.append(start)

    j=0
    #While goals !empty:
    while goals:
        j += 1
        best = 99999
        # calculate the cost to each goal
        for goal in goals:
            current = cost(path[len(path)-1], goal, curTheta)
            # remember the smallest cost
            if current < best:
                best = current
                nextGoal = goal
        # update curTheta for robot pointing to smalest cost goal
        curTheta = thetaCal(path[len(path)-1], nextGoal, dCal(path[len(path)-1], nextGoal))
        # add smallest cost goal to path
        path.append(nextGoal)
        goals.remove(nextGoal)
    ret = []
    for i in path:
        ret.append((float(i.x)/100.0,float(i.y)/100.0))
    return ret
    
    
    
