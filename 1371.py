import sys

sentence = sys.stdin.read()
# sys.stdin.readline()은 줄바꿈\n이 같이 입력되기 때문에
# 반복문으로 여러줄의 문자열을 입력받기 위해서는
# sys.stdin.read()사용

alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in alphabet:
    result.append(sentence.count(i)) 
    #알파벳이라는 변수내의 문자들별로 빈도수를 카운트 후 result라는 리스트에 추가

m = max(result) # 가장 높은 빈도수를 가진 값을 m에 저장
for i in range(len(result)): # 빈도수가 동일할 경우 전부 출력하기 위해 for문 수행
    if m == result[i]: # 가장 높은 빈도수와 값이 동일할 경우
        print(chr(i+97), end='') #해당 문자 출력
        # A~Z : 65~90, a~z : 97~122
        # 97이 소문자 a이므로, 97+1 = 98 = b