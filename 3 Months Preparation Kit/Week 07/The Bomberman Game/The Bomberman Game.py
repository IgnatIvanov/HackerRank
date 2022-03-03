#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 0:
        return grid
    time_line = [[] for i in range(5)]
    
    for i in range(5):
        if i == 0:
            new_grid = []
            for x in range(len(grid)):
                new_line =[]
                for y in range(len(grid[x])):
                    if grid[x][y] == '.':                        
                        new_line.append(-1)
                    elif grid[x][y] == 'O':                        
                        new_line.append(3)
                new_grid.append(new_line)
            time_line[i] = new_grid
            continue
        
        time_line[i] = time_line[i - 1]
        for x in range(len(time_line[i])):
            for y in range(len(time_line[i][x])):
                time_line[i][x][y] -= 1
                
        for x in range(len(time_line[i])):
            for y in range(len(time_line[i][x])):
                if time_line[i][x][y] == 0:
                    if x != 0: 
                        if time_line[i][x - 1][y] != 0:
                            time_line[i][x - 1][y] = -1
                    if x != len(time_line[i]) - 1:
                        if time_line[i][x + 1][y] != 0:
                            time_line[i][x + 1][y] = -1
                    if y != 0: 
                        if time_line[i][x][y - 1] != 0:
                            time_line[i][x][y - 1] = -1
                    if y != len(time_line[i]) - 1:
                        if time_line[i][x][y + 1] != 0:
                            time_line[i][x][y + 1] = -1                                
            
        if i % 2 == 0:  #Bomberman is planting bombs
            for x in range(len(time_line[i])):
                for y in range(len(time_line[i][x])):
                    if time_line[i][x][y] <= 0:
                        time_line[i][x][y] = 3
                        
    time_line[0] = time_line[4]
    return [str(time_line[(n % 4)][x]) for x in range(len(time_line[(n % 4)]))]
    res_grid = time_line[n % 4]
    result = []
    for x in range(len(res_grid)):
        new_line = ''
        for y in range(len(res_grid[x])):
            if res_grid[x][y] <= 0:
                new_line += '.'
            elif res_grid[x][y] > 0:
                new_line += 'O'
        result.append(new_line)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
