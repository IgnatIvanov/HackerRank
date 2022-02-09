#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    main_sum = 0
    sec_sum = 0
    for i in range(len(arr)):
        main_sum += arr[i][i]
    for i in range(len(arr)):
        x = len(arr) - 1 - i
        sec_sum += arr[i][x]
    return max(main_sum, sec_sum) - min(main_sum, sec_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
