import math

n, a, b, c, d = map(int, input().split())

x = math.ceil(n / a)
y = math.ceil(n / c)

print(min(x*b, y*d))