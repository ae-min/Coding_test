n = int(input())
li = []

for _ in range(n):
    s = input()
    li.append(s[0])
    # 선수들 이름을 입력받고, 이름 맨 첫글자 s[0]만 li라는 리스트에 저장
    
li2 = set(li) 
# set자료형으로 만들면 자동으로 중복이 제거됨. 중복된 이름 제거를 위해 li라는 이름의 set자료형으로 만듬
result = []

for i in li2: # 중복이 배제된 li2리스트에 들은 데이터들을 하나씩 불러옴
    if li.count(i)>=5:
        # 이름의 첫글자가 불러온 데이터 값과 동일한 사람이 5명 이상이라면
        result.append(i) # 결과 리스트에 그 이름 첫글자를 저장

if len(result)>0:
    print(''.join(sorted(result)))
    # join은 개별적인 리스트 값들을 다 붙여줌
    # 사전순으로 쓰라고 했으니 sorted 정렬 
else:
    print("PREDAJA")
    