#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix)
    max_sum = 0
    for x in range(len(matrix) // 2):
        for y in range(len(matrix)  // 2):
            top_left = matrix[x][y]
            top_right = matrix[x][n - y - 1]
            bot_left = matrix[n - x - 1][y]
            bot_right = matrix[n - x - 1][n - y - 1]
            max_sum += max(top_left, top_right, bot_left, bot_right)
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
