#!/usr/bin/env python
# coding: utf-8

# # ODE in Quantum Mechanics (QM)

# ### Example: Quantum mechanics (ordinary differential equations, integrals, plotting):
# 
# Consider a particle of mass $m$ moving in a small space surrounded by impenetrable barriers.
# 

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define piece-wise function
def f(x, a):
    if(0 <= x <= a):
        return 0
    else:
        return 10000

def psi_function(a, n, x, t):
  
    psi_x = np.sqrt(2/a)*np.sin(n*np.pi*x/a)*np.cos(t)

    return psi_x


# In[42]:


a=2


# In[43]:


x = np.arange(0, 2.01, 0.01)


# In[44]:


y1 = psi_function(a, 1, x, 0) # n=1

y2 = psi_function(a, 2, x, 0) # n=2

y3 = psi_function(a, 3, x, 0) # n=3

y4 = psi_function(a, 4, x, 0) # n=4





# **(h)** Now append the wiggle factor, call the above function for different times, and create a movie with $4$ panels showing how the first $4$ stationary states $\Psi(x,t)$ evolve in time. Add a time stamp to the movies.

# In[46]:


for i in np.arange(0,10,0.1):
    
    y1 = psi_function(a, 1, x, i) # n=1
    
    y2 = psi_function(a, 2, x, i) # n=2

    y3 = psi_function(a, 3, x, i) # n=3

    y4 = psi_function(a, 4, x, i) # n=4
    
    fig, ax = plt.subplots(2,2, figsize=(10,6))

    ax[0][0].plot(x, y1,  label = r'$\psi_1$')
    ax[0][1].plot(x, y2,  label = r'$\psi_2$')
    ax[1][0].plot(x, y3,  label = r'$\psi_3$')
    ax[1][1].plot(x, y4,  label = r'$\psi_4$')

    ax[0][0].legend()
    ax[0][1].legend()
    ax[1][0].legend()
    ax[1][1].legend()

    ax[0][0].set_xlim(0,2)
    ax[0][1].set_xlim(0,2)
    ax[1][0].set_xlim(0,2)
    ax[1][1].set_xlim(0,2)

    ax[0][0].set_ylim(-1.5,1.5)
    ax[0][1].set_ylim(-1.5,1.5)
    ax[1][0].set_ylim(-1.5,1.5)
    ax[1][1].set_ylim(-1.5,1.5)

    #plt.show()
    plt.savefig("wave_functions{:03f}.png".format(i))
    plt.close()


# In[1]:


import glob
from PIL import Image


# In[ ]:


images_in = "wave_functions**.png"

gif_image_out = "wave_functions.gif"

imgs = (Image.open(f) for f in sorted(glob.glob(images_in)))

img = next(imgs)

img.save(fp = gif_image_out, format='GIF', append_images=imgs, save_all=True, duration=100, loop=0)

