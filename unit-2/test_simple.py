#!/usr/bin/env python3

# Test module
# Funtion 1: defines an operation

def multiply(a, b):
   c = a * b
   return c

# Function 2: test function

def test_multiply():
   """
   Function to test our multiply operation.
   """
   assert multiply(2, 5) == 10


