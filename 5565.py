n = 10
b = []

for i in range(n):
    b.append(int(input()))

x = sum(b)-b[0]
print(abs(x-b[0]))

'''
total = int(input())

for i in range(9):
	total -= int(input())
print(total)

이렇게 간단한 문제를.. 너무 복잡하게 풀었구나..
'''