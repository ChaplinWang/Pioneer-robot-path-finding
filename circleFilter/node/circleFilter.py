#!/usr/bin/env python

import roslib
roslib.load_manifest('circleFilter')

import rospy
import time
import sys

from circleFinder.msg import *
from circleFilter.msg import *
from circleFilter.srv import *

from geometry_msgs.msg import *

from nav_msgs.msg import Odometry
import tf 
from tf.transformations import euler_from_quaternion


from threading import Semaphore

from plot_funcs import *

import matplotlib.pyplot as plt

from circleFilter.msg import *

from pylab import *
from numpy import dot, sum, tile, linalg
from numpy.linalg import inv
from numpy import dot
from numpy import matrix
from numpy import linalg
import math


sem = Semaphore()

filterData = (array([[0.1], [0.1], [0.1]]),diag((math.pow(10,100), math.pow(10,100), math.pow(10,100))))

#The true coordinates
truth = [((-1, -2), 0.13,1), \
         (( 3, 0), 0.23,2), \
         ((-1, 2), 0.05,3)]
         
#The distances.
truthDist = {}
for i in range(len(truth)):
    for u in range(len(truth)):
        if i != u:
            truthDist[(i,u)] = math.sqrt(math.pow(truth[i][0][0] - truth[u][0][0], 2) + math.pow(truth[i][0][1] - truth[u][0][1], 2))




#Motion Update  (prediction)
def kf_predict(X, P, Q, U):			#U is action U[0] -fwd U[1]-turn
    X[0] = X[0] + U[0]*cos(X[2])
    X[1] = X[1] + U[0]*sin(X[2])
    X[2] = X[2] + U[1]
    while X[2] > math.pi:
        X[2] = X[2]-2*math.pi
    while X[2] <= -math.pi:
        X[2] = X[2]+2*math.pi

    F = matrix([[1,0,-U[0]*sin(U[1])], [0,1,U[0]*cos(U[1])],[0,0,1]]) 

    P  = dot(F,dot(P,(F.T))) + Q
    return(X,P)


#Observation Update  
def kf_update(X, P, Z, XB, YB, R):

	dx = XB-X[0]
	dy = YB-X[1]
	distsqr = pow(dx,2) + pow(dy,2)
	dist = sqrt(distsqr)
	h21 = -dx/dist
	h22 = -dy/dist
	h23 = 0
	h31 = -dy/distsqr  
	h32 = dx/distsqr 
	h33 = -1
	H = matrix([[0,0,0],[h21,h22,h23],[h31,h32,h33]])

	while(X[2] > math.pi):
		X[2] = X[2]-2*math.pi
	while(X[2] <= -math.pi):
		X[2] = X[2]+2*math.pi
	h = matrix([[0], [dist], [math.atan2(dy, dx) - X[2]]]) #bug! care degree -Pi - Pi

	y = Z-h

	while(y[2] > math.pi):
		y[2] = y[2]-2*math.pi
	while(y[2] <= -math.pi):
		y[2] = y[2]+2*math.pi

	S = dot(H, dot(P,(H.T))) + R              #S = H*P*(H.T) + R
	K = dot(dot(P, (H.T)),(S.I)) 			 #kalman gain  K = P * (H.T)*(inverse(TEMP))

	X = X + dot(K,y)

	while(X[2] > math.pi):
		X[2] = X[2]-2*math.pi
	while(X[2] <= -math.pi):
		X[2] = X[2]+2*math.pi

	#print(H)
	I= diag((1, 1, 1))
	P = dot((I - dot(K,H)),P)
 	return (X,P)

state = 1
update_active = False

def stateChange_callback(data):
    # 0 is do nothing
    # 1 observation listen
    # 2 motion
    # 3 reset
    global state
    global update_active 
    state = data.state
    while update_active:
        pass
    if state == 3:
        global filterData
        filterData = (array([[0], [0], [0]]),diag((math.pow(10,100), math.pow(10,100), math.pow(10,100))))
        state = 0
    return True

