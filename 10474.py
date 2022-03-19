while True:
    a, b = map(int, input().split())
    
    if a==0 and b==0:
        break
        
    x = a//b
    y = a%b

    print(x, y,end=" / ")
    print(b)