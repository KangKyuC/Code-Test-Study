"""
시간 초과

문제
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

4
3 5 2 7

출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

5 7 7 -1
"""
import sys
input = sys.stdin.readline

input_num = int(input()) # 입력할 수
input_list = [int(v) for v in input().split()][:input_num] # 입력할 수만큼 수를 입력
okunum = None # 오큰수
result = [] # 출력 값



for i in input_list: # 입력된 수만큼 반복
    if okunum is None: # 오큰수가 비어있다면
        okunum = list(filter(lambda x: x > i, input_list)) # input_list에서 i보다 큰 오큰수를 찾아서 리스트로 반환
        result.append(list(okunum)[0]) # 오큰수[0]을 출력 값에 추가

    elif okunum[0] >= i: # 오큰수가 i보다 크거나 같다면
        okunum = list(filter(lambda x: x > i, input_list)) # input_list에서 i보다 큰 오큰수를 찾아서 리스트로 반환
        if len(okunum) == 0:
            result.append(-1)
            pass
        result.append(list(okunum)[0]) # 오큰수[0]을 출력 값에 추가

    else: # 오큰수가 없다면
        result.append(-1) # -1을 출력 값에 추가

print(result)
