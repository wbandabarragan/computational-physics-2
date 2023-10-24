#!/usr/bin/env python3

# Importing libraries
import numpy as np
from mpi4py import MPI

# Call main to execute the script

if __name__ == "__main__":

   # Define our communicator for MPI
   world_comm = MPI.COMM_WORLD

   # Get size of our CPU
   world_size = world_comm.Get_size()

   # Get the ranks (ID for the processors)
   my_rank = world_comm.Get_rank()

   # Define a vector size
   N = 10000000

   # Add an init time stamp
   start_time_a = MPI.Wtime()
   # Initialise the first vector
   a = np.ones(N)
   # Add an end time stamp
   end_time_a = MPI.Wtime()
   
   # Printing the a time stamp
   if my_rank == 0:
      print("Initialize a time: " + str(end_time_a - start_time_a)) 

   # Add an init time stamp
   start_time_b = MPI.Wtime()
   # Initialise the second vector
   b = np.zeros(N)

   # Add values to b
   for i in range(N):
       b[i] = 1.0 + i

   # Add an end time stamp
   end_time_b = MPI.Wtime()

   # Printing the a time stamp
   if my_rank == 0:
      print("Initialize b time: " + str(end_time_b - start_time_b))

   # Add an init time stamp
   start_time_s = MPI.Wtime()

   # Add the two arrays (PARALELISATION PART 1)
   for i in range(N):
       a[i] = a[i] + b[i]

   # Add an end time stamp
   end_time_s = MPI.Wtime()

   # Printing the a time stamp
   if my_rank == 0:
      print("The sum operation time: " + str(end_time_s - start_time_s))

   # Add an init time stamp
   start_time_m = MPI.Wtime()

   # Average of the result (PARALELISATION PART 2)
   summ = 0.0

   # For loop
   for i in range(N):
       summ += a[i]
   average = summ/N 

   # Add an end time stamp
   end_time_m = MPI.Wtime()

   # Printing the a time stamp
   if my_rank == 0:
      print("The average operation time: " + str(end_time_m - start_time_m))

   # Print result
   if my_rank == 0:
       print("Average is: ", str(average))