relData = (0,0,0)
lastPos = (0,0,0,0)
def motion_callback(data, args):
   
    global state
    global lastPos
    if state != 2:
        return;

    global update_active
    update_active = True
    global filterData 
    pub = args[0]
    print "Motion update"
    global relData
    print data
    dx = data.pose.pose.position.x - relData[0]
    dy = data.pose.pose.position.y - relData[1]
    a = data.pose.pose.orientation

    q0 = a.w
    q1 = a.x
    q2 = a.y
    q3 = a.z
    #print math.atan2(2*(q0 * q1 + q2*q3 ),1- 2 * (q1*q1 + q2*q2))
   
    #print  math.asin(2*(q0 * q2- a.z*a.y))

    #print   math.atan2(2*(a.x * a.z + a.y*a.w),1- 2 * (a.w*a.w + a.z*a.z))

    da = math.atan2(2 * a.z * a.w, 1- 2 * a.z*a.z ) - math.atan2(2 * lastPos[3] * lastPos[2], 1- 2 * lastPos[3]*lastPos[3] ) 

    lastPos = (a.x,a.y,a.w,a.z)


    dist = sqrt(math.pow(dx,2) + math.pow(dy,2))
    relData = (data.pose.pose.position.x, data.pose.pose.position.y)

    U = array(([dist],[da]))
    
    X = filterData[0]
    P = filterData[1]


    Q = diag((0.1,0.1,0.1))
    filterData = kf_predict(X, P, Q, U)
    
    coords = coordinate()
    coords.x = filterData[0][0]
    coords.y = filterData[0][1]
    coords.theta = filterData[0][2]
    coords.beaconcount
    pub.publish(coords)
    
    update_active = False
    
obs_count = 0
def observation_callback(data, args):  
    global state
    if state != 1:
        return;
        
    global update_active
    update_active = True
    
    print "Observation update"

    pub = args[0]
    max_deviation = args[1]
    global filterData 
    
    array = data.array
    matches = {}
    #go through each found circle and find the best radial match
    for i in array:
        best = float("inf")
        match = None
        for u in truth:
            #get the truth that has the closest tadius
            c = abs(i.radius - (0.0 + u[1]))
            if c < best:
                best = c
                match = u
        if match == -1:
            print "ERROR: no truth matched."
            sys.exit(0)
        if match in matches:
            possibles = matches[match]
            possibles.append(i)
            matches[match] = possibles
        else:
            matches[match] = [i]
    
    # Get the best match for any circles that have two or more candidates.
    # Calculate the distance error from each truth and the candidate and
    # choose the smallest error.
   
    count = 0
    for i in truth:
        if i in matches:
            for u in matches[i]:
                ratio =  u.radius/ i[1]
                if 1 + max_deviation >= ratio and 1 - max_deviation <= ratio:
                    print "ID:", i[2]
                    #beacon x
                    XB = i[0][0]
                    #beacon y
                    YB = i[0][1]
                    #observation matrix
                    theta = u.theta
                    
                    while theta > math.pi:
                        theta = theta-2*math.pi
                    while theta <= -math.pi:
                        theta = theta+2*math.pi
                    Z = matrix([[0], [u.distance], [theta]])
                    #R = eye(shape(Z)[0])
                    disvar = 0.004 + 0.00001 * sqrt((pow(i[0][0]-u.x,2) + pow(i[0][1]-u.y,2)))
                    R = diag((1, disvar,0.001))
                    R = diag((1,0.005,0.005))
                    X = filterData[0]
                    P = filterData[1]
                    filterData = kf_update(X, P, Z, XB, YB, R)
                    count = count + 1
                else:
                    print "DROPPED"
                    print u
                    print

    
                
    coords = coordinate()
    coords.x = filterData[0][0]
    coords.y = filterData[0][1]
    coords.theta = filterData[0][2]
    coords.beaconcount = count
    pub.publish(coords)
    global obs_count
    obs_count = obs_count + count
    print obs_count
    print filterData[1 ]
    print
    update_active = False
     

if __name__ == '__main__':
    
    print "Circle Filter started."
    
    pub = rospy.Publisher("coordinate", coordinate)
    
    max_deviation = 0.2
    
    args = [pub,max_deviation]
    
    rospy.init_node('circleFilter')
    rospy.Subscriber("circles",circleArray, observation_callback, callback_args=args)

    motion_args = [pub, 2.0]
    
    rospy.Subscriber("pose",Odometry, motion_callback,callback_args=motion_args)
    
    
    s = rospy.Service('filterStateChange', stateChange, stateChange_callback)

    rospy.spin()
