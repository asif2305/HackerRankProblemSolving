#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a, b, n):
    if n==1:
        return b
    else:
        f0=a
        f1=b
       # f2=f1+f0
        for i in range(n-1):
            f2=f0+f1
            f0=f1
            f1=f2
    return f2 % 1000000007


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abn = input().split()

        a = int(abn[0])

        b = int(abn[1])

        n = int(abn[2])

        result = solve(a, b, n)

        #fptr.write(str(result) + '\n')
        print(result)
    #fptr.close()
