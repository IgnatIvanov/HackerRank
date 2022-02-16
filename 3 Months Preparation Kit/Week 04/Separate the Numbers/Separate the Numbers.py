#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    numbers = []
    current_n = 0
    
    for i in range(1, (len(s) // 2) + 1):
        current_n = int(s[:i])
        line = ''
        while len(line) < len(s):
            line += str(current_n)
            current_n += 1
        if len(line) != len(s):
            continue
        if line == s:
            print('YES ' +  s[:i])
            return
            
    print('NO')

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
 