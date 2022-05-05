word = input().upper() #upper()대문자, lower() 소문자
word_list = list(set(word)) #set:중복제거

cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))]) 
    #cnt.index(max(cnt)) : max(cnt)의 인덱스 위치를 구하고
    #word_list에서 그 인덱스 위치의 값을 출력하도록 []이걸로 묶어줌