#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    variations = [h]
    answer = 0
    while len(variations) > 0:
        cur = variations.pop(0)
        if len(cur) == 0:
            continue
        area = min(cur) * len(cur)
        if answer < area:
            answer = area
        
        #spliting current map by min height
        min_h = min(cur)
        new_map = []
        if len(cur) == 1:
            continue
        for h in cur:
            if h == min_h:
                variations.append(new_map)
                new_map = []
            else:
                new_map.append(h)
        if len(new_map) > 0:
            variations.append(new_map)
                
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
