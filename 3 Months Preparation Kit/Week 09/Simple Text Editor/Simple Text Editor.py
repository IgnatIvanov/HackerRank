# Enter your code here. Read input from STDIN. Print output to STDOUT
s = ''
result_stack = []

for i in range(int(input())):
    op = str(input()).split(' ')
    if op[0] == '1':
        result_stack.append(s)
        s += op[1]
    elif op[0] == '2':
        result_stack.append(s)
        s = s[:-int(op[1])]        
    elif op[0] == '3':
        print(s[int(op[1]) - 1])
    elif op[0] == '4':
        s = result_stack.pop()
        