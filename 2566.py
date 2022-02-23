matrix = []
for _ in range(9):
    matrix.append(list(map(int,input().split())))

x = y = 0
max = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j]>max:
            max = matrix[i][j]
            x = i+1
            y = j+1
print(max)
print(x, y)