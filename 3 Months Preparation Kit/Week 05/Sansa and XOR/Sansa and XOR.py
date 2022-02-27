#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
    ans = 0
    if len(arr) % 2 == 0:
        return 0
    else:
        for i in range(0, len(arr), 2):
            ans = ans ^ arr[i];
        
    return ans;
    
    
    answer = 0
    for l in range(1, len(arr) + 1):
        for start_p in range(len(arr) - l + 1):
            if start_p == 0:
                if l == 1:
                    answer = arr[start_p]
                    continue
            sub_arr = arr[start_p:start_p + l]
            #print(sub_arr)
            if l == 1:
                answer = answer ^ arr[start_p]
            else:
                sub_ans = sub_arr[0]
                for i in range(1, len(sub_arr)):
                    sub_ans = sub_ans ^ sub_arr[i]
                answer = answer ^ sub_ans
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
