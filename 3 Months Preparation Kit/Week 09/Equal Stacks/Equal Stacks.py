#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
        return 0
        
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    
    if sum1 == sum2 and sum2 == sum3:
        return sum1
        
    while True:
        if sum1 > sum2:
            sum1 -= h1.pop(0)
        elif sum1 < sum2:
            sum2 -= h2.pop(0)
        else:
            if sum2 > sum3:
                sum2 -= h2.pop(0)
            elif sum2 < sum3:
                while True:
                    sum3 -= h3.pop(0)
                    if sum2 > sum3:
                        break
                    elif sum2 == sum3:
                        return sum3
            else:
                return sum3
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
