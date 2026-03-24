from mpi4py import MPI

if __name__ == "__main__":

    # World communicator = pool of processors
    world_comm = MPI.COMM_WORLD

    # This is the number of processors retrieved from -np xxxx
    world_size = world_comm.Get_size()

    # This is the ID of a specific processor
    my_rank = world_comm.Get_rank()

    # Independent msg sent by each rank
    print("World Size: " + str(world_size) + "   " + "Rank: " + str(my_rank))
