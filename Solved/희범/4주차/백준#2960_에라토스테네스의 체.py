"""
메모리: 32412 KB, 시간: 36 ms
https://www.acmicpc.net/problem/2960
문제
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

이 알고리즘은 다음과 같다.

2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)

출력
첫째 줄에 K번째 지워진 수를 출력한다.

입출력

7 3
6

15 12
7

10 7
9

생각정리
1. 변수는 N과 K
2. N은 2부터 N까지의 모든 정수
3. K는 지우는 수의 순서
4. 숫자 N을 입력하면 2부터 N까지의 리스트 작성
5. 리스트에서 가장 작은 수를 찾아 지우고, 해당 수의 배수를 지운다.
6. 5.의 과정을 K번째가 되었을 때, 지우려던 수를 출력하고 멈춘다.

"""

import sys
input = sys.stdin.readline

input_num, input_k = [int(i) for i in input().split()]
num_list = [i for i in range(input_num, 1, -1)]

stack_list = [] # 삭제될 K 값들을 넣을 리스트
temp_list = [] # K 외의 값들을 임시 보관할 리스트
i = 2


while input_k != len(stack_list): # stack)list의 요소 갯수가 K번째와 같아질 떄 까지

    if len(num_list) == 0 : # num_list가 빈 리스트일 때
        num_list = temp_list[::-1] # temp_list를 num_list로 이동
        temp_list = [] # temp_list 초기화
        i += 1 # 다음 배수

    value = num_list.pop() # num_list에서 가장 작은 수를 pop
    
    if value % i == 0 : # value가 i의 배수라면
        stack_list.append(value) # stack_list에 value값을 추가
    else : # 그 외의 경우
        temp_list.append(value) # value를 temp_list에 추가

print(stack_list[-1]) # K번째 삭제한 값을 출력
