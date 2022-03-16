A, B, C = map(int, input().split())
N = int(input())

tot = 0 
for i in range(N): 
    # N마다 3줄의 입력을 받아야하므로 1번케이스-3줄, 2번케이스-3줄을 위해 이중for문을 돌림
    total = 0
    for j in range(3):
        a, b, c = map(int, input().split())
        total += (A*a)+(B*b)+(C*c)
        
    tot = max(tot, total) 
    # 1번케이스의 total을 tot에 담고, 2번케이스의 total을 1번케이스가 담긴 tot과 비교해서 큰 그룹을 찾음

print(tot)