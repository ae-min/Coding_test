while True:
    n = list(map(int, input().split()))
    leaf = 1
    if n[0] == 0:
        break
    for i in range(1, len(n), 2):
        leaf = leaf*n[i]-n[i+1]
    print(leaf)

# leaf = leaf*n[i]-n[i+1] 풀이 방법은 생각해냈으나, 2단계씩 건너뛰는 것을 생각하지 못해 어려움이 있었음