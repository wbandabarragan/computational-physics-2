#!/usr/bin/env python3

import numpy as np

def random_square(seed):
    
    # Allocate seed
    np.random.seed(seed)
    
    # Generate random number    
    random_num = np.random.randint(0, 10)
    
    # Return squared values
    return random_num**2
