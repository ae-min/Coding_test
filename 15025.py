a, b = map(int, input().split())

if a!=0 and b!=0 and a==b:
    print('Even', a+b)
elif a!=b:
    print('Odd', max(a,b)*2)
elif a==0 and b==0:
    print('Not a moose')