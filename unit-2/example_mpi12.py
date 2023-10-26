#!/usr/bin/env python3

# Example of Broadcasting
from mpi4py import MPI

# Define the communicator
world_comm = MPI.COMM_WORLD

# Get the rank
my_rank = world_comm.rank

# rank 0 will be the one broadcasting

if my_rank ==0:
      # Sample data
      sample_dict = {"key 1": 1, "key 2": 2, "key 3": 3}

else:
      # No data
      sample_dict = None

# Broadcasting the message
sample_dict = world_comm.bcast(sample_dict, root = 0)

# Printing the data info
print("Rank: ", my_rank, sample_dict)
