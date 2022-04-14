while True:
    s = input()
    cnt = 0
    if s == "#":
        break
    
    for i in s:
        if i in "aeiouAEIOU":
            cnt += 1
    print(cnt)       
    
# 문자열 = 'hello world'
# if 'a' not in 문자열:
#     print('a가 문자열안에 없다')
# if 'e' in 문자열:
#     print('e가 문자열안에 있다')