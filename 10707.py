a = int(input()) #x사의 1리터당 요금
b = int(input()) #y사 기본요금
c = int(input()) #y사 기본요금이 되는 상한
d = int(input()) #y사 1리터 당 추가요금
p = int(input()) #집에서 사용하는 한달간 수도 양

x = p * a

if c>=p: 
    print(min(x, b))
else: 
    print(min(x, b+((p-c)*d)))
