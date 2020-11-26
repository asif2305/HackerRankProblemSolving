from __future__ import division

from pip._vendor.distlib.compat import raw_input


def average(array):
    # your code goes here
    string=set(array)
    sum=0
    for i,val in enumerate(string):
        sum=sum+val
    return (sum/len(string))

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print (result)