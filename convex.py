# Convex Hull Problem
# by
# Jack Pharies and Rob Ranseen

# import
import random 


# global vars
points = []
count = 0

# opens file called data.txt and creates a global list of points
# first number in list is the amount of variables
# in data.txt, x cords are on the left and y cords are on the right
#
# outputs : = pointList = list of all points genereated
def getData():
    dataFile = open("data.txt", "r")
    
    numOfPoints = int(dataFile.readline().rstrip())
    
    while numOfPoints > 0:
        stringPoint = dataFile.readline().rstrip()
        point = stringPoint.split(" ")
        point[0] = int(point[0])
        point[1] = int(point[1])
        points.append(point)
        numOfPoints = numOfPoints - 1

    dataFile.close()

    

 
    





# creates a list of psuedo-randomly generated pojnts of length n
# points that are generated are between the range of 0 and 100
#
# inputs : n = length of list.
def createData(n):
    
    gate = n
    while gate > 0:
        point = []
        x = random.randint(0, 100)
        point.append(x)
        y = random.randint(0, 100)
        point.append(y)
        copy = False
        for items in points:
            if items[0] == x and items[1] == y:
                copy = True
        if copy == False:
            points.append(point)
            gate = gate - 1

    
              
 
        
#
#
# output : points = 
def getConvexHull();










# main method, calls the other methods
def main():
    
    getData()
    print(points)









main()
