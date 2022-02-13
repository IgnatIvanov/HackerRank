# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for x in range(T):    
    S = str(input())
    even = ''
    odd = ''
    for i in range(len(S)):
        if i % 2 == 1:
            even += S[i]
        else:
            odd += S[i]
    print(odd, even)