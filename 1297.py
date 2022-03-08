# 입력============================
# 첫째 줄에 TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W이 
# 공백 한 칸을 사이에 두고 주어진다.
# 출력============================
# 첫째 줄에 TV의 높이와 TV의 너비를 공백 한 칸을 이용해서 구분지은 후 출력한다. 
# 만약,소수점이 나올 경우에는 그 수보다 작으면서 가장 큰 정수로 출력(즉 소수점 떼기!!)

# 피타고라스 정리를 이용해보자!!
# a^2+b^2=c^2

d,h,w=map(int,input().split())

# d**2 = (h*x)**2 + (w*x)**2의 식을 정리하면
x = (d**2 / (h**2 + w**2)) **0.5

# 출력은 높이 h*x와 너비 w*x를 정수로!

print(int(h*x), end=" ") #공백 한칸으로 구분
print(int(w*x))