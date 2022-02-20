count = []
result = 0

for i in range(4):
    a, b = map(int, input().split())
    result = result - a + b
    count.append(result)
    
print(max(count))
