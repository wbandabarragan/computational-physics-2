#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

# get basic information about the MPI communicator
world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank()

if __name__ == "__main__":

    N = 10000000

    # determine the workload of each rank
    workloads = [ N // world_size for i in range(world_size) ]
    if my_rank == 0:
        print("Workloads: ", workloads)

    for i in range( N % world_size ):
        workloads[i] += 1
    
    my_start = 0
    for i in range( my_rank ):
        my_start += workloads[i]
    my_end = my_start + workloads[my_rank]
    
#    if my_rank == 0:
#        print("Rank 0's dynamic start: ", my_start)
#        print("Rank 0's dynamic end: ", my_end)
#    else:
#        print("Other ranks dynamic start: ", my_start)
#        print("Other rabks dynamic end: ", my_end)
    # initialize a
    start_time = MPI.Wtime() # Adding time stamp
    a = np.ones(N)
    end_time   = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Initialise a time: " + str(end_time - start_time))

    # initialize b
    start_time1 = MPI.Wtime() # Adding time stamp
    b = np.zeros(N)
    for i in range(N):
        b[i] = 1.0 + i
    end_time1    = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Initialise b time: " + str(end_time1 - start_time1))

    # add the two arrays
    start_time2 = MPI.Wtime() # Adding time stamp
    for i in range(N):
        a[i] = a[i] + b[i]
    end_time2 = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Adding arrays time: " + str(end_time2 - start_time2))

    # average the result
    start_time3 = MPI.Wtime() # Adding time stamp
    sum = 0.0
    for i in range(my_start, my_end):
        sum += a[i]
    #average = sum / N
    # Rank 0 gets the value of sum from itself
    if my_rank == 0:
        # The global sum
        world_sum = sum # This is only the rank 0 sum here
        # Rank0 receives messages from every procesor other than rank 0 
        for i in range( 1, world_size ):
            # First an empty array is created -> the object where rank 0 will place the msg
            sum_np = np.empty( 1 )
            
            # Receive function, which gets sum_np in format dbl from every rank (other than 0), taggest with 77  
            world_comm.Recv( [sum_np, MPI.DOUBLE], source=i, tag=77 )

            # Rank 0 places every number in an empty object and adds the next value for as many np we have 
            world_sum += sum_np[0]
        # Finally rank 0 averages all results
        average = world_sum / N
    # Any other rank (-np) stores their onwn sums in sum_np array    
    else:
        sum_np = np.array( [sum] )
        # We use the Send function to transmit the sum_np object of format dbl to rank 0 as dest, with tag 77
        world_comm.Send( [sum_np, MPI.DOUBLE], dest=0, tag=77 )
    end_time3 = MPI.Wtime() # Adding time stamp

    if my_rank == 0:
        print("Averaging result time: " + str(end_time3 - start_time3))
        print("Average: " + str(average))
