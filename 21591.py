a, b, c, d = map(int, input().split())
#a너비 b높이 > c스티커너비 d스티커높이
#맞으면 1 / 안맞으면 0
#사방이 1센치의 공간이 있어야 맞는 값이 되므로, 상하 2, 좌우2가 필요하므로 2보다 커야함

if a-c >=2 and b-d >=2:
    print('1')
else: print('0')
