n = int(input())
x = int(str(n), 2)
x *= 17
print(bin(x)[2:])

#앞에 ob이런 것들은 제거하기 위해서 시작지점을 [2:]으로 지정해줌