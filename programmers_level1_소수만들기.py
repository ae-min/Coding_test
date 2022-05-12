from itertools import combinations #순서상관없이 원하는 개수 추출하는 조합 
# 순서가 상관있는 순열은 permutations

def prime(a,b,c):
    total = a+b+c
    #소수판별법 2보다크고, 자신보다 작은 숫자 중에서 0으로 나누어떨어지면 소수가 아닌 것
    #소수 : 2보다 큰 수로 나눴을 때, 1과 자기자신으로만 나누어 떨어지는 것
    for i in range(2,total):
        if total % i == 0: 
            return False
    return True

def solution(nums):
    answer = 0
    lst = list(combinations(nums,3))
    for i in lst:
        if prime(i[0],i[1],i[2]):
            answer += 1
    return answer

'''
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
'''