#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    sorted_sticks = sorted(sticks)
    for i in reversed(range(len(sorted_sticks))):
        if i > 1:
            first_stick = sorted_sticks[i]
            second_stick = sorted_sticks[i - 1]
            third_stick = 0
            third_boarder = max(first_stick, second_stick) - min(first_stick, second_stick) 
            #if third_boarder >= max(sorted_sticks[:i - 1]):
                #return [-2]
            for x in reversed(range(i - 1)):
                if sorted_sticks[x] >= third_boarder:
                    third_stick = sorted_sticks[x]
                    if first_stick + second_stick > third_stick:
                        if second_stick + third_stick > first_stick:
                            if third_stick + first_stick > second_stick:
                                return sorted([first_stick, second_stick, third_stick])
                else:
                    break
        else:
            break    
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
