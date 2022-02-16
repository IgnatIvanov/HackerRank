#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    import string
    e = ''  # Encrypted text
    #_ascii = string.ascii_letters
    while k > 26:
        k -= 26
    
    for letter in s:
        if letter in string.ascii_letters:
            if letter in string.ascii_uppercase:
                for i in range(26):
                    if string.ascii_letters.upper()[i] == letter:
                        e += string.ascii_letters.upper()[i + k]
            else:
                for i in range(26):
                    if string.ascii_letters.lower()[i] == letter:
                        e += string.ascii_letters.lower()[i + k]
        else:
            e += letter
            
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
