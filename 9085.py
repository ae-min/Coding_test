t = int(input())

for i in range(t):
    total = 0
    n = int(input())
    x = list(map(int, input().split()))
    
    total = sum(x)
    
    print(total)
       