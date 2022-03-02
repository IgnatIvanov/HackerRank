#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    str_dict = dict()
    for letter in s:
        str_dict.setdefault(letter, 0)
        str_dict[letter] += 1
    
    values = []
    for value in str_dict.values():
        values.append(value)
    
    if min(values) == max(values):
        return 'YES'
    else:
        if min(values) == 1 and values.count(1) == 1:
            if values.count(max(values)) == len(values) - 1:
                return 'YES'
        for i in range(len(values)):
            if values[i] == max(values):
                values[i] -= 1
                break
        if min(values) == max(values):
            return 'YES'
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
