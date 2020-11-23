
#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)
        print(l// result * b//result)

        #fptr.write(str(result) + '\n')

   # fptr.close()
