n, m = map(int, input().split()) 

if m==1 or m==2: #m<=2
    print('NEWBIE!')
elif m<=n and m>2:
    print('OLDBIE!')
else: 
    print('TLE!')