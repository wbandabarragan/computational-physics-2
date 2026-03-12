#!/opt/anaconda3/envs/py39/bin/python
"""
Script to generate 10 million random numbers.
"""
# Import modules
import numpy as np

# Random number function
def matrix_op(seed):
    """
    Square a random number generated witn an input seed.
    """
    # Allocate seed
    np.random.seed(seed)

    # Set a matrix size -> square matrices
    n_matrix = 20

    # Create the matrices
    matrix_a = np.random.rand(n_matrix, n_matrix)
    matrix_b = np.random.rand(n_matrix, n_matrix)
    
    # Matrix multiplication
    result = matrix_a @ matrix_b
    # result = np.dot(matrix_a, matrix_b)

    # Return squared values
    return np.mean(result)
