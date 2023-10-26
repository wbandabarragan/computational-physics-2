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

   # Defining workloads
   # Determine the workload of each rank
   workloads = [ N // world_size for i in range(world_size) ]

   # Leftover elements -> modulus op. 
   for i in range( N % world_size ):
       workloads[i] += 1

   # Define start and end for each rank
   my_start = 0
   for i in range( my_rank ):
        my_start += workloads[i]
   my_end = my_start + workloads[my_rank]

   # Printing our control objects (my_start and my_end) 
   print("Printing workloads: " + str(workloads))
   print("Printing my_start: " + str(my_start))
   print("Printing my_end: " + str(my_end))  

   # Add an init time stamp
   start_time_a = MPI.Wtime()
   # Initialise the first vector
   a = np.ones(workloads[my_rank])
   # Add an end time stamp
   end_time_a = MPI.Wtime()
   
   # Printing the a time stamp
   if my_rank == 0:
      print("Initialize a time: " + str(end_time_a - start_time_a)) 

   # Add an init time stamp
   start_time_b = MPI.Wtime()
   # Initialise the second vector
   b = np.zeros(workloads[my_rank])

   # Add values to b
   for i in range(workloads[my_rank]):
       b[i] = 1.0 + (i + my_start)

   # Add an end time stamp
   end_time_b = MPI.Wtime()

   # Printing the a time stamp
   if my_rank == 0:
      print("Initialize b time: " + str(end_time_b - start_time_b))

   # Add an init time stamp
   start_time_s = MPI.Wtime()

   # Add the two arrays (PARALELISATION PART 1)
   for i in range(workloads[my_rank]):
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
   for i in range(workloads[my_rank]):
       summ += a[i]
   
   if my_rank == 0:
       # Get the summ of rank 0 only
       world_summ = summ
       # Now get the summs from all ranks > 0
       for i in range(1, world_size):
           # Create an epy object to receive the information from each rank
           summ_np = np.empty(1)
           # Receive the MPI message from each rank
           world_comm.Recv([summ_np, MPI.DOUBLE], source = i, tag = 77)
           world_summ += summ_np[0]
           average = world_summ / N
   else:
       # Information to be sent vy ranks > 0
       summ_np = np.array([summ])
       # Call MPI to send this object (summ_np)
       world_comm.Send( [summ_np, MPI.DOUBLE], dest = 0, tag = 77)
   #average = summ/N 

   # Add an end time stamp
   end_time_m = MPI.Wtime()

   # Printing the a time stamp
   if my_rank == 0:
      print("The average operation time: " + str(end_time_m - start_time_m))
      print("Average is: ", str(average))

