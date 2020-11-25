from __future__ import print_function

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())

    i = 1
    for i in range(n):
        print(i+1, end="")
    #print()
