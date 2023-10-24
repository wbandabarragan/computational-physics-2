#!/usr/bin/env python3

# Importing libraries
import numpy as np
from mpi4py import MPI

# Call main to execute the script

if __name__ == "__main__":

   # Define a vector size
   N = 10000000

   # Initialise the first vector
   a = np.ones(N)

   # Initialise the second vector
   b = np.zeros(N)

   # Add values to b
   for i in range(N):
       b[i] = 1.0 + i

   # Add the two arrays
   for i in range(N):
       a[i] = a[i] + b[i]

   # Average of the result
   summ = 0.0

   # For loop
   for i in range(N):
       summ += a[i]
   average = summ/N 

   # Print result
   print("Average is: ", str(average))

