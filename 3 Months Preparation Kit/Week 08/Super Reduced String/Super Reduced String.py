#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    letters_list = [s[x] for x in range(len(s))]
    
    i = 0
    while True:
        if i >= len(letters_list) - 1:
            break
        
        if letters_list[i] == letters_list[i + 1]:
            letters_list.pop(i + 1)
            letters_list.pop(i)
            i = 0
        else:
            i += 1
            
    if len(letters_list) == 0:
        return 'Empty String'
    
    answer = str()
    for i in range(len(letters_list)):
        answer += letters_list[i]
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
