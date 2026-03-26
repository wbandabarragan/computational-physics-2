# Import the MPI library
from mpi4py import MPI  

# Create a world communicator
comm = MPI.COMM_WORLD 

# Get the total number of processes and rank IDs in the communicator
size = comm.Get_size()  
rank = comm.Get_rank()

# If the current process is the root process (rank 0)
if rank == 0:
    
    # List of data with (x+1)^x.
    data = [(2*x + 1) ** x for x in range(size)]
    
    # Print the data that will be scattered
    print('we will be scattering:', data)  

else:
    # Initialize data to None, non-root processes will receive data via scatter
    data = None  

# Distribute the data list from the root process to all processes, each receiving one element.
data = comm.scatter(data, root=0)  

# The root process also receives its own data and 
data += 10  

# Print the rank and the modified data on each proces
print('rank', rank, 'has new data:', data)

# Gather the modified data from all processes to the root process
newData = None
newData = comm.gather(data, root=0)  

# If the current process is the root process
if rank == 0:
    # Print the gathered data on the root process
    print('master:', newData)  
