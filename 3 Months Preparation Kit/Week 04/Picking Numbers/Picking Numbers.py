#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    values = []
    
    for i in range(max(a) + 1):
        values.append(0)
        
    for number in a:
        values[number] += 1
        
    sum = 0
    
    for i in range(len(values) - 1):
        if values[i] + values[i + 1] > sum:
            sum = values[i] + values[i + 1]
    
    return sum
        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
