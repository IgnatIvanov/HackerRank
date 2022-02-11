#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    spotted_amount = []
    for i in range(max(arr) + 1):
        spotted_amount.append(0)
    for bird in arr:
        spotted_amount[bird] += 1
    max_count = 0
    max_bird = 0
    for i in range(len(spotted_amount)):
        if spotted_amount[i] > max_count:
            max_count = spotted_amount[i]
            max_bird = i
    return max_bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
