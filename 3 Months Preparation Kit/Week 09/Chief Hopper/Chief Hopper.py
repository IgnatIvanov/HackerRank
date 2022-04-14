#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    minE = 0
    for i in range(len(arr) - 2, -1, -1):
        minE = (minE + arr[i + 1]) / 2
        minE = math.ceil(minE)
                
    return math.ceil((minE + arr[0]) / 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
