import numpy as np
from mpi4py import MPI

if __name__ == "__main__":

    # get basic information about the MPI communicator
    world_comm = MPI.COMM_WORLD
    world_size = world_comm.Get_size()
    my_rank = world_comm.Get_rank()

    N = 10000000

    # initialize a
    start_time = MPI.Wtime()
    a = np.ones(N)
    end_time = MPI.Wtime()
    if my_rank == 0:
        print("Initialize a time: " + str(end_time-start_time))
    elif my_rank == 1:
        print("I am rank 1.")
    else:
        print("I am also here.")
    
    # initialize b
    b = np.zeros( N )
    for i in range( N ):
        b[i] = 1.0 + i

    # add the two arrays
    for i in range( N ):
        a[i] = a[i] + b[i]

    # average the result
    sum = 0.0
    for i in range( N ):
        sum += a[i]
    average = sum / N

    print("Average: " + str(average))
