#!/usr/bin/env python3

# Example on scattering/gathering
from mpi4py import MPI

# Define the communicator
world_comm = MPI.COMM_WORLD

# Get workd size
world_size = world_comm.Get_size()

# Get the rank
my_rank = world_comm.Get_rank()

# Generate data in rank = 0 to be scattered

if my_rank == 0:
    sample_data = [(4.*y + 1.)**y for y in range(world_size)]
    print("These are the data to be scattered", sample_data)
else:
    sample_data = None

# Scatter the data from rank = 0
sample_data = world_comm.scatter(sample_data, root = 0)

# Modify the data
sample_data *= 10

# Printing the info from each rank
print("Rank: " + str(my_rank) + " sees: " + str(sample_data))

# Gather the data and put it into a new object
new_sample_data = world_comm.gather(sample_data, root = 0)

# Print the gathered result -> rank =0

if my_rank ==0:
    print("The gathered data look like: ", new_sample_data)

