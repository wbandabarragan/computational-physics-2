#!/usr/bin/env python

# Importing the sys library
import sys

# Get the PATHs from the user and allocate them into python objects
inputfolder  = sys.argv[1]
outputfolder = sys.argv[2]
ics_position = sys.argv[3]

# Safe check
print('Input folder is: ' + inputfolder, 'Output folder is: ' + outputfolder)

print('The initial position is: ' + ics_position)

# Live input
print('Now provide the initial velocity please:')

ics_velocity = input()

ics_velocity_v = float(ics_velocity)

print('Thanks, the velocity provided is: ' + ics_velocity)

print(ics_velocity_v)
