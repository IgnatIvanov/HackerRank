#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    answer = -100

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    for x in range(len(arr) - 2):
        for y in range(len(arr) - 2):
            #hsum = arr[x][y] + arr[x + 1][y] + arr[x + 2][y]
            #hsum += arr[x + 1][y + 1]
            #hsum += arr[x][y + 2] + arr[x + 1][y + 2] + arr[x + 2][y + 2]
            hsum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2]
            hsum += arr[x + 1][y + 1]
            hsum += arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2]
            if hsum > answer:
                answer = hsum
    print(answer)
