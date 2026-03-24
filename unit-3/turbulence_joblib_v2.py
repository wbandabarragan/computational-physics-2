# Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
import time
from joblib import Parallel, delayed
import pandas as pd

# I/O function
def io_turbulence(fname):
    """

    """
    # Split the name to get the numbers only
    n_fname = os.path.basename(fname).split(".")[1]

    # Get the data into a mesh
    mesh = pv.read(fname)

    # Get data arrays in code units
    rho = pv.get_array(mesh, "rho", preference = 'cell')

    # Reshape the density array into a 2D array
    rho_2d = rho.reshape(mesh.dimensions[0] - 1, mesh.dimensions[1] - 1)

    # Add the mesh
    # Create coordinate vectors:
    x = np.linspace(mesh.bounds[0], mesh.bounds[1], mesh.dimensions[1] - 1)
    y = np.linspace(mesh.bounds[2], mesh.bounds[3], mesh.dimensions[0] - 1)

    # Generate Grid
    x_2d, y_2d = np.meshgrid(x, y)

    # Plotting the density
    plt.figure(figsize=(4,3))

    z_dens = plt.pcolor(x_2d, y_2d, np.log10(rho_2d), cmap = "Blues")#, vmin = -25, vmax=-23)

    plt.colorbar(z_dens)

    plt.savefig(f"./img_turb/dens_{n_fname}.jpg")

    plt.close()

# Execution line
if __name__ == "__main__":

    # For testing
    #FILE_NAME = "data.0000.vtk"

    # Function Call 
    #io_turbulence("./TURB_DRIVE_SUP_hr/" + FILE_NAME)

    # Start time stamp
    #start = time.time()

    # Number of cores
    n_list = [1, 2, 4, 5, 10]
    e_list = []

    # File name -> File list
    b_path = "./TURB_DRIVE_SUP_hr/"

    for k in n_list:
        #print(k)
        # Adapt filenames
        file_list = [os.path.join(b_path + f"data.0{j:03d}.vtk") for j in range(100)]
        #print(file_list)
    
        # Start time stamp
        start = time.time()

        # Perform the parallelisation
        results = Parallel(n_jobs = k, batch_size = 100//k, backend = "multiprocessing")(delayed(io_turbulence)(i) for i in file_list)

        # Start time stamp
        end = time.time()
        
        exec_time = np.round(end - start, 4)

        e_list.append(exec_time)
        
        # Print the execution time
        print("The parallel execution time in seconds is: ", exec_time)

    #print(e_list)
    # Switch to arrays -> dataframes


    # Writing a new data frame

    df = pd.DataFrame({"n_cores": np.array(n_list), "e_times": np.array(e_list)})

    # Output a new post-processed file
    df.to_csv("./scaling.csv", ",", float_format = "{:.2e}".format, index = None)

