t = int(input())
for _ in range(t):
    d = int(input())
    cnt = 0
    for i in range(101):
        if i*i+i <= d:
            cnt = i
        else:
            break
    print(cnt)