k = int(input())
d1, d2 = map(int, input().split())

if d1==d2:
    print(k**2)
else:
    b = (max(d1,d2)-min(d1,d2))/2
    # 긴변에서 짧은 변을 빼고 남은 값을 2로 나누는 과정에서 소수점이 나올 수 있으므로 //가 아닌 /사용
    # 높이 a를 구하기 위해서 b제곱을 우측으로 넘김. a제곱=c제곱-b제곱
    a = k**2-b**2
    print(a)

# 피타고라스의 정리 : a제곱+b제곱=c제곱
# a 높이, b 밑변, c 기울어진 변