#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    i = 0
    position = []
    while True:
        if len(ranked) == 1:
            break
        if ranked[i] == ranked[i + 1]:
            ranked.pop(i)
            i -= 1
        else:
            i += 1
        if i == len(ranked) - 1:
            break
    
    r = len(ranked) - 1
    p = 0
    while p < len(player):
        if ranked[r] > player[p]:
            position.append(r + 2)
            p += 1
        elif ranked[r] == player[p]:
            position.append(r + 1)
            p += 1
        else:
            if r == 0:
                while p < len(player):
                    position.append(1)
                    p += 1
                return position
            else:
                r -= 1
                
    return position

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
