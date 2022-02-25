n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    even = []
    
    for i in li: 
        if i % 2 == 0:
            even.append(i)

    print(sum(even), min(even))