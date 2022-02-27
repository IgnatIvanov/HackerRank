#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    for i in range(len(arr) // 2):
        arr[i][1] = '-'
    arr_by_num = []
    for item in arr:
        if int(item[0]) + 1 > len(arr_by_num):
            for i in range(int(item[0]) + 1 - len(arr_by_num)):
                arr_by_num.append([])
        arr_by_num[int(item[0])].append(item[1])
        
    for i in range(len(arr_by_num)):
        for j in range(len(arr_by_num[i])):
            print(arr_by_num[i][j],end=' ')
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
