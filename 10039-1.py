score=[]

for i in range(5):
    score.append(int(input()))
    if score[i]<40:
           score[i] = 40

print(sum(score)/5)

#정답은 나오지만 정답처리 안됨. if score[i]<40: 이 부분이 에러라고 하는데 잘 모르겠음.
