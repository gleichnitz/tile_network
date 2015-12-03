import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

def main():
    x = 100
    y = 100
    gran = 1.
    plt.figure()
    plt.xlabel("distance between people")
    plt.ylabel("number of steps to completely cover area")
    for dist in range(1,x):
        partial_sum = 0
        times = 5
        #Only running with (times = 5) b/c too slow otherwise 
        for i in range(times):
            partial_sum += computeSteps(x,y,dist,dist,gran)
        plt.plot(dist, partial_sum/times, marker='o', color='blue')
    plt.show()
    
def computeSteps(x, y, xdist, ydist, gran):    
    points = []
    locations = {}   
    visited = 0
    toVisit = x * y * gran

    #plt.figure()
    #plt.xlim([0,x])
    #plt.ylim([0,y])
    # keeping track of covered coordinates
    points_record_x = []
    points_record_y = []
    # intiializing location array to zero for each potential coordinate
    for xcoord in np.arange(0, x, gran):
        for ycoord in np.arange(0, y, gran):
            locations[(xcoord, ycoord)] = 0
            
    # try every coordinate pair (incrementing by xdist/ydist)
    for xcoord in np.arange(0, x, xdist*gran):
        for ycoord in np.arange(0, y, ydist*gran):
            points.append((xcoord, ycoord))
            locations[(xcoord, ycoord)] = 1
            visited += 1
            #plt.plot(xcoord, ycoord, marker='o', color='red')
            points_record_x.append([])
            points_record_y.append([])
    
    steps = 0
    while visited < toVisit:
        steps += 1   
        for i in range(len(points)):
            cont = True
            while cont:
                cont = False
                # randomly move either up, down, left, or right
                # with equal probability
                rand = random.randint(0, 3)
                xcoord = points[i][0]
                ycoord = points[i][1]
                newPoint = (0,1)
                if (rand == 0 and xcoord > 0):
                    newPoint = (xcoord -1, ycoord)
                elif(rand == 1 and xcoord < x-1):
                    newPoint = (xcoord + 1, ycoord)
                elif(rand == 2 and ycoord > 0):
                    newPoint = (xcoord, ycoord - 1)
                elif(rand ==3 and ycoord < y-1):
                    newPoint = (xcoord, ycoord + 1)
                else:
                    cont = True
                    continue
                points[i] = newPoint
                # record the coordinates visited - for mapping/plotting the walks
                points_record_x[i].append(newPoint[0])
                points_record_y[i].append(newPoint[1])
                #plt.plot([xcoord, newPoint[0]], [ycoord, newPoint[1]], marker='o', color='blue')
                status = locations[(points[i][0], points[i][1])]
                # change status of location if not yet visited, increment counter
                if (status == 0):
                    visited += 1
                    locations[(points[i][0], points[i][1])] = 1    
              
    print xdist, ": steps: ", steps
    return steps
    #for i in range(len(points)):
        #plt.plot(points_record_x[i], points_record_y[i], marker='o', color='blue') 
    #plt.plot(points_record_x[50], points_record_y[0], marker='o', color='blue') 
    #plt.plot(points_record_x[500], points_record_y[10], marker='o', color='blue') 
    #plt.plot(points_record_x[5000], points_record_y[20], marker='o', color='blue') 
    #plt.show()


if __name__ == "__main__":
    main()
