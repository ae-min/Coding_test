a,b,c,x,y = map(int, input().split())
cost = 0
cost1 = 0
i = (x*a)+(y*b)

if x<y:
    cc = (c*2)*x
    cost = (b*(y-x))+cc
    cost1 = (c*2)*(y-x)+cc
elif x>y :
    cc = (c*2)*y
    cost = (a*(x-y))+cc
    cost1 = (c*2)*(x-y)+cc
        
print(min(i,cost,cost1))
