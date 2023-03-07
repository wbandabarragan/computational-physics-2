#!/usr/bin/env python3

import numpy as np

def random_generator(seed):

    # Allocate seed
    np.random.seed(seed)

    # Generate random number
    random_num = np.random.randint(0, 10)

    # Return square of the number
    return random_num**2

