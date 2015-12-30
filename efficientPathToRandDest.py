#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random
import csv


def main():
	# NOTE: all of my code relies on a 100x100 grid which i accomplish by doing dimension*(1/error).
	# I kept dimension = 10 to match Sams code. When we calculate expected coverage,
	# this will be good for consistency.


	with open('mapallpaths3.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		roadBlockListImport = list(csvreader)
		roadBlockList = roadBlockListImport[:32] # got rid of extra empty lines in file
		roadblocks = np.array(roadBlockList).astype('int')
		print roadblocks.shape


		dimensionx = 3.1
		dimensiony = 3.6
		error = 0.1 # toggle for performance

		saturated = False
		users = 500 # toggle for performance
		destinations = 250 # toggle for performance

		userLocations = []
		destinationLocations = []
		efficientPaths = [] # efficient paths array to keep track of most efficient path distances

		# assign random location for each user
		for i in range(users):
			roadblockCheck = False
			while roadblockCheck != True:
				x = random.randrange(0, dimensionx*(1/error))
				y = random.randrange(0, dimensiony*(1/error))
				if roadblocks[x, y] == 1:
					roadblockCheck = True
			userLocations.append((x, y))
			#print roadblocks[x, y]

		# assign random destination locations
		for i in range(destinations):
			roadblockCheck = False
			while roadblockCheck != True:
				x = random.randrange(0, dimensionx*(1/error))
				y = random.randrange(0, dimensiony*(1/error))
				if roadblocks[x, y] == 1:
					roadblockCheck = True
				if (x,y) in userLocations:
					roadBlockCheck = False

			destinationLocations.append((x, y))
			efficientPaths.append([]) # append an empty array to later keep track of efficient paths per destination

		# get most efficient path for each user
		for user in userLocations:
			randomDestinationChoice = random.randrange(0, destinations)
			dest = destinationLocations[randomDestinationChoice]
			(destx, desty) = dest # destination
			(userx, usery) = user # initial user position
			d = (destx-userx)**2 + (desty-usery)**2 # initial distance away
			visited = np.zeros((dimensionx*(1/error)+1, dimensiony*(1/error)+1)) # an array marking where user has visited
			visited[userx, usery] = 1 # initialize array for first user position

			# path arrays for plotting (because hard to plot visited array)
			pathx = []
			pathy = []
			pathx.append(userx)
			pathy.append(usery)

			# check each point directly near current point and choose to move to point that is closest to destination
			destinationReached = False
			
			visitedPoints = []
			while (destinationReached == False):
				possibleNextSteps = []
				for i in np.arange(userx - 1, userx + 1 + 1):
					if (i < 0 or i > dimensionx*(1/error)):
						continue;
					for j in np.arange(usery - 1, usery + 1 + 1):
						if (j < 0 or j > dimensiony*(1/error)):
							continue;
						if (roadblocks[i,j] == 0):
							continue;
						if (i == userx and j == usery):
							continue;

						possibleNextSteps.append((i,j))

				chosenPoint = possibleNextSteps[0]
				dMin = 1000000
				for (i, j) in possibleNextSteps:
						# distance from current point to dest
					distToDest = math.pow(destx - i, 2) + math.pow(desty - j, 2)
					if ((i, j) not in visitedPoints): # ... distance less than the one from the original point -> update d to find chosen point to move to
						if (distToDest <= dMin): 
							dMin = distToDest
							chosenPoint = (i,j)
				# print distToDest
				(xcoord, ycoord) = chosenPoint
				userx = xcoord # update x coord of user to be at chosen point
				usery = ycoord # update y coord of user to be at chosen point
				visited[userx, usery] = 1 # keep track of path in array
				visitedPoints.append((userx, usery))
				
				# keep track of path in lists for plotting
				pathx.append(userx)
				pathy.append(usery)
				print "***"
				print userx, usery
				print destx, desty
				# print roadblocks[userx, usery]

				if (userx == destx and usery == desty): # if we have reached our destination -> destinationReached = true
					destinationReached = True

			# add final path of squares to list of efficient paths for a given destination
			efficientPaths[randomDestinationChoice].append((pathx, pathy))

		# plot efficient paths for each destination
		for i in efficientPaths:
			#plt.figure()
			plt.xlim(0,dimensiony*(1/error))
			plt.ylim(0,dimensionx*(1/error))
			plt.xlabel('x')
			plt.ylabel('y')
			# plot each invidiual path
			for (x, y) in i:
				plt.plot(y, x, marker=".")
				plt.plot(y[len(y)-1], x[len(x)-1], 'o')
		plt.show()

main()
