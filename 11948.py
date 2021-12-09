a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

x = (a+b+c+d)-min(a,b,c,d)

print(x+max(e,f))

#a,b,c,d 과목 중 3과목 / e,f 중 1과목을 선택해 최댓값을 출력하는 문제
#a,b,c,d의 합에서 최소과목 1개를 min으로 구해 빼주고, e,f는 두개뿐이므로 그중에 큰 값을 max로 구해 더해줌