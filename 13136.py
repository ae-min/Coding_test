r, c, n = map(int, input().split())
a = r//n
b = c//n

if r % n == 0 and c % n == 0:
    print(a*b)
elif r % n != 0 and c % n == 0:
    print((a+1)*b)
elif r % n == 0 and c % n != 0:
    print(a*(b+1))
else: 
    print((a+1)*(b+1))