N, M = map(int, input().split())
li = list(map(int, input().split()))
res = 1
for i in li:
    res *= i
print(res%M)