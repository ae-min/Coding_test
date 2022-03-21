s1, s2 = map(int,input().split())
score1 = 0
score2 = 0
for i in range(s1):
    a, b = map(int,input().split())
    if a==b:
        score1 += 1
for j in range(s2):
    x, y = map(int, input().split())
    if x==y:
        score2 += 1
        
if score1==s1 and score2==s2:
        print('Accepted')
elif score1==s1 and score2!=s2:
        print('Why Wrong!!!')
elif score1!=s1:
        print('Wrong Answer')