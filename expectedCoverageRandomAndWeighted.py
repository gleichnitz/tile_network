#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import random


def generateRandom(dimension):
	val1 = int(random.randrange(0, dimension))
	dec1 = random.randrange(0, 10)*.1
	x = val1 + dec1 
	val2 = int(random.randrange(0, dimension))
	dec2 = random.randrange(0, 10)*.1
	y = val2 + dec2
	return x, y


def generateWeightedRandom(weighted_locations, dimension):
	random_prob = 0.5 # probability of being in a random location
	if random.random() < random_prob:
		x, y = generateRandom(dimension)
	else:
		# choose a weighted location uniformly at random
		location = int(random.randrange(0, len(weighted_locations)))
		x, y = weighted_locations[location]
	return x, y


def coverage(x, y, visited, dimension, error):
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


def main():
	dimension = 10
	error = 0.1 # toggle for performance

	users = 0
	trials = 10 # toggle for performance

	plt.plot(users, 0, 'bs', label='random')
	plt.plot(users, 0, 'rs', label='weighted')
	users += 1

	saturated = False

	num_weighted_locations = 4 # toggle
	weighted_locations = [None]*num_weighted_locations

	# generate random weighted locations
	for i in range(num_weighted_locations):
		x = int(random.randrange(0, dimension))
		y = int(random.randrange(0, dimension))
		weighted_locations[i] = [x, y]

	while(saturated == False):
		totalVisits_random = 0
		totalVisits_weighted = 0
		for t in range(trials):
			visited_random = np.zeros((dimension*(1/error), dimension*(1/error)))
			visited_weighted = np.zeros((dimension*(1/error), dimension*(1/error)))
			for u in range(users):
				x_random, y_random = generateRandom(dimension)
				x_weighted, y_weighted = generateWeightedRandom(weighted_locations, dimension)

				coverage(x_random, y_random, visited_random, dimension, error)
				coverage(x_weighted, y_weighted, visited_weighted, dimension, error)

			totalVisits_random += visited_random.sum()
			totalVisits_weighted += visited_weighted.sum()
		coverage_random = (1.*totalVisits_random)/(dimension*(1./error)*trials)
		coverage_weighted = (1.*totalVisits_weighted)/(dimension*(1./error)*trials)

		plt.plot(users, coverage_random, 'bs')
		plt.plot(users, coverage_weighted, 'rs')
		users += 1

		if (coverage_weighted >= 90): # toggle for performance
			saturated = True

	plt.xlabel('number of users')
	plt.ylabel('expected coverage')
	plt.legend(loc='upper left')
	plt.show()

main()