#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    # Write your code here
    totalSwaps = 0
    for i in range(2 * n):
        numberOfSwaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swap = a[j]
                a[j] = a[j + 1]
                a[j + 1] = swap
                numberOfSwaps += 1
        totalSwaps += numberOfSwaps
                
        if numberOfSwaps == 0:
            print('Array is sorted in', totalSwaps, 'swaps.')
            print('First Element:', a[0])
            print('Last Element:', a[-1])
            break