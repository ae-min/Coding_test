T = int(input())

for i in range(T):
    n, c = map(int, input().split())
    
    if n%c != 0:
        total = (n//c)+1
    else: 
        total = n//c

    print(total)