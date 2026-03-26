# Import the libraries
from mpi4py import MPI

# Define the communicator
comm = MPI.COMM_WORLD

# Number of processors: -np
size = comm.Get_size()

# Get the ID of the rank
rank = comm.Get_rank()

if rank == 0:
   data = [(2*x+1)**x for x in range(size)]
   print('we will be scattering: ',data)
else:
   data = None
   
data = comm.scatter(data, root=0)
print('rank '+ str(rank) + ' has data: ' + str(data))
