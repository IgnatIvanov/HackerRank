#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_n = bin(n)[2:]
    ones = []
    
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            if i == 0 or bin_n[i] != '1':
                ones.append(0)
            ones[-1] += 1
        else:
            ones.append(0)
    
    print(max(ones))
