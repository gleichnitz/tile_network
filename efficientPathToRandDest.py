#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def main():
	# NOTE: all of my code relies on a 100x100 grid which i accomplish by doing dimension*(1/error).
	# I kept dimension = 10 to match Sams code. When we calculate expected coverage,
	# this will be good for consistency.
	dimension = 10
	error = 0.1 # toggle for performance

	saturated = False
	users = 100 # toggle for performance
	destinations = 5 # toggle for performance

	userLocations = []
	destinationLocations = []
	efficientPaths = [] # efficient paths array to keep track of most efficient path distances
	roadblocks = np.zeros((dimension*(1/error), dimension*(1/error))) # no roadblocks for now

	# assign random location for each user
	for i in range(users):
		x = random.randrange(0, dimension*(1/error))
		y = random.randrange(0, dimension*(1/error))
		userLocations.append((x, y))

	# assign random destination locations
	for i in range(destinations):
		x = random.randrange(0, dimension*(1/error))
		y = random.randrange(0, dimension*(1/error))
		destinationLocations.append((x, y))
		efficientPaths.append([]) # append an empty array to later keep track of efficient paths per destination

	# get most efficient path for each user
	for user in userLocations:
		randomDestinationChoice = random.randrange(0, destinations)
		dest = destinationLocations[randomDestinationChoice]
		(destx, desty) = dest # destination
		(userx, usery) = user # initial user position
		d = (destx-userx)**2 + (desty-usery)**2 # initial distance away
		visited = np.zeros((dimension*(1/error), dimension*(1/error))) # an array marking where user is visited
		visited[userx, usery] = 1 # initialize array for first user position

		# path arrays for plotting (because hard to plot visited array)
		pathx = []
		pathy = []
		pathx.append(userx)
		pathy.append(usery)

		# check each point directly near current point and choose to move to point that is closest to destination
		destinationReached = False
		while (destinationReached == False):
			chosenPoint = (0,0)
			for i in np.arange(userx - 1, userx + 1 + 1):
				if (i < 0 or i > dimension*(1/error)):
					continue;
				for j in np.arange(usery - 1, usery + 1 + 1):
					if (j < 0 or j > dimension*(1/error)):
						continue;
					# distance from current point to dest
					distToDest = math.pow(destx - i, 2) + math.pow(desty - j, 2)
					if (distToDest <= d and roadblocks[i,j] != 1): # ... distance less than the one from the original poitn -> update d to find chosen point to move to
						d = distToDest
						chosenPoint = (i,j)
			(xcoord, ycoord) = chosenPoint
			userx = xcoord # update x coord of user to be at chosen point
			usery = ycoord # update y coord of user to be at chosen point
			visited[userx, usery] = 1 # keep track of path in array
			
			# keep track of path in lists for plotting
			pathx.append(userx)
			pathy.append(usery)
			if (userx == destx and usery == desty): # if we have reached our destination -> destinationReached = true
				destinationReached = True

		# add final path of squares to list of efficient paths for a given destination
		efficientPaths[randomDestinationChoice].append((pathx, pathy))

	# plot efficient paths for each destination
	for i in efficientPaths:
		plt.figure()
		plt.xlim(0,dimension*(1/error))
		plt.ylim(0,dimension*(1/error))
		plt.xlabel('x')
		plt.ylabel('y')
		# plot each invidiual path
		for (x, y) in i:
			plt.plot(x, y, marker=".")
			plt.plot(x[len(x)-1], y[len(y)-1], 'o')
	plt.show()

main()