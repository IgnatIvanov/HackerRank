#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    values = []
    u = ''
    
    for i in range(len(s)):
        u += s[i]
        score = (ord(u[0]) - ord('a') + 1) * len(u)
        values.append(score)
        if i == len(s) - 1:
            break
        if s[i] != s[i + 1]:
            u = ''
    
    values = set(values)
    
    return ['Yes' if q in values else 'No' for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

    