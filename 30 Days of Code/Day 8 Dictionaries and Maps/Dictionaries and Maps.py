# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = dict()
for i in range(n):
    in_str = str(input()).split(' ')
    phoneBook[in_str[0]] = in_str[1]
    
find_name = str(input())
while find_name != '':
    if find_name in phoneBook:
        print(find_name, '=', phoneBook[find_name], sep='')
    else:
        print('Not found')
    try:
        find_name = str(input())
    except EOFError:
        break