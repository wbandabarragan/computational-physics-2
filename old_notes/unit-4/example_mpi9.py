#!/usr/bin/env python

from mpi4py import MPI
import numpy as np

if __name__ == "__main__":

    # get basic information about the MPI communicator
    world_comm = MPI.COMM_WORLD
    world_size = world_comm.Get_size()
    my_rank = world_comm.Get_rank()

    N = 10000000

    # Start parallelisation: point-point comm

    # determine the workload of each rank

    workloads = [ N // world_size for i in range(world_size) ]

    for i in range( N % world_size ):
        workloads[i] += 1
    my_start = 0

    for i in range( my_rank ):
        my_start += workloads[i]
    my_end = my_start + workloads[my_rank]

    print("Printing workloads: " + str(workloads))
    print("Printing my_start: " + str(my_start))
    print("Printing my_end: " + str(my_end))

    # initialize a
    start_time = MPI.Wtime() # Adding time stamp
    #a = np.ones(N)
    a = np.ones(workloads[my_rank])
    end_time   = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Initialise a time: " + str(end_time - start_time))

    # initialize b
    start_time1 = MPI.Wtime() # Adding time stamp
    b = np.zeros(workloads[my_rank])
    for i in range(workloads[my_rank]):
        b[i] = 1.0 + (i + my_start)
    end_time1    = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Initialise b time: " + str(end_time1 - start_time1))

    # add the two arrays
    start_time2 = MPI.Wtime() # Adding time stamp
    for i in range(workloads[my_rank]):
        a[i] = a[i] + b[i]
    end_time2 = MPI.Wtime() # Adding time stamp

    # Print the time
    if my_rank == 0:
        print("Adding arrays time: " + str(end_time2 - start_time2))

    # average the result
    start_time3 = MPI.Wtime() # Adding time stamp
    sum = 0.0
    #for i in range(N):
    for i in range(workloads[my_rank]):
        sum += a[i]
    #average = sum / N
    if my_rank == 0:
    	world_sum = sum
    	for i in range(1, world_size):
    		sum_np = np.empty(1)
    		world_comm.Recv([sum_np, MPI.DOUBLE], source=i, tag=77)
    		world_sum += sum_np[0]
    		average = world_sum / N
    else:
    	sum_np = np.array( [sum] )
    	world_comm.Send( [sum_np, MPI.DOUBLE], dest=0, tag=77 )

    end_time3 = MPI.Wtime() # Adding time stamp

    if my_rank == 0:
        print("Averaging result time: " + str(end_time3 - start_time3))
        print("Average: " + str(average))
