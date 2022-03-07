n = int(input())

for i in range(n):
    c, v = map(int, input().split())
    
    x = c // v
    y = c % v
    
    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(x,y))