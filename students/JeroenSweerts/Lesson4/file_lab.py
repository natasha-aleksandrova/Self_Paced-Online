#!/usr/bin/env python3
"""Write a program which prints the full path for all files in the current directory, one per line"""
import os
import pathlib

cwd = os.getcwd()
pth = pathlib.Path(cwd)
for f in pth.iterdir():
    print(f)

"""Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command). """
