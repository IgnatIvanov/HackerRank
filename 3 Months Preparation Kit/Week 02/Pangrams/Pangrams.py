#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    str_dict = dict.fromkeys([letter for letter in s.lower()])
    if len(str_dict) == 27:
        return 'pangram'
    if len(str_dict) == 26:
        if ' ' not in str_dict.keys():
            return 'pangram'
    return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
