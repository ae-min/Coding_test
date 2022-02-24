a, b = map(int, input().split())
n = int(input())
min = (1000/b)*a
for i in range(n):
    x, y = map(int, input().split())
    
    if (1000/y)*x < min:
        min = (1000/y)*x
        
print(round(min,2))