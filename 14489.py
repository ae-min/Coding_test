a, b = map(int, input().split())
c = int(input())

s = a+b

if s>=c*2:
    print(s-(c*2))
else:
    print(s)