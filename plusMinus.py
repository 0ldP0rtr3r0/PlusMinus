#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    for i in range(0,len(arr)):
        if arr[i]>0:
            pos = pos + 1
        elif arr[i]<0:
            neg = neg + 1
        else:
            zero = zero + 1
    print(pos/len(arr))
    print(neg/len(arr))
    print (zero/len(arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
