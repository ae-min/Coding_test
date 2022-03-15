n = int(input())
count = 0
li = list(map(int, input().split()))

for i in range(n):
    if li[i] != i+1:
        count += 1

print(count)