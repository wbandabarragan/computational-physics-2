#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="--input takes a string with the input folder", type=str, default=None)

parser.add_argument("--output", help="--output takes a string with the output folder", type=str, default=None)

args = parser.parse_args()

print("The input folder is: " + args.input)

print("The output folder is: " + args.output)
