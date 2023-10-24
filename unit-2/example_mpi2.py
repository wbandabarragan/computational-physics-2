#!/usr/bin/env python3

# Import MPI
from mpi4py import MPI

if __name__ == "__main__":

   # Define our communicator for MPI
   world_comm = MPI.COMM_WORLD

   # Get size of our CPU
   world_size = world_comm.Get_size()

   # Get the ranks (ID for the processors)
   my_rank = world_comm.Get_rank()

   #print("Hola, mundo.")
   print("World Size: " + str(world_size) + "   " + "Rank: " + str(my_rank))
