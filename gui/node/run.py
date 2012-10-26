#!/usr/bin/env python

import roslib
roslib.load_manifest('gui')

import rospy
import time
import sys

from circleFilter.msg import *


from Tkinter import *

x = 300
y = 650


def gui_callback(data):
    global x
    global y
    x = data.x
    y = data.y
    print "Update: "
    print "x:", x
    print "y:", y
    print
    # when left side of ball hits wall reset


    


def drawcircle(canv,x,y,rad):
    canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='blue')

def movecircle(canv, cir):
    canv.move(cir,-1,-1)

def callback(event):
    movecircle(canvas, circ1)


if __name__ == '__main__':
    global x
    global y
    print x
    print y
    rospy.init_node('gui')
  
    rospy.Subscriber("coordinate",coordinate, gui_callback)
    
    

    print "Circle Filter started."

    try:
            # Python2
        import Tkinter as tk
    except ImportError:
            # Python3
        import tkinter as tk
    
    master = Tk()

    canvas = Canvas(master, width=2000, height=1000,bg='white',offset='50,50')
    canvas.pack()





    #i'd like to recalculate these coordinates every frame
    circ1=drawcircle(canvas,450,400,10)          
    circ2=drawcircle(canvas,850,400,12)
    circ3=drawcircle(canvas,650,0,15)

    canvas.create_line(650,0 , 650, 1000)
    canvas.create_line(0,300 , 10000, 300)

 




    root = tk.Tk()
    root.title("Tkinter Moving Ball")

    w = 420
    h = 300


    # create 50x50 square box for the circle boundries
    box = (0, 120, 50, 170)
    # create the ball object
    # give it a tag name for reference
    canvas.create_oval(box, fill="green", tag='robo')

    #canvas.create_rectangle(100, 25, 150, 75, fill="yellow", tag='robo')
    
    while True:
        # move the ball by given increments
        rad = 10
        x= x+1 #change this to update
        y = y+1 #change this to update
        canvas.create_oval(x-rad,y-rad,x+rad,y+rad, fill="red", tag='robo')
        # 15 millisecond delay
        # higher value --> slower animation
        canvas.after(15)
        canvas.update()
        time.sleep(.25)

  
    mainloop()





