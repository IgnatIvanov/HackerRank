#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    len_s = len(s) - 2
    left = 0
    right = len(s) - 1
    s_l = [i for i in s]
    s_r = []
    if s_l == [s_l[i] for i in range(right, -1, -1)]:
        return -1
            
    while True:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            s_l.pop(left)
            if s_l == [s_l[i] for i in range(len_s, -1, -1)]:
                return left
            s_r = [i for i in s]
            s_r.pop(right)
            if s_r == [s_r[i] for i in range(len_s, -1, -1)]:
                return right
            else:
                return -1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
