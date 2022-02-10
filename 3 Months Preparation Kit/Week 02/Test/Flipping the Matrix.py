

matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
import numpy as np
half = len(matrix) // 2

for x in range(len(matrix) // 2, len(matrix)):
    if sum(matrix[x][:half]) > sum(matrix[x][half:]):
        line = []
        for y in range(len(matrix)):
            line.append(matrix[x][y])
        for y in range(len(matrix)):
            matrix[x][y] = line[len(line) - y - 1]

matrix = np.transpose(matrix)

for x in range(len(matrix) // 2, len(matrix)):
    if sum(matrix[x][:half]) < sum(matrix[x][half:]):
        line = []
        for y in range(len(matrix)):
            line.append(matrix[x][y])
        for y in range(len(matrix)):
            matrix[x][y] = line[len(line) - y - 1]  
            
matrix = np.transpose(matrix)

for x in range(len(matrix) // 2):
    if sum(matrix[x][:half]) < sum(matrix[x][half:]):
        line = []
        for y in range(len(matrix)):
            line.append(matrix[x][y])
        for y in range(len(matrix)):
            matrix[x][y] = line[len(line) - y - 1]    
            
matrix = np.transpose(matrix)

for x in range(len(matrix) // 2):
    if sum(matrix[x][:half]) < sum(matrix[x][half:]):
        line = []
        for y in range(len(matrix)):
            line.append(matrix[x][y])
        for y in range(len(matrix)):
            matrix[x][y] = line[len(line) - y - 1]

matrix = np.transpose(matrix)      

sum_n = 0
for x in range(len(matrix) // 2):
    for y in range(len(matrix) // 2):
        sum_n += matrix[x][y]

print(sum_n)
#print(matrix[1][half:])  
#print(matrix)
#matrix = np.transpose(matrix)
#print(matrix)
#matrix = np.transpose(matrix)
#print(matrix)