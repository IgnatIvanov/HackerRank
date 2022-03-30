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
    
    list_grid = []
    for x in range(len(grid)):
        new_line = []
        for y in range(len(grid[x])):
            new_line.append(0)
        list_grid.append(new_line)
            
    
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '.':                        
                list_grid[x][y] = -1
            elif grid[x][y] == 'O':                        
                list_grid[x][y] = 3
                
    for i in range(1, n + 1):
        for x in range(len(list_grid)):  ## Timer count
            for y in range(len(list_grid[x])):
                list_grid[x][y] -= 1 
        
        
        for x in range(len(list_grid)):  ## Bombs detonation
            for y in range(len(list_grid[x])):
                if list_grid[x][y] == 0:
                    if x != 0: 
                        if list_grid[x - 1][y] != 0:
                            list_grid[x - 1][y] = -1
                    if x != len(list_grid) - 1:
                        if list_grid[x + 1][y] != 0:
                            list_grid[x + 1][y] = -1
                    if y != 0: 
                        if list_grid[x][y - 1] != 0:
                            list_grid[x][y - 1] = -1
                    if y != len(list_grid[x]) - 1:
                        if list_grid[x][y + 1] != 0:
                            list_grid[x][y + 1] = -1
                            
        if i % 2 == 0:  #Bomberman is planting bombs
            for x in range(len(list_grid)):
                for y in range(len(list_grid[x])):
                    if list_grid[x][y] <= 0:
                        list_grid[x][y] = 3
        
        if i == n:
            break
        if i % 4 == (n % 4) + 0:
            if i != 1:
                break   
      
    result = []  
    for x in range(len(grid)):
        new_line = str()
        for y in range(len(grid[x])):
            if list_grid[x][y] <= 0:
                new_line += '.'
            elif list_grid[x][y] > 0:
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
