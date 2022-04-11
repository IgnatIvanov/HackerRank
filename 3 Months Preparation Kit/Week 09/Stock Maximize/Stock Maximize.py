#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    bought = []
    max_future = []
    for i in range(len(prices)):
        max_future.append(0)
    max_future[-1] = prices[-1]
    for i in range(len(prices) - 2, -1, -1):
        max_future[i] = prices[i]
        if max_future[i + 1] > max_future[i]:
            max_future[i] = max_future[i + 1]
    profit = 0
    for i in range(len(prices)):
        delta = max_future[i] - prices[i]
        if delta > 0:
            profit += delta
    
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
