total = []
for i in range(7):
    num = int(input())
    
    if num % 2 == 1:
        total.append(num)

if len(total) == 0:
    print(-1)
else :    
    print(sum(total))
    print(min(total))