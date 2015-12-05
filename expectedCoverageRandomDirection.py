#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def markPoint(x, y, dimension, radius, visited):
	# iterate over the square the circle around the user is inscribed in
	for i in np.arange(x - radius, x + radius + 1):
		if (i < 0 or i >= dimension):
			continue;
		for j in np.arange(y - radius, y + radius + 1):
			if (j < 0 or j >= dimension):
				continue;
			# distance from current point to center of circle
			distToCenter = math.sqrt(math.pow(x - i, 2) + math.pow(y - j, 2))
			if distToCenter <= radius: # ... the point is within the circle -> covered
				visited[i][j] = 1
	return visited

def inBounds(coord, dimension):
	if coord > 0 and coord < dimension:
		return True
	return False

def main():
	dimension = 1000
	radius = 100

	walk_distance = 10 # toggle for performance

	saturated = False
	users = 30
	trials = 5 # toggle for performance

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
					if direction == 0:
						if inBounds(x-1, dimension):
							x -= 1
							visited = markPoint(x,y,dimension,radius,visited)
						else:
							direction = int(random.randrange(0,4))
					if direction == 1:
						if inBounds(y+1, dimension):
							y += 1
							visited = markPoint(x,y,dimension,radius,visited)
						else:
							direction = int(random.randrange(0,4))
					if direction == 2:
						if inBounds(x+1, dimension):
							x += 1
							visited = markPoint(x,y,dimension,radius,visited)
						else:
							direction = int(random.randrange(0,4))
					if direction == 3:
						if inBounds(y-1, dimension):
							y -= 1
							visited = markPoint(x,y,dimension,radius,visited)
						else:
							direction = int(random.randrange(0,4))

				#plt.plot(i, j, 'bo')
				#plt.plot(x, y, 'rs')
			totalVisits += visited.sum()
		coverage = (1.*totalVisits)/(dimension*trials*dimension)
		print users, coverage, totalVisits
		plt.plot(users, coverage, 'bs')

		saturated = True
		if (coverage >= 95): # toggle for better performance
			saturated = True

	plt.xlabel('number of users')
	plt.ylabel('expected coverage')
	plt.show()

main()