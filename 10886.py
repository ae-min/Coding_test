n = int(input())
yes=no=0
for i in range(n):
    x = int(input())
    if x==1:
        yes += 1
    elif x==0:
        no += 1
        
if yes>no:
       print('Junhee is cute!')
elif yes<no:
       print('Junhee is not cute!')