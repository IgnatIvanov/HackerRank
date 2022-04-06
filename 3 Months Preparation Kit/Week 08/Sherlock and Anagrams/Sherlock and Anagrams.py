#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    anagrams_dict = dict()
    count = 0
    
    for l in range(1, len(s)):
        for i in range(0, len(s) - l + 1):
            current_list = s[i:i + l] 
            current_list = sorted(current_list)
            current = ''
            for i in range(len(current_list)):
                current += current_list[i]
            anagrams_dict.setdefault(current, 0)
            anagrams_dict[current] += 1
        
        for k in anagrams_dict.values():
            count += k * (k - 1) // 2
        
        print(anagrams_dict)
        anagrams_dict = dict()
                
    return round(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
