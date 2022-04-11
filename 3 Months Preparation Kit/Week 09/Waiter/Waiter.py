#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    answer = []
    
    n = max(number)
    sieve = list(range(n + 1))
    sieve[1] = 0  
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    i = 0
    while True:
        if i == len(sieve):
            break
        if sieve[i] == 0:
            sieve.pop(i)
        else:
            i += 1
            
    while True:
        if len(sieve) <= q:
            break
        else:
            sieve.pop()
            
    for val in sieve:
        A = []
        for i in range(len(number)):
            A.append(number.pop())
        B = []    
        
        i = 0
        while True:
        #for i in range(len(A)):
            if i == len(A):
                break
            if A[i] % val == 0:
                B.append(A.pop(i))
            else:
                i += 1
                
        for i in range(len(B)):
            answer.append(B.pop())
            
        if len(A) == 0:
            break
        else:
            for i in range(len(A)):
                number.append(A.pop(0))
        
    if len(number) > 0:
        for i in range(len(number)):
            answer.append(number.pop())
    
    #print(number)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
