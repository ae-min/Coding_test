s = [0]*3
for i in range(3):
    s[i] = int(input())
    
total = sum(s)

if s[0]==60 and s[1]==60 and s[2]==60:
    print('Equilateral')
elif total==180 and (s[0]==s[1] or s[1]==s[2] or s[0]==s[2]):
    print('Isosceles')
elif total==180 and (s[0]!=s[1] or s[1]!=s[2] or s[0]!=s[2]):
    print('Scalene')
elif total!=180:
    print('Error')