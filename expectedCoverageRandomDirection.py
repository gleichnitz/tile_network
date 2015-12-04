#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def markPoint(x, y, dimension, error, visited):
	# iterate over the square the circle around the user is inscribed in
	for i in np.arange(x - 1, x + 1 + 1, error):
		if (i < 0 or i > dimension):
			continue;
		for j in np.arange(y - 1, y + 1 + 1, error):
			if (j < 0 or j > dimension):
				continue;
			# distance from current point to center of circle
			distToCenter = math.pow(x - i, 2) + math.pow(y - j, 2)
			if distToCenter <= 1: # ... the point is within the circle -> covered
				visited[(1/error)*i][(1/error)*j] = 1
	return visited

def main():
	dimension = 10
	error = 0.1 # toggle for performance

	saturated = False
	users = 0
	trials = 20 # toggle for performance

	while(saturated == False):
		totalVisits = 0
		for t in range(trials):
			visited = np.zeros((dimension*(1/error), dimension*(1/error)))
			for u in range(users):
				# place a user in a random location in the graph
				x = int(random.randrange(0, dimension))
				y = int(random.randrange(0, dimension))
				visited = markPoint(x,y,dimension,error,visited)
				#plt.plot(i, j, 'bo')
				#plt.plot(x, y, 'rs')
			totalVisits += visited.sum()
		coverage = (1.*totalVisits)/(dimension*(1./error)*trials)
		print users
		print coverage
		plt.plot(users, coverage, 'bs')
		users += 1

		if (coverage >= 95): # toggle for better performance
			saturated = True

	plt.xlabel('number of users')
	plt.ylabel('expected coverage')
	plt.show()

main()