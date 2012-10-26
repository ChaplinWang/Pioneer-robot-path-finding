import math

#-------------------------------------------------------------------------------
# Function: matchCirc
#
# Matches a circle to a set of data points.
#
#-------------------------------------------------------------------------------
#
# points      - The (x,y) points to match a circle to. These points are assumed to be on the edge of a circle.
# allow_conconcave
#             - If True then circles that are defined by concave arcs will be returned. If False then None will be returned when a concave arc is found.
#
#-------------------------------------------------------------------------------
#
# return      - ((centre x, centre y), radius) if a circle could be matched. 'None' if a circle could not be matched.
#
#-------------------------------------------------------------------------------
def matchCirc(points, allow_conconcave):
    if len(points) < 3:
        return None
        
    offset = len(points)/10
    
    if len(points) <= 3:
        offset = 1
    elif len(points) <= 10:
        offset = 2
    elif len(points) <= 20:
        offset = 5
    elif len(points) <= 100:
        offset = 10
        
    lines = []
    for u in range(len(points)-offset):
        
        y1 = (points[u])[1]
        y2 = (points[u+offset])[1]
        
        x1 = (points[u])[0]
        x2 = (points[u+offset])[0]
        
        xx = (x1 + x2)/2
        yy = (y1 + y2)/2
        
        #remove the -1/ to make this line the gradient of the two points.
        gradient = -1/((y2 - y1)/(x2 -x1))
        
        l = ((-100,(gradient*(-100 -xx) + yy)),(100,(gradient*(100 -xx) + yy)))
        lines.append(l)

    #get the intersection of all lines.
    inter = []
    xt = 0
    yt = 0
    for i in lines:
        for u in lines:
            #don't get intersection with self.
            if u != i:
                #get the coords of the four points
                #line 1
                x1 = (i[0])[0]
                y1 = (i[0])[1]
                x2 = (i[1])[0]
                y2 = (i[1])[1]
                
                #line 2
                x3 = (u[0])[0]
                y3 = (u[0])[1]
                x4 = (u[1])[0]
                y4 = (u[1])[1]
                
                #denominator
                d = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
                #x-coord
                xi = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/d
                #y-coord
                yi = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4))/d
                
                #plt.plot(xi,yi,'ro')
                inter.append((xi,yi))
                
    #get centre. 0.85 was worked out by a mediumish-sized emperial test for a good number
    centre = findCentre(inter, 0.85)
    
    #get radius
    radius = -1
    try:
        radius = findRadius(points, centre, 0.85)
    except Exception, err:
        return None

    #prune concave circles if requested.
    #This section MUST be after the radius find as it removes outlying points.
    if not allow_conconcave:
        d = math.sqrt(math.pow(centre[0] ,2) + math.pow(centre[1] ,2))
        min = d
        for i in points:
            compare = math.sqrt(i[0]*i[0] + i[1]*i[1])
            if compare < min:
                min = compare
        if min == d:
            return None
    return (centre,radius)
    
    
#-------------------------------------------------------------------------------
# Function: msd
#
# Calculates the mean and standard deviation of a set of data.
#
#-------------------------------------------------------------------------------
#
# data        - The data set.
#
# return      - (mean, standard deviation).
#-------------------------------------------------------------------------------
def msd(data):
    if len(data) == 1:
        return (data[0],0)
    elif len(data) == 0:
        return ()
    n = len(data)
    s = 0
    ss = 0
    for x in data:
        s = s + x
        ss = ss + x*x
    mean = s/n
    variance = (ss - s*mean)/(n - 1)
    return (mean, math.sqrt(abs(variance)))

#-------------------------------------------------------------------------------
# Function: findCentre
#
# Finds the mean distance of a set of points (x,y) to a centre point. 
#
#-------------------------------------------------------------------------------
#
# points      - The data set.
# endChange   - The ratio of variance change at which to stop.
#
# return      - The mean point (x,y).
#-------------------------------------------------------------------------------
def findCentre(points, endChange):
    #Calculate the distances of all points. This will be the most time intensive single step.
    r = []
    for i in points:
        r.append(math.sqrt(i[0] * i[0] + i[1] * i[1]))
    old = -1
    #loop through
    while True:
        #get the mean and the varience.
        ms = msd(r)
        #if the varience is 0 or if the ratio target is reached, end.
        if(ms[1] == 0 or ms[1]/ old >= endChange):
            break
        #save the current varience.
        old = ms[1]
        #calculate valid range.
        compareP = ms[0] + (1 * ms[1])
        compareN = ms[0] - (1 * ms[1])
        
        #remove any item that is out of range
        for i in range(len(points)-1, -1,-1):
            if r[i] < compareN or r[i] > compareP:
                del r[i]
                #plt.plot((intersections[i])[0],(intersections[i])[1], 'ro')
                del points[i]
    #calculate centre
    xm = 0
    ym = 0
    for i in points:
        xm = xm + i[0]
        ym = ym + i[1]
    return ((xm / len(points),ym/ len(points)))

#-------------------------------------------------------------------------------
# Function: findRadius
#
# Finds the mean distance of a set of points (x,y) to a centre point. 
#
#-------------------------------------------------------------------------------
#
# points      - The data set.
# centre      - The centre point.
# endChange   - The ratio of variance change at which to stop.
#
# return      - The mean distance.
#-------------------------------------------------------------------------------
def findRadius(points, centre, endChange):
    #Calculate the distances of all points. This will be the most time intensive single step.
    r = []
    for i in points:
        r.append(math.sqrt(math.pow(centre[0] - i[0], 2) + math.pow(centre[1] - i[1], 2)))  
    old = -1
    #loop through
    while True:
        #get the mean and the varience.
        ms = msd(r)
        #if the varience is 0 or if the ratio target is reached, end.
        if(ms[1] == 0 or ms[1]/ old >= endChange):
            break
        #save the current varience.
        old = ms[1]
        #calculate valid range.
        compareP = ms[0] + (1 * ms[1])
        compareN = ms[0] - (1 * ms[1])
        
        #remove any item that is out of range
        for i in range(len(r)-1, -1,-1):
            if r[i] < compareN or r[i] > compareP:
                del r[i]
    return sum(r)/len(r)
