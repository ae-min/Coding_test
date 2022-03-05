t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    total = 0
    for j in li:
        total += j // k

    print(total)