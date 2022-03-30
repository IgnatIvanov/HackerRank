# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_date = [int(x) for x in input().split(' ')]
due_date = [int(x) for x in input().split(' ')]

if returned_date[2] > due_date[2]:
    print(10000)
elif returned_date[2] < due_date[2]:
    print(0)
elif returned_date[1] > due_date[1]:
    print((returned_date[1] - due_date[1]) * 500)
elif returned_date[1] < due_date[1]:
    print(0)
elif returned_date[0] > due_date[0]:
    print((returned_date[0] - due_date[0]) * 15)
else:
    print(0)
