n = int(input())
x = n // 3
result = (x - 1) * (x - 2) // 2     # 1 + 2 + 3 + 4 + ... + (n - 2) 더한 값
print(result)