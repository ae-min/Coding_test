color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = color.index(input())
b = color.index(input())
c = color.index(input())

result = int(str(a)+str(b))*(10**c)
print(result)

# 리스트.index(값) : 리스트안의 값의 위치를 반환
# 4+7을 int형으로 변환하면 47이 되므로 47*100을 해준 것