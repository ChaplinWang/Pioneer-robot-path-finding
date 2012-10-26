import math
    
#-------------------------------------------------------------------------------
# Function: dataParser
#
# Takes a LaserScan ros message and extracts possible data groups that may
# contain a circle.
#
#-------------------------------------------------------------------------------
#
# data          - The LaserScan message.
# range_max     - If any point in the scan if further than this from the origin
#                 then it will be ignored.
# grad_tol      - The tolerance in gradient difference when finding an removing
#                 straight lines. Try 0.3.
# split_multi   - The multiplier for the split function. Try 2.5.
#
# prune_lines   - Flag that indicates if lines should be removed.
#
# return        - An array containing arrays of (x,y) points that could possibly
#                 be on circle edges.   
#-------------------------------------------------------------------------------
def dataParser(data,range_max, grad_tol, split_multi, prune_lines ):

    # Clear out all points that are outside of the maximum range. Place each
    # group of consecutive in range points into an array and store if their
    # count is greater or equal to 3 (minimum number of points to define a
    # circle). Also converts each point to Cartesian coordinates
    possibles = []
    current = []
    for i in range(len(data.ranges)):
        if data.ranges[i] <= range_max :
            angle = data.angle_min + i*data.angle_increment
            
            current.append( (data.ranges[i] * math.cos(angle), data.ranges[i] * math.sin(angle)) )
        else:
            if len(current) >= 3:
                possibles.append(current)
            current = []            
    if len(current) >= 3:
        possibles.append(current)     
    
    # Prune out any obvious straight lines.
    if prune_lines :
        for i in range(len(possibles)):
            loop = True
            while(loop):
                loop = prune(possibles[i], grad_tol)
            
    # Split groups of points that are to far apart to be circles.
    new = []
    for i in possibles:
        splits = split(i, split_multi)
        for x in splits:
            new.append(x)
    return new
      
#-------------------------------------------------------------------------------
# Function: prune
#
# Takes a set of (x,y) points and prunes out any straight lines. 
#
# Sets of three or more points with the same gradient (within a passed 
# tolerance) will be removed from the data.
#
#-------------------------------------------------------------------------------
#
# points        - An array of (x,y) points.
# grad_tol      - The tolerance of gradient difference that is acceptable in the
#                 line.
#
# return        - True if any points were removed. False if no changes.
#-------------------------------------------------------------------------------
def prune(points, grad_tol):  
    if len(points) < 4:
        return False
    removes = []
    gradients = getGradients(points)
    for i in range(len(gradients) - 2):
        if math.sqrt(math.pow(gradients[i],2) + math.pow(gradients[i+1],2) + math.pow(gradients[i+2],2) ) < grad_tol:
                if not i in removes:
                    removes.append(i)
                if not i + 1 in removes:
                    removes.append(i+1)
                if not i + 2 in removes:
                    removes.append(i+2)
                
    removes.reverse()
    for x in removes:
        del points[x]
    return (len(removes) != 0)
    

#-------------------------------------------------------------------------------
# Function: getGradients
#
# Takes a set of (x,y) points and returns an array that contains the gradients 
# between these points
#
#-------------------------------------------------------------------------------
#
# points        - An array of (x,y) points,
#
# return        - An array containing the gradients of the lines passing each 
#                 consecutive pair of points. Length will be one less than that 
#                 of the array sent passed to it.
#-------------------------------------------------------------------------------
def getGradients(points):
    if len(points) < 2:
        return None
    gradients = []
    for u in range(len(points)-1):
        y1 = (points[u])[1]
        y2 = (points[u+1])[1]
        x1 = (points[u])[0]
        x2 = (points[u+1])[0]
        gradient = ((y2 - y1)/(x2 -x1))
        gradients.append(gradient)
    return gradients
    
#-------------------------------------------------------------------------------
# Function: split
#
# Takes a set of points and splits the group at any interval where the distance
# between two points exceeds a projected expected distance. This separates out
# the data into clumps of points that are relatively close to their neighbours.
#
# Take a sample. Assume that it is on the edge of a circle that fits exactly
# between the next and previous samples (in this case, 1 degree). The projected
# next sample will be at the edge of this circle. If the circle is in truth
# larger than the sample will occur 'closer' to the first sample.
#
# This function finds the distance between two samples and the projected
# distance of the next sample. If the true distance is <= to the projection
# then then no split occurs. If it is greater then it is assumed that the point
# cannot be on a circle edge and a split occurs.
#
# This does have problems with samples on the further edges of circles. To
# counter this, a the projected distance is scaled up by a multiplier. This
# multiplier must be well chosen else circle data will be split or clump jumps
# will be missed.
#
#-------------------------------------------------------------------------------
#
# points        - The points to search for splits.
# multiplier    - The projection multiplier.
#
# return        - An array containing arrays of (x,y) points that were sections 
#                 of the passed point array. If no splits occurred then this 
#                 will be the passed array.
#-------------------------------------------------------------------------------
def split(points, multiplier):
    ret = []
    current = []
    for i in range(len(points) -1):
        current.append(points[i])
        x1 = (points[i])[0]
        y1 = (points[i])[1]
        x2 = (points[i+1])[0]
        y2 = (points[i+1])[1]
        
        d = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
        
        projected_dist = math.sqrt(x2*x2 + y2*y2) * math.sin( math.pi / 180)
        
        measured_dist = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
        if(measured_dist > 2.5 * projected_dist):
            if len(current) >= 3:
                ret.append(current)
            current = []
    current.append(points[len(points) - 1])
    if len(current) >= 3:   
        ret.append(current)
    return ret
