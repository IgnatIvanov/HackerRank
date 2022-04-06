#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    opened = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            opened.append(s[i])
        else:
            if len(opened) == 0:
                return 'NO'
            last = opened.pop()
            if last == '(' and s[i] != ')':
                return 'NO'
            if last == '[' and s[i] != ']':
                return 'NO'
            if last == '{' and s[i] != '}':
                return 'NO'
            
    
    if len(opened) > 0:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
