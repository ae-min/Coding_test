a, b = map(int, input().split())
c, d = map(int, input().split())

print(min(a+d, b+c))
#왼쪽으로 넘기는 것과 오른쪽으로 넘기는 것 중에 작은 수를 답으로 출력