def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))] #[[]*열]*행
    # len(arr) : row행의 개수
    # len(arr[0]) : row행이 가지고 있는 column열의 개수
    # arr2는 열인데, 그냥 arr2라고 하면 행의 개수가 추출되므로, arr2[0]이라고해서 0행의 열을 출력하도록함(모든행의 열이 똑같으므로 그냥 0행의 열을 구함)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k]*arr2[k][j] #행렬곱셈공식
    return answer

'''
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.

입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''