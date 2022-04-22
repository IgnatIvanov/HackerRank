# Enter your code here. Read input from STDIN. Print output to STDOUT
heap = []
min_heap = 2000000000
for q in range(int(input())):
    command = str(input()).split(' ')
    if command[0] == '1':
        v = int(command[1])
        heap.append(v)
        if v < min_heap:
            min_heap = v
    elif command[0] == '2':
        v = int(command[1])
        heap.remove(v)
        if min_heap == v:
            if len(heap) == 0:
                min_heap = 2000000000
            else:
                min_heap = min(heap)
    elif command[0] == '3':
       print(min_heap) 