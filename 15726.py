a, b, c = map(int, input().split())

x = a*b/c
y = a/b*c

print(int(max(x, y)))