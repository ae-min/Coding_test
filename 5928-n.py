d, h, m = map(int, input().split())

start = 11 * 24 * 60 + 11 * 60 + 11
total = d * 24 * 60 + h * 60 + m
result = total - start
if result < 0:
    result = -1

print(result)