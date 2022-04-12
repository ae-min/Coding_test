s1, s2, s3 = map(int, input().split())
li = []
count_li = []

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            ans = i+j+k
            li.append(ans)
          

        
x = max(li)

for a in range(x+1):
      count_li.append(li.count(a))

print(count_li.index(max(count_li))) #index(x) : 리스트에 x 값이 있으면 x의 위치 값을 반환
