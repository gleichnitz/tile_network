#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

from pymobility.models.mobility import random_waypoint


def main():
    dimension = 100
    gran = 1.
    plt.figure()
    plt.title("Random Waypoint Mobility Model")
    plt.xlabel("number of users")
    plt.ylabel("expected number of steps to completely cover 100x100 area")
    # ^ (because users move at varying speeds, "steps" means steps of the model)
    for users in range(20, 110, 10):
        print "num users: %d" % users
        partial_sum = 0
        trials = 5
        for t in range(trials):
            visited = np.zeros((dimension, dimension)) 
            # create random waypoint mobility model object
            rw = random_waypoint(users, dimensions=(1, 1), 
            	velocity=(0.1, 1.), wt_max=1.0) 
            # compute num steps for total coverage
            partial_sum += computeSteps(rw, visited, dimension, gran)
        plt.plot(users, partial_sum/trials, marker='o', color='blue')
    plt.show()
    

def computeSteps(rw, visited, dimension, gran):
    steps = 0
    toVisit = dimension * dimension * gran
    for positions in rw:
        for i in range(len(positions)):
            x = int(positions[i][0]*100)
            y = int(positions[i][1]*100)
            markPoint(x, y, dimension, visited, gran)
        steps += 1
        totalVisits = visited.sum()
        # all points in region have been covered
        if (totalVisits >= toVisit):
            break
    print steps
    return steps


def markPoint(x, y, dimension, visited, gran):
    # iterate over the square the circle around the user is inscribed in
    for i in np.arange(x - 1, x + 1 + 1):
        if (i < 0 or i >= dimension):
            continue;
        for j in np.arange(y - 1, y + 1 + 1):
            if (j < 0 or j >= dimension):
                continue;
            # distance from current point to center of circle
            distToCenter = math.pow(x - i, 2) + math.pow(y - j, 2)
            if distToCenter <= 1: # ... the point is within the circle -> covered
                visited[(1/gran)*i][(1/gran)*j] = 1
                

if __name__ == "__main__":
    main()
