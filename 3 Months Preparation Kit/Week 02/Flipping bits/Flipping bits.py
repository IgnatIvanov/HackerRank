#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    bin_int = [x*0 for x in range(32)]
    res = 0
    bin_n = bin(n)
    bin_n_32 = '0' * (32 - len(bin(n)) + 2) + bin_n[2:]
    for i in reversed(range(32)):
        if bin_n_32[i] == '0':
            res += (2 ** (31 - i))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
