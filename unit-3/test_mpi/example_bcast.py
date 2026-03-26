from mpi4py import MPI

# Define the world comm
comm = MPI.COMM_WORLD

# Rank
rank = comm.rank

if rank == 0:
    # Dictionary which only rank 0 has
    data = {'a':1,'b':2,'c':3}
else:
    # ALl the other ranks have nothing
    data = None

# World coom is broadcasting from rank 0 its dictionary
data = comm.bcast(data, root=0)

# Print the info for all ranks
print('rank',rank,data)
