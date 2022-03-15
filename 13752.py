n = int(input())

for i in range(n):
    k = int(input())

    for i in range(k):
        print("=",end='')
    print(sep='\n')  

# 아래 코드도 정답
# for _ in range(int(input())):
#     print('=' * int(input()))