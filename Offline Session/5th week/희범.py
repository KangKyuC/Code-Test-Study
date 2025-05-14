"""
문제
아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진
정사각형 모양의 종이가 주어져 있고, 각 정사각형들은
하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 
주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를
가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.


전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면
종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로
중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은
크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이
I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은
색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의
색종이로 나눈다. 이와 같은 과정을 잘라진 종이가
모두 하얀색 또는 모두 파란색으로 칠해져 있거나,
하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를
처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를,
<그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와
7장의 파란색 색종이를 보여주고 있다.


입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색
(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와
파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다.
N은 2, 4, 8, 16, 32, 64, 128 중 하나이다.
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로
둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0,
파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고,
둘째 줄에는 파란색 색종이의 개수를 출력한다.

예제 입력 1 
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

예제 출력 1 
9
7

풀이 과정
시작

1. 입력 받기
   N ← 정수 입력  // 행렬의 크기
   matrix ← 빈 2차원 배열 크기 N×N
   for i from 0 to N-1:
     한 줄을 공백 기준으로 분할하여 matrix[i]에 저장

2. 균일 검사 함수 정의
   함수 isUniform(x, y, size) → Boolean:
     기준값 ← matrix[x][y]
     for i from x to x+size-1:
       for j from y to y+size-1:
         if matrix[i][j] ≠ 기준값:
           return False
     return True

3. 쿼드트리 분할 함수 정의
   프로시저 quadtree(x, y, size, resultList):
     if isUniform(x, y, size) then
       // 모두 같은 값이면 하나의 블록으로 취급
       resultList에 (x, y, size, matrix[x][y]) 추가
     else
       // 섞여 있으면 4등분하여 재귀 호출
       half ← size / 2
       // 1사분면 (왼쪽 위)
       quadtree(x,       y,       half, resultList)
       // 2사분면 (오른쪽 위)
       quadtree(x,       y+half,  half, resultList)
       // 3사분면 (왼쪽 아래)
       quadtree(x+half,  y,       half, resultList)
       // 4사분면 (오른쪽 아래)
       quadtree(x+half,  y+half,  half, resultList)

4. 쿼드트리 실행 및 색상 개수 세기
   resultList ← 빈 리스트
   quadtree(0, 0, N, resultList)

   whiteCount ← 0  // 0인 블록 개수
   blueCount  ← 0  // 1인 블록 개수

   for each (x, y, size, value) in resultList:
     if value = "0" then
       whiteCount ← whiteCount + 1
     else
       blueCount ← blueCount + 1

5. 결과 출력
   출력 whiteCount
   출력 blueCount

끝

"""

import sys

input = sys.stdin.readline

input_num = int(input())
matrix = [input().split() for _ in range(input_num)]


def is_uniform(x, y, size):
    # (x,y)에서 시작해 size×size 영역이 모두 같은 값인지 확인
    
    first = matrix[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] != first:
                return False
    return True

def quadtree(x, y, size, result):
    # x,y: 현재 블록의 왼쪽 위 좌표
    # size: 블록 한 변의 길이
    # result: 쿼드 트리 결과

    # 1) 같은 숫자가 모이면
    if is_uniform(x, y, size):
        result.append((x, y, size, matrix[x][y]))  
        # (x, y, size, 값) 형태로 저장
    else:
        # 2) 숫자가 섞여 있으면 4분할
        half = size // 2
        # 1 사분면
        quadtree(x, y, half, result)
        # 2 사분면
        quadtree(x+half, y, half, result)
        # 3 사분면
        quadtree(x, y+half, half, result)
        # 4 사분면
        quadtree(x+half, y+half, half, result)

result = []

quadtree(0, 0, len(matrix), result)

white = 0
blue = 0

for i in result:
    if i[3] == "0": # 0이면
        white += 1
    else: # 1이면
        blue += 1

print(white, blue, sep="\n")
