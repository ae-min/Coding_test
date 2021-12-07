import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
k = math.ceil(A / C)
m = math.ceil(B / D)
free = max(k, m)
print(L - free)

'''
math 모듈의 ceil함수를 이용해 나눗셈이 딱 떨어지지 않을경우 올림 가능
''' 

