L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
x = 0
y = 0

if A%C == 0 or B%D == 0:
    print(L-max(A//C, B//D))
elif A % C != 0:
    print(L-max((A//C)+1, B//D))
else: 
    print(L-max(A//C, (B//D)+1))

#예제풀이는 되는데 왜 틀렸다고 나오는지는 모르겠다
'''
방학 L일
수학 총 B페이지 하루 최대 D
국어 총 A페이지 하루 최대 C
방학 20일
수학 30페이지 하루에 8페이지 4
국어 25페이지 하루에 6페이지 5
총페이지를 하루에 가능한 페이지로 나누는데 나머지가
0이 안되면 몫에 1을 추가하기.
그렇게해서 최종으로 수학과 국어중에 더 오래걸리는 맥스를 구한다
'''


