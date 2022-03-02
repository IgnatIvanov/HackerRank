#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    player = 'Richard'
    while n > 1:
        to_take = 1
        while True:
            if to_take * 2 >= n:
                break
            to_take *= 2
            
        n -= to_take
        if player == 'Louise':
            player = 'Richard'
        else:
            player = 'Louise'
    return player
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
