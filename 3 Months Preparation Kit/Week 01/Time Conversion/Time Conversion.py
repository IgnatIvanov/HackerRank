#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh = int(s[0] + s[1])
    if s[-2] == 'P':
        if hh != 12:
            hh += 12
    else:
        if hh == 12:
            hh = 0
    
    if hh < 10:
        return '0' + str(hh) + s[2:-2]
    else:
        return str(hh) + s[2:-2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
