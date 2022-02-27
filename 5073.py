while True:
    li = list(map(int, input().split()))
  
    if li[0]==0 and li[1]==0 and li[2]==0:
        break
    if li[0]==li[1]==li[2]:
        print('Equilateral')
    elif sum(li)-max(li) <= max(li):
        print('Invalid')
    elif li[0]!=li[1] and li[1]!=li[2] and li[0]!=li[2]:
        print('Scalene')
    else: 
        print('Isosceles')