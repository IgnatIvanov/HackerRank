#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score = scores[0]
    most_breaks = 0
    least_breaks = 0
    for i in range(len(scores)):
        if max_score != max(scores[:i+1]):
            max_score = max(scores[:i+1])
            most_breaks += 1
        elif min_score != min(scores[:i+1]):
            min_score = min(scores[:i+1])
            least_breaks += 1
    
    return [most_breaks, least_breaks]
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
