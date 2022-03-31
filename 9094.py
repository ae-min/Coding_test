from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n,m = map(int, stdin.readline().split())
    cnt = 0
    for a in range(1, n-1): #0<a<b<n이므로 a는 1부터 n-1까지 (n-1은 포함안되므로 사실상 n-2까지)
        for b in range(a+1, n): # b는 a보다 크므로 a+1부터 n까지 (n은 포함안되므로 사실상 n-1까지)
            if (a**2+b**2+m) % (a*b) == 0: #정수임을 판단하는 기준은, 분자를 분모로 나누었을 때 나머지가 0인 순서쌍으로 함
                cnt += 1
    print(cnt)

#stdin을 사용해도 python3는 시간초과 발생하여 pypy3로 제출