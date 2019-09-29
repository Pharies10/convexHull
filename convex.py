# Convex Hull Problem
# by
# Jack Pharies and Rob Ranseen

# import
import random 


# global vars
points = []
count = 0
found = False
convexList = []


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
# param : n = length of list.
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
# output : convexList = points in a convex hull, no repeates
def getConvexHull():
    firstItem = points[0]
    xLow = firstItem[0]
    

    # since we know the an extreme must be the lowest x value, we start by finding the smallest x value
    for item in points:
        if item[0] < xLow:
            xLow = item[0]

    
    convexList.append(xLow)
    
  
    while found == False:
  
        for point in convexList:
            nextPoint = False
            pointsCount = points.length()
            while nextPoint == False and pointsCount >= 0:
                testPoint = points[pointsCount]
                if point[0] =! testPoint[0] and point[1] =! testPoint[1]:
                    nextPoint = checkLineSegment(point, testPoint)
            if nextPoint == True:
                convexList.append(testPoint)
                
    return convexList
                    

# checks if all the points of points lie on one side of the line or not
#
# param : index1, index2 = two distinct points from the list of points
#
# output : True if all the points lie on one side
#          False if the points do not all lie on same side
def checkLineSegment(index1, index2):
    a, b, c = findLine()

    for items in points:
        
    





# calculates the values a, b, c by from the parameters by which the formula ax+by=c is made
#
# param : index1, index2 = two distinct points from the list of points
#
# output : a,b,c = the three values that are calculated 
def findLine(index1, index2):

    a = index2[1] - index1[1]

    b = index1[0] - index2[0]

    c = (index1[0] * index2[1]) - (index2[0] * index1[1])

    return a, b, c
    







    

# main method, calls the other methods
def main():
    
    getData()
    getConvexHull()
    








main()
