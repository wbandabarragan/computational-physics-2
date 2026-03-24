#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {

// Setting up MPI
MPI_Init(&argc, &argv);

int world_size, world_rank;

// MPI commands -> MPI syntax
MPI_Comm_size(MPI_COMM_WORLD, &world_size);

MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

// Printing the messages
printf("Hello from rank %d in a world of %d processors.\n", world_rank, world_size);

// Finalise MPI

MPI_Finalize();
return 0;
}
