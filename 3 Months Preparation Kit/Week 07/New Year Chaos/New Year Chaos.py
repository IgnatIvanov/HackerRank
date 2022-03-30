#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    total_bribes_count = 0
    bribes_per_person = {}
    last = len(q) - 1
    swaps = True
    while swaps:
        swaps = False
        for i in range(last):
            if q[i] > q[i + 1]:
                
                # add to individual bribes counter
                if q[i] in bribes_per_person:
                    bribes_per_person[q[i]] += 1
                    # check if not too chaotic
                    if bribes_per_person[q[i]] > 2:
                        print("Too chaotic")
                        return
                else:
                    bribes_per_person[q[i]] = 1
                    
                # swap with neighbour ahead
                q[i], q[i + 1] = q[i + 1], q[i]
                total_bribes_count += 1
                swaps = True
                
        last -= 1 # this optmises a bit
        
    print(total_bribes_count)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
