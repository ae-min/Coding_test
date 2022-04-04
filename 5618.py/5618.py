import sys


# 두 수의 공약수는 두 수의 최대공약수의 약수
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))  # 두 수 혹은 세 수 입력받음
g = gcd(num[0], gcd(num[1], num[-1]))               # 두 수 혹은 세 수의 최대공약수
for i in range(1, g // 2 + 1):                      # 1부터 최대공약수의 절반만큼만 확인해도됨. 그치만 굳이 2로 안나누고 전체로 조회해도됨
    if g % i == 0:                                  # 최대공약수를 나누어 떨어지게 하면 약수
        print(i)
print(g)                                            # 최대공약수 자신도 출력