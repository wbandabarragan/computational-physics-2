#!/usr/bin/env python
# coding: utf-8

# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sint

# Define constants
c_2 = 1 # difussivity constant

# Length of the box/domain
L = 200

# Discretisation of the domain
N = 2000

# Define the step size
h = L/N

# Define x-axis
x = np.arange(-L/2, +L/2, h)

# Time step
t_step = 0.025
t_max = 400.

# Time discretisation:
t = np.arange(0, t_max, t_step)

# Heat equation, FFT method
# $u_t = c^2 u_{xx}$

# Wavenumbers = spatial frequencies:
k_numbers = 2*np.pi*np.fft.fftfreq(len(x), d = h)

# Initial conditions
u_0 = np.zeros(len(x), dtype= complex)

# Replace zeroes with cos(4*pi*x/L), alpha should be 4*pi/L
u_0[int((L / 2 - L / 8)/h):int((L / 2 + L / 8)/h)]  = np.cos(4*np.pi*x[int((L / 2 - L / 8)/h):int((L / 2 + L / 8)/h)]/L)

# Fourier transform
u_0_fourier = np.fft.fft(u_0)
u_0_fourier_conc = np.concatenate((u_0_fourier.real, u_0_fourier.imag))

# Construct ODE (RHS of ODE)
# Function to get RHS

def RHS_ODE(u_0_fourier_conc, t, k_numbers, c_2):    
    u_tilde = u_0_fourier_conc[:N] + (1j)*u_0_fourier_conc[N:]
    rhs_u_tilde = -(c_2**2)*(k_numbers**2)*u_tilde
    rhs_ode = np.concatenate((rhs_u_tilde.real, rhs_u_tilde.imag))
    return rhs_ode

# k ODEs: solution
solution = sint.odeint(RHS_ODE, u_0_fourier_conc, t, args = (k_numbers, c_2))

# Reconstruct Complex solution:
u_solution = solution[:, :N] + (1j)*solution[:, N:]

# Inverse Fourier transform of each u_solution
# For loop with k as index
inv_u_solution = np.zeros(u_solution.shape, dtype = complex)

# We want to parallelise the code from here onwards
for k in range(len(t)):
    inv_u_solution[k, :] = np.fft.ifft(u_solution[k, :])

# Plotting the solution:
# Add colour
R = np.linspace(1, 0, len(t))
B = np.linspace(0, 1, len(t))
G = 0	
	
plt.figure(figsize= (10, 6))
for j in range(len(t)):
	plt.plot(x, inv_u_solution[j, :].real, color = [R[j], G, B[j]])
plt.xlabel("position [m]")
plt.ylabel("temperature [$\degree$ C]")
plt.savefig("serial_output.png")
plt.close()