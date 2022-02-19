n  = int(input())
call = list(map(int, input().split()))
y=m=0

for i in call:
    y += (i//30)*10+10
    m += (i//60)*15+15
if y==m:
    print("Y M",m)
elif y>m:
    print("M",m)
else:
    print("Y", y)