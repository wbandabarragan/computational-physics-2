# Based on this code:
# https://stackoverflow.com/questions/36025188/along-what-axis-does-mpi4py-scatterv-function-split-a-numpy-array/36082684

# Import libraries
import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

# Call MPI, # processors, etc.
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# If processor 0
if rank == 0:
    
    # Create array 1
    array1 = np.zeros([512,512]) 
    array1 = np.ones([512,512])

    # Create array 2
    array2 = np.zeros([512,512]) 
    array2 = np.ones([512,512])
 
     # Output 0's array of same size
    outputArray = np.zeros([512,512])
    
    # Use # of cores to split the array along an axis
    splitt = np.array_split(array1,size,axis = 0)
    
    split_sizes = []

    # Fill split_sizes 
    for i in range(0,len(splitt),1):
        split_sizes = np.append(split_sizes, len(splitt[i]))

    # For input data
    split_sizes_input = split_sizes*512
    displacements_input = np.insert(np.cumsum(split_sizes_input),0,0)[0:-1]

    # For output data
    split_sizes_output = split_sizes*512
    displacements_output = np.insert(np.cumsum(split_sizes_output),0,0)[0:-1]


    print("Input data split into vectors of sizes %s" %split_sizes_input)
    
    print("Input data split with displacements of %s" %displacements_input)
    
    #plt.figure(figsize=(4,3))
    #plt.imshow(array1)
    #plt.show()
    #plt.clf()
    #plt.imshow(array1)
    #plt.colorbar()
    #plt.title('Input data 1')
    #plt.savefig('./array1.png')

    
    #plt.clf()
    #plt.imshow(array2)
    #plt.colorbar()
    #plt.title('Input data 2')
    #plt.savefig('./array2.png')
    #plt.close
    
    
else:
    #Create variables on other cores
    split_sizes_input = None
    displacements_input = None
    split_sizes_output = None
    displacements_output = None
    splitt = None
    array1 = None
    array2 = None
    outputArray = None

splitt = comm.bcast(splitt, root=0) #Broadcast split array to other cores
split_sizes = comm.bcast(split_sizes_input, root = 0)
displacements = comm.bcast(displacements_input, root = 0)
split_sizes_output = comm.bcast(split_sizes_output, root = 0)
displacements_output = comm.bcast(displacements_output, root = 0)

#Create array to receive subset of data on each core, where rank specifies the core
output_chunk_1 = np.zeros(np.shape(splitt[rank])) 
output_chunk_2 = np.zeros(np.shape(splitt[rank])) 

print("Rank %d with output_chunk 1 shape %s" %(rank,output_chunk_1.shape))
print("Rank %d with output_chunk 2 shape %s" %(rank,output_chunk_2.shape))

#Scatter both arrays using displacements
comm.Scatterv([array1,split_sizes_input, displacements_input,MPI.DOUBLE],output_chunk_1,root=0)
comm.Scatterv([array2,split_sizes_input, displacements_input,MPI.DOUBLE],output_chunk_2,root=0)

#Create output array on each core
output = np.zeros([len(output_chunk_1),512]) 

for i in range(0,np.shape(output_chunk_1)[0],1):
    output[i,0:512] = output_chunk_1[i] + 2*output_chunk_2[i]

#plt.clf()
#plt.imshow(output)
#plt.title("Output shape %s for rank %d" %(output.shape,rank))
#plt.colorbar()
#plt.savefig('./array_total.png')
print("Output shape %s for rank %d" %(output.shape,rank))

comm.Barrier()

comm.Gatherv(output,[outputArray,split_sizes_output,displacements_output,MPI.DOUBLE], root=0) #Gather output data together


if rank == 0:
    outputArray = outputArray[0:len(array1),:]
    print("Final data shape %s" %(outputArray.shape,))

    #plt.clf()
    #plt.imshow(outputArray)
    #plt.title("Combined array")
    #plt.colorbar()
    #plt.savefig('./resultado.png')
    print(outputArray)

