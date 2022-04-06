
# Enter your code here. Read input from STDIN. Print output to STDOUT
queue = []

for i in range(int(input())):
    command = [int(x) for x in input().split(' ')]
    if command[0] == 1:
        queue.append(command[1])
    elif command[0] == 2:
        queue.pop(0)
    elif command[0] == 3:
        print(queue[0])