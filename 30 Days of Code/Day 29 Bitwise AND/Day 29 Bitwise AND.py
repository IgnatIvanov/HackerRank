#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    return K-1 if ((K-1) | K) <= N else K-2
    
    max_and = 0
    S = range(1, N + 1)
    for x in range(len(S)):
        for y in range(x, len(S)):
            if x == y:
                continue
            cur_and = S[x] & S[y]
            if cur_and > 0 and cur_and < K and cur_and > max_and:
                max_and = cur_and
                
    return max_and

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
