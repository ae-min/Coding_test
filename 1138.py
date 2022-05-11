n = int(input())

arr = list(map(int, input().split()))
answer = [0]*n

for i in range(n):   
    cnt = 0 
    #왼쪽에 몇명이 있는지 확인하기 위해 사용. 1씩증가하며 0명이있니 1명이있니 체크하게 되고, 증가하는 만큼 answer의 위치도 동일하게 증가되므로 결과적으로 해당 인덱스가 위치할 자리를 찾게됨
    for j in range(n):
        if cnt == arr[i] and answer[j] == 0:
            answer[j] = i + 1 #출력은 1부터의 형식인데 인덱스를 읽을 때는 0부터이므로 1을 더해주게됨
            break #break는 하나의 for문만 탈출가능하므로 for j in range만 탈출하는 구조임.
        elif answer[j] == 0:
            cnt += 1
                
print(' '.join(map(str, answer))) #리스트로 입력받은 요소를 하나의 문자열로 출력 : ''.join(리스트)