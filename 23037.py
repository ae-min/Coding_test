n = int(input())
x = list(map(int, str(n)))
sum = 0
for i in x:
    sum += i**5

print(sum)