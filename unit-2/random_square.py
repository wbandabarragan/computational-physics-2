#!/usr/bin/env python3

import numpy as np

# Function to allocate a seed and generate squared random #s
def random_square(seed):
	"""
	Takes in a seed and returns the square of a random #
	"""
	# Allocate the seed
	np.random.seed(seed)

	# Generate random #
	random_num = np.random.randint(0, 10)

	# Return squared values
	random_sq = random_num**2

	return random_sq 


