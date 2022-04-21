#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def proper_pairs(pairs, s_list):
    proper_pairs = []
    
    for pair in pairs:
        to_check = str()
        for l in s_list:
            if l in pair:
                to_check += l
                
        etalon = (to_check[0] + to_check[1]) * (len(to_check) // 2)
        if len(to_check) % 2 == 1:
            etalon += etalon[0]
            
        if to_check == etalon:
            proper_pairs.append(len(to_check))
            
    return proper_pairs


def alternate(s):
    # Write your code here
    s_dict = dict()
    s_list = [l for l in s]
    
    for letter in s:
        s_dict.setdefault(letter, 0)
        s_dict[letter] += 1
        
    pairs = []
    keys = [k for k in s_dict.keys()]
    values = [v for v in s_dict.values()]
    for x in range(len(keys)):
        for y in range(x + 1, len(keys)):
            if values[x] == values[y]:
                new_pair = [keys[x], keys[y]]
                pairs.append(new_pair)
            elif values[x] == values[y] + 1:
                new_pair = [keys[x], keys[y]]
                pairs.append(new_pair)
            elif values[x] == values[y] - 1:
                new_pair = [keys[x], keys[y]]
                pairs.append(new_pair)
            
    pairs = proper_pairs(pairs, s_list)
    pairs.append(0)
    
    return max(pairs)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
