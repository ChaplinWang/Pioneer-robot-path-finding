from pylab import *
from math import *
import time
import mover

def driving(dist):
    pass
#send moving msg to the robot stop obs
#driving the dist
#robo will send info to kalman,no worries here
#	

def tunrning(angle):
    pass
#send moving msg to the robot stop obs
#tuning the angle
#robo will send info to kalman,no worries here	

def obs():
    #obs comes from kalman
	return currentPosition,

def dest():
    #dest come from path
    return dest


def excute(D):
    #step 1:
    destPoint = array([D[0],D[1]])
    currentPosition = array([[0],[0],[0]])

    # go obs and get current position
    #destPoint = dest();
    #currentPosition = obs();
    currentPosition = mover.getLocation()
    while not mover.getSet():
        time.sleep(0.05)
        currentPosition = mover.getLocation()
        
    currentPosition = (0,0,0)
    dx = destPoint[0] - currentPosition[0]
    dy = destpoint[1] - currentPosition[1]

    angle = math.atan2(dy,dx) - currentPosition[2]
    if angle > math.pi:                     #probabbly buggy have to test this code might have angle 
        angle = math.pi - angle
    turning(angle)

    dist = sqrt(pow((destpoint[1]-currentPosition[1]),2) + pow(destpoint[0]-currentPosition[0]),2)
    dist = dist/3     
    goal = array([[currentPosition[0] + dist*cos(currentPosition[2])],[currentPosition[0] + dist*sin(currentPosition[2])],[0]])
    driving(dist);

    #step 2:
	currentPosition = mover.getLocation()
    while not mover.getSet():
        time.sleep(0.05)
        currentPosition = mover.getLocation()
        
    dx = destPoint[0] - currentPosition[0]
    dy = destpoint[1] - currentPosition[1]

    angle = math.atan2(dy,dx) - currentPosition[2]
    if angle > math.pi:                     #probabbly buggy have to test this code might have angle 
        angle = math.pi - angle
    turning(angle)

    dist = sqrt(pow((destpoint[1]-currentPosition[1]),2) + pow(destpoint[0]-currentPosition[0]),2)
    dist = dist/2
    goal = array([[currentPosition[0] + dist*cos(currentPosition[2])],[currentPosition[0] + dist*sin(currentPosition[2])],[0]])
    driving(dist);c

    #step 3:
    
	currentPosition = mover.getLocation()
    while not mover.getSet():
        time.sleep(0.05)
        currentPosition = mover.getLocation()
        
    dx = destPoint[0] - currentPosition[0]
    dy = destpoint[1] - currentPosition[1]

    angle = math.atan2(dy,dx) - currentPosition[2]
    if angle > math.pi:                     #probabbly buggy have to test this code might have angle 
        angle = math.pi - angle
    turning(angle)

    dist = sqrt(pow((destpoint[1]-currentPosition[1]),2) + pow(destpoint[0]-currentPosition[0]),2)
    dist = dist
    goal = array([[currentPosition[0] + dist*cos(currentPosition[2])],[currentPosition[0] + dist*sin(currentPosition[2])],[0]])
    driving(dist);

    #step 4: (optional)
	currentPosition = mover.getLocation()
    while not mover.getSet():
        time.sleep(0.05)
        currentPosition = mover.getLocation()
        
    tollerance = destPoint - currentposition
    if tollerance > 0.5 or tollerance < -0.5:
        dx = destPoint[0] - currentPosition[0]
        dy = destpoint[1] - currentPosition[1]


        angle = math.atan2(dy,dx) - currentPosition[2]
        if angle > math.pi:                     #probabbly buggy have to test this code might have angle 
            angle = math.pi - angle
        turning(angle)

        dist = sqrt(pow((destpoint[1]-currentPosition[1]),2) + pow(destpoint[0]-currentPosition[0]),2)
        dist = dist
        goal = array([[currentPosition[0] + dist*cos(currentPosition[2])],[currentPosition[0] + dist*sin(currentPosition[2])],[0]])
        driving(dist);
        #currentPosition = obs(); 

    



