#!/usr/bin/env python3

# Impot ArgParse
import argparse

# First call
parser = argparse.ArgumentParser(description='Process some integers.')

# Add arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

# CLosing statement
args = parser.parse_args()

# Print
print(args.accumulate(args.integers))
