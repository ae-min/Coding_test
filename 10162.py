t = int(input())

if t%10 !=0:
     print(-1)
elif t < 300:
    a = t//60
    b = t%60
    c = b//10
    print(0, a, c)
elif t>=300:
    a = t//300
    b = t%300
    c = b//60
    d = b%60
    e = d//10
    print(a, c, e)