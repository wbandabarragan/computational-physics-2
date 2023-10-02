# POP: functions

# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Function to generate density maps

def get_map(bsize, ftype):
	"""
	This function takes to inputs:
	bsize = box size as a float
	ftype = field type as string
	Return a map of the density field
	"""

	# Define vectors
	x = np.linspace(-1., +1., bsize)
	y = np.linspace(-1., +1., bsize)

	# Meshgrid
	x_2d, y_2d = np.meshgrid(x, y)

	# Comment
	print("The grid has been generated.")

	# Select density field
	if ftype == "uniform":
		# Generate 2D surface
		z_2D = np.ones((bsize,bsize))
	elif ftype == "random":
		# Generate 2D random field
		z_2D = np.random.normal(2., 1.5, size=(bsize,bsize))
	elif ftype == "harmonic":
		# Generate 2D harmonic field
		z_2D = zharmonic(x_2d, y_2d)
	else:
		# Default density field
		z_2D = np.zeros((bsize,bsize))
       
	# Modulus
	z_mod = np.sqrt(z_2D**2 + z_2D**2) 

	# Plotting
	fig, ax = plt.subplots(figsize=(5,5))

	im = ax.quiver(x_2d, y_2d, z_2D, z_2D, z_mod, cmap = "viridis")

	fig.colorbar(im, ax=ax)

	print("Plot is ready.")

	return fig
	 

def zharmonic(xx, yy):
	"""
	Generate harmonic density map.
	"""
	
	zz = np.sin(10.*xx) + 0.5*np.cos(5.*yy)
	
	return zz








