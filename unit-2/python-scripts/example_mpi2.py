#!/usr/bin/env python

from mpi4py import MPI


if __name__ == "__main__":

    # Define world comm
    world_comm = MPI.COMM_WORLD

    # Get size of the world
    world_size = world_comm.Get_size()

    # Call ranks
    my_rank = world_comm.Get_rank()

    #print("Hello World!")

    # Print world size and ranks
    print("World Size: " + str(world_size) + "   " + "Rank: " + str(my_rank))
