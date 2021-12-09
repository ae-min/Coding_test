a = list(map(int, input().split())) #4명의 팀원의 스킬레벨
a.sort()

x = a[0]+a[3]
y = a[1]+a[2]

#오름차순 정렬 후, 가장 작은 수와 가장 큰수 더하기
#두번째로 작은 수와 두번째로 큰수 더하기
#두 그룹의 차이 출력

if x>y:
    print(x-y)
else:
    print(y-x)