#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def markPoint(x, y, dimension, radius, visited):
	# iterate over the square the circle around the user is inscribed in
	for i in np.arange(x - radius/2., x + radius/2. + 1):
		if (i < 0 or i >= dimension):
			continue;
		for j in np.arange(y - radius/2, y + radius/2. + 1):
			if (j < 0 or j >= dimension):
				continue;
			# distance from current point to center of circle
			distToCenter = math.pow(x - i, 2) + math.pow(y - j, 2)
			if distToCenter <= radius/2.: # ... the point is within the circle -> covered
				visited[i][j] = 1
	return visited

def main():
	dimension = 1000
	radius = 100

	walk_distance = 1 # toggle for performance

	saturated = False
	users = 30
	trials = 20 # toggle for performance

	while(saturated == False):
		totalVisits = 0
		for t in range(trials):
			visited = np.zeros((dimension, dimension))
			print len(visited)
			for i in range(0,users):
				# place a user in a random location in the graph
				x = int(random.randrange(0, dimension))
				y = int(random.randrange(0, dimension))
				visited = markPoint(x,y,dimension,radius,visited)
				# choose a random direction for the user to walk
				direction = int(random.randrange(0,4))
				for j in range(0,walk_distance):
					if direction == 0 and x > :
						x -= 1

				#plt.plot(i, j, 'bo')
				#plt.plot(x, y, 'rs')
			totalVisits += visited.sum()
		coverage = (1.*totalVisits)/(dimension*trials*10)
		print users, coverage, totalVisits
		plt.plot(users, coverage, 'bs')

		saturated = True
		if (coverage >= 95): # toggle for better performance
			saturated = True

	plt.xlabel('number of users')
	plt.ylabel('expected coverage')
	plt.show()

main()