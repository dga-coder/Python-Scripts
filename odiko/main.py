import os
import math
#CONSTANTS -- modify these 
POINT1 = (480009.081702929,4200677.33213743)
POINT2 = (479517.5210926,4200839.92440093)
STEP_SIZE = 2
ar =[30,34]

dx = POINT2[0] - POINT1[0]
dy = POINT2[1] - POINT1[1]

bearing = math.atan2(dy,dx)
print "Bearing: {b}".format(b=bearing)
#Use pythagoras to work out the distance
distance_between_points = math.sqrt(dx**2+dy**2) 

for p in range(30,34,2):
    x = POINT1[0] + p * math.cos(bearing)
    y = POINT1[1] + p * math.sin(bearing)
    print "Intermediate point {x},{y}".format(x=x,y=y)
    print p 
    
    