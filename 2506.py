n = int(input())
q = list(map(int, input().split()))
score = 0
total = 0
for i in range(n):
   if q[i]==0:
       score = 0
   else:
       score = score+1
       total = total+score
    
print(total)