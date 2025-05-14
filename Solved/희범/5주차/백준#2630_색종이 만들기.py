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
input_num = int(input())
input_str = [input() for _ in range(input_num)]

pre_num = ""
pre_mat = ""

# 행열구조 input_str[x][y]

1. input_str[0][0] 
2. input_str[1][0] x+1
3. input_str[0][1] y+1
4. input_str[1][1] x+1, y+1

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
    # size: 블록 한 변의 길이 (2^k 형태)
    # result: quadtree 정보를 누적할 리스트

    # 1) 블록이 균질하다면
    if is_uniform(x, y, size):
        result.append((x, y, size, matrix[x][y]))  
        # (x, y, size, 값) 형태로 저장
    else:
        # 2) 섞여 있으면 4분할
        half = size // 2
        # Ⅰ 사분면
        quadtree(x,       y,       half, result)
        # Ⅱ 사분면
        quadtree(x,       y+half,  half, result)
        # Ⅲ 사분면
        quadtree(x+half,  y,       half, result)
        # Ⅳ 사분면
        quadtree(x+half,  y+half,  half, result)

result = []

quadtree(0, 0, len(matrix), result)

white = 0
blue = 0

for i in result:
    if i[3] == "0":
        white += 1
    else:
        blue += 1

print(white, blue, sep="\n")
