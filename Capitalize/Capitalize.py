#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
from pip._vendor.distlib.compat import raw_input


def solve(s):
    for x in s[:].split():
        str = s.replace(x, x.capitalize())
    print(str)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)
    print(result.strip())

    #fptr.write(result + '\n')

    #fptr.close()
