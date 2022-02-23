t = int(input())

for _ in range(t):
    num = int(input())
    
    q = num // 25
    num = num - 25*q
    
    d = num // 10
    num  = num  - 10*d
    
    n = num // 5
    num  = num  - 5*n
    
    p = num //1

    print(q,d,n,p)