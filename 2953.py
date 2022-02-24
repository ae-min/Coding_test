li = []
max = max_i = 0
for i in range(5):
    li = list(map(int, input().split()))
    
    if sum(li)>max:
        max = sum(li)
        max_i = i
        
print(max_i+1, max)