# 0에 대한 일괄처리
# 변수 추가 생성 cycle -> 직관력 향상
# 시간 32ms

import sys
input = sys.stdin.readline

pattern ={
    0: [10],
    1: [1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a %10
    cycle = pattern[a]
    index = (b-1)%len(cycle)
    print(cycle[index])