#!/usr/bin/env python
#-------------------------------------------------------------------------------
#
# Circle finder.
#
# Rowan Leeder
#
#-------------------------------------------------------------------------------
#
# Listens on the 'scan' and 'base_scan' topics. These are the pioneers SICK
# topic and Stage's scan topic respectively.
#
# The program strips out noise samples and attempts to match circles to the
# remaining samples.
#
# Any circle that is found is then published on the 'circles' topic in a
# circleArray message.
#
# The circleArray and circleEntry messages are defined in the msg\ folder.
#
#-------------------------------------------------------------------------------
#
# Compile Commands:
#
# First run 'rosmake' in the base directory. If you change the messages in any
# way then you will have to close all ros components using the topic (basically
# everything) and then recompile with rosmake. If you add a message, add an 
# entry to the manifest file. 
#
# To run this program do 'rosrun circleFinder finder.py'. 
#
# Exit with Ctrl + C.
#
# Listen in with 'rostopic echo circles'
#
# If you want to see a plot of the data, set the 'plot' variable to True.
#
#-------------------------------------------------------------------------------
# Known Bugs:
# If the laser scan covers 360 degrees then you might get two circles at the 
# same spot. This is becuase i haven't joined the two ends of the scan together.
# This will not be an issue with the robots as they only take 180 degree scans.

# Ros imports.
import roslib; 
roslib.load_manifest('circleFinder')
import rospy
from sensor_msgs.msg import LaserScan
from roslib.rostime import Duration 

# Python lib imports.
import math
import time

# Message imports
from circleFinder.msg import *

# Local file imports.
from placment_funcs import *
from data_parser import *

# plot functions are in here. Remove if you dont want and you might free up 
# some memory.
from plot_funcs import *


#-------------------------------------------------------------------------------
# Function: callback
#
# Thread created when a laser scan is received on a listening topic and extract 
# and publish a specified number of circle from the data.
#
#-------------------------------------------------------------------------------
#
# args          - An array of arguments. The form is: 
#    max_dist      - the maximum distance to look for circles. If a sample or 
#                    circle edge goes beyond this then it will be ignored.
#    max_rad       - The maximum radius that a valid circle can have.
#    min_rad       - The minimum radius that a valid circle can have.
#    grad_tol      - The tolerance used in the prune function.
#    split_multi   - The multiplier used in the split function
#
# publish       - A circleArray object containing the circle data in an array of 
#                 circleEntry objects. These classes are defined in the 
#                 circleFinder/msg path.
#-------------------------------------------------------------------------------
def callback(data, args):
    tStart = time.time()
    
    pub         = args[0]
    max_dist    = args[1]
    max_rad     = args[2]
    min_rad     = args[3]
    grad_tol    = args[4]
    split_multi = args[5]
    prune_lines = args[6]
    plot        = args[7]
    
    
    # Get possible circle data.
    possibles = dataParser(data,max_dist, grad_tol, split_multi, prune_lines)
    
    # Calculate the circle info from that data.
    circles = []
    for i in possibles:
        current = matchCirc(list(i), False)
        if current is not  None:
            #prune out any circles that are too large or small
            if  current[1] > max_rad or \
                current[1] < min_rad or \
                math.sqrt(math.pow(current[0][0],2) + math.pow(current[0][1],2)) + current[1] > max_dist:
                pass
            else:
                circles.append(current)
    
    # Setup circleArray and publish found circles.
    ret = []
    for i in circles:
        c = circleEntry()
        c.x = i[0][0]
        c.y = i[0][1]
        c.distance = math.sqrt(i[0][0]*i[0][0] + i[0][1] * i[0][1])
        c.theta = math.atan2(i[0][1], i[0][0])
        c.radius = i[1]
        ret.append(c)
    m = circleArray()
    m.broadcastTime = rospy.get_rostime()
    m.duration = time.time() - tStart
    m.array = ret
    if not rospy.is_shutdown():
        pub.publish(m)
        
    if plot:
        import matplotlib.pyplot as plt
        plotWorld(data, 30, True, 'ro')
        for i in circles:
            plotCircle((i[0])[0],(i[0])[1],i[1])
        for i in possibles:
            for u in i:
                plt.plot(u[0], u[1], 'bo')
        plt.plot(0,0,'ro')
        plotAxis(8,-8,8,-8,4)
        plt.axis([-8,8,-8,8])
        plt.show()



#-------------------------------------------------------------------------------
# Function: main
#
# Sets up the callback function and then idles.
#
# Program arguments are inside. 
#
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    #print dir()
    
    # the publiser
    pub = rospy.Publisher("circles", circleArray)
    
    # The maximum distance from the origin that a sample point or circle edge 
    # can be before they are considered invalid.
    max_dist    = 7
    
    # The maximum radius a circle can be before it is considered invalid.
    max_rad     = 0.25
    
    # The maximum radius a circle can be before it is considered invalid.
    min_rad     = 0
    
    # See the prune function in data_parser.py
    grad_tol    = 0.3
    
    # See the split function in data_parser.py
    split_multi = 2.5
    
    # If true then an attempt to remove straight edges from the data will be 
    # made.
    prune_lines = True
    
    # Plot flag.
    plot = False
    
    import sys
    if (len(sys.argv) > 1):
        for i in sys.argv:
            if i == '--plot':
                plot = True
            elif i == '--no-line-pruning':
                prune_lines = False
    
    args = [pub, max_dist, max_rad, min_rad, grad_tol, split_multi, prune_lines , plot]
    print "--------------------------------------------------------------------------------"
    print "Circle Finder"
    print
    print "--------------------------------------------------------------------------------"
    print "Command line arguments are:"
    print "     --plot             Will cause the outcome of the first scan to be plotted."
    print "     --no-line-pruning  Will prevent straight lines from being removed from the" 
    print "                        scan."
    print
    print "--------------------------------------------------------------------------------"
    print "Starting circle finder with arguments:"
    print
    print "    Publisher:          " , pub
    print "    Maximum Distance:   " , max_dist
    print "    Maximum Radius:     " , max_rad
    print "    Minimum Radius:     " , min_rad
    print "    Gradient Tolerance: " , grad_tol
    print "    Split Multiplier:   " , split_multi
    print "    Remove Lines:       " , prune_lines 
    print "    Plot:               " , plot
    print
    print "--------------------------------------------------------------------------------"
    print "To increase speed, the listening thread is not verbose."
    print "Ctrl+C to exit."
    rospy.init_node('circles', anonymous=True)
    rospy.Subscriber("base_scan",LaserScan, callback, callback_args=args)
    rospy.Subscriber("scan",LaserScan, callback, callback_args=args)
    rospy.spin()
