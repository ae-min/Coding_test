n = int(input())
x = list(map(int, input().split()))

count = 0

for i in range(n):
    if x[i] == count % 3:
        count += 1

print(count)

# 초기 0을 3으로 나누면 그대로 0이고, 하나씩 증가하면 0-1-2 순서대로 되는 걸 생각했어야 함