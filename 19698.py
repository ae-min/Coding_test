n, w, h, l = map(int, input().split())
x = (w//l)*(h//l)

if n<x:
    print(n)
else:
    print(x)
