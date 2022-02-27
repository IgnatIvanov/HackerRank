#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    if n < 3:
        return 6 - n
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    num_count = 0
    low_count = 0
    upp_count = 0
    spe_count = 0
        
    for letter in password:
        if letter in numbers:
            num_count += 1
        elif letter in lower_case:
            low_count += 1
        elif letter in upper_case:
            upp_count += 1
        elif letter in special_characters:
            spe_count += 1
            
    to_add = 0
    if not num_count:
        to_add += 1
    if not low_count:
        to_add += 1
    if not upp_count:
        to_add += 1
    if not spe_count:
        to_add += 1
    
    return max(to_add, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
