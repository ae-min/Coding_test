a = list(map(int, input().split()))

if a.count(1) >= 2:
    print(1)
elif a.count(2) >= 2:
    print(2)