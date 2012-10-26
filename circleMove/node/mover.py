#!/usr/bin/env python

import roslib
roslib.load_manifest('circleMove')

from circleFilter.msg import *
import circleFilter
from circleFilter.srv import *

from pylab import *
from math import *
import time

import pathfinder

import math
import time



from geometry_msgs.msg import Twist
import sys, select, termios, tty, rospy

location_set = False
location = None


def driving(dist, twist_pub, changeState, vel):
    dist = dist * 1.1
    duration = abs(dist/ vel) 
    print "dist", dist
    print "Duration",duration
    
    print "out current location:"
    print location
    print
    
    twist = Twist()

    twist.linear.x = vel; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;

    changeState(2)

    send = moveNotify()
    send.linear = dist
    send.rotation = 0


    start = time.time()
    while time.time() - start < duration:
        twist_pub.publish(twist)
        twist_pub.publish(twist)
        time.sleep(0.1)
    
    twist = Twist()
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    twist_pub.publish(twist)
    time.sleep(0.05)
    print "out new location:"
    print location
    print
    
    changeState(1)  
    time.sleep(1.5)


def turning(angle,twist_pub, changeState, vel):
    angle * 1.1
    duration = abs(angle/ vel) 


    print "angle", angle
    print "Duration",duration
    
    print "out current location:"
    print location
    print
    
    twist = Twist()

    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = vel;
    if(angle < 0):
        twist.angular.z = -abs(vel);

    changeState(2)

    send = moveNotify()
    send.linear = 0
    send.rotation = angle

    start = time.time()
    while time.time() - start < duration:
        twist_pub.publish(twist)
        twist_pub.publish(twist)
        time.sleep(0.1)
    
    twist = Twist()
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    twist_pub.publish(twist)
    time.sleep(0.2)
    print "out new location:"
    print location
    print
    changeState(1) 
    time.sleep(1.5) 
       


def excute(D, twist_pub, changeState, vel):
    global location
    global location_set

    #---------------------------------------------------------------------------
    #get destination
    destPoint = (D[0],D[1])
    
    #get current
    current = location
    count = 0
    while not location_set and count < 20:   #????probabbly danger
        time.sleep(0.05)
        current = location
        count = count + 1
    
    currentPosition = (current.x,current.y,current.theta)
        
    dx = destPoint[0] - currentPosition[0]
    dy = destPoint[1] - currentPosition[1]

    #rotate towards it.
    angle = math.atan2(dy,dx) - currentPosition[2]
    while(angle > math.pi):
        angle = angle-2*math.pi
    while(angle <= -math.pi):
        angle = angle+2*math.pi

    #probabbly buggy have to test this code might have angle 
    turning(angle, twist_pub, changeState, vel);
    #drive to it.
    dist = sqrt(pow((destPoint[1]-currentPosition[1]),2) + pow(destPoint[0]-currentPosition[0],2))  
    driving(dist/3, twist_pub, changeState, vel)
    
    #---------------------------------------------------------------------------
    #get destination
    destPoint = (D[0],D[1])
    
    #get current
    current = location
    count = 0
    while not location_set and count < 20:   #????probabbly danger
        time.sleep(0.05)
        current = location
        count = count + 1
    
    currentPosition = (current.x,current.y,current.theta)
        
    dx = destPoint[0] - currentPosition[0]
    dy = destPoint[1] - currentPosition[1]

    #rotate towards it.
    angle = math.atan2(dy,dx) - currentPosition[2]
    while(angle > math.pi):
        angle = angle-2*math.pi
    while(angle <= -math.pi):
        angle = angle+2*math.pi

                     #probabbly buggy have to test this code might have angle 
    turning(angle, twist_pub, changeState, vel);
    #drive to it.
    dist = sqrt(pow((destPoint[1]-currentPosition[1]),2) + pow(destPoint[0]-currentPosition[0],2))  
    driving(dist/2, twist_pub, changeState, vel)
    print "Done move to : " , destPoint
    print "from: ", currentPosition

    #---------------------------------------------------------------------------
    destPoint = (D[0],D[1])
    
    #get current
    current = location
    count = 0
    while not location_set and count < 20:   #????probabbly danger
        time.sleep(0.05)
        current = location
        count = count + 1
    
    currentPosition = (current.x,current.y,current.theta)
        
    dx = destPoint[0] - currentPosition[0]
    dy = destPoint[1] - currentPosition[1]

    #rotate towards it.
    angle = math.atan2(dy,dx) - currentPosition[2]
    while(angle > math.pi):
        angle = angle-2*math.pi
    while(angle <= -math.pi):
        angle = angle+2*math.pi

                     #probabbly buggy have to test this code might have angle 
    turning(angle, twist_pub, changeState, vel);
    #drive to it.
    dist = sqrt(pow((destPoint[1]-currentPosition[1]),2) + pow(destPoint[0]-currentPosition[0],2))  
    driving(dist, twist_pub, changeState, vel)





def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def location_updater(data, args):
    global location_set
    global location
    location_set = True
    location = data
    
  
    
def localize(twist_pub, changeState, vel):
    resp = changeState(3)
    for i in range(3):
        resp = changeState(1)
        time.sleep(0.4)
        resp = changeState(2)
        turning((2 * math.pi) /3,twist_pub, changeState, vel)
        time.sleep(0.15)
    resp = changeState(1)

if __name__ == '__main__':
    start = time.time()
    total = 0
    vel = 0.5
    
    settings = termios.tcgetattr(sys.stdin)
    if (len(sys.argv) != 2):
        print "Requires the goal file"
        sys.exit(0)
    filePath = sys.argv[1]
    print filePath
        
    #subscriber to listen and update the location.
    args = []
    rospy.Subscriber("coordinate",coordinate, location_updater, callback_args=args)
    twist_pub = rospy.Publisher('cmd_vel', Twist)

    rospy.init_node('circleMover')
    
    twist_pub.publish( Twist())
    #set up service
    rospy.wait_for_service('filterStateChange')
    changeState = rospy.ServiceProxy('filterStateChange', stateChange)
    #start obser

    localize(twist_pub, changeState, vel)

    #calc plan
    resp = changeState(1)
    time.sleep(0.5)
    plan =  pathfinder.finder([location.x,location.y,location.theta], filePath)
    print plan

    #loop through plan and move.
    print location
    del plan[0]
    print "the plan:"
    print plan
    print 
    for i in plan:
        print "Moving to point: ", i
        resp = changeState(1)
        time.sleep(1)
        excute(i,twist_pub,changeState, vel)
        resp = changeState(0)
        print "Done moving to a point. preventing updates."
        print "the current location is:"
        print location
        print
        print "Press any key to go to next point or end:"
        total = total + time.time() - start
        start = time.time()
        print "Current time is: " , total
        key = getKey()
        #localize(twist_pub, changeState, vel)

    print
    print "All points 'apparently' visited"
    print "Time took:", total
