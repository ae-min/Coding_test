n = int(input())

while True:
    x = int(input())
    
    if x==0:
        break
    if x % n == 0:
        print('{0} is a multiple of {1}.'.format(x,n))
    else :
        print('{0} is NOT a multiple of {1}.'.format(x,n))