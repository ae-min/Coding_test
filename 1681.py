n, l = map(int, input().split())
cnt = 0
x = 0
while cnt!=n: #배열은 0부터 시작이니까 10개입력받을거면 9까지만 받으면 되므로 10이랑 같아지면 더이상 루프 돌지않음
    x+=1 # 숫지 1부터 하나씩 조건에 대입해봄
    if str(l) in str(x): 
        #ex)숫자를 문자로 변환해서 10이라는 문자에 문자 l이 포함되어있으면 건너뜀
        continue
    cnt+=1 #포함이 안되어있으면 추가 가능, 어차피 제일 큰수를 뽑는거니까 걍 카운트만 올려서 다음 수를 입력받음. 
print(x) 