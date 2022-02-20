A = list(map(int, input().split()))
B = list(map(int, input().split()))

history = 'D'
sumA=sumB=0 

for i in range(10):  
    if A[i]>B[i]:
        sumA += 3
        history="A"
    elif A[i]<B[i]:
        sumB += 3
        history="B"
    elif A[i]==B[i]:
        sumA += 1
        sumB += 1
 
print(sumA, sumB)

if sumA>sumB:
    print('A')
elif sumA<sumB:
    print('B')
elif sumA==sumB:
     if history=='A':
       print('A')
     elif  history=='B':
       print('B')
     elif history=='D':
       print('D')


# 비기기 전에 마지막으로 입력되었던 값을 구해내는 부분에서 어려움이 있었음.
# 각 라운드 승패가 결정될 때마다 누가 이겼는지를 history라는 변수에 저장함으로써 구해낼 수 있었음