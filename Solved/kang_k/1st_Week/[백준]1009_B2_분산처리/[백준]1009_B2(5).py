# 메모리 최적화를 위해 튜플 형식으로 생성
# 안정성 및 무결성 (불변) 확보
# 시간 36ms

import sys
input = sys.stdin.readline

pattern = (
    [10],  # for digit 0
    [1],   # for digit 1
    [2, 4, 8, 6],  # for digit 2
    [3, 9, 7, 1],  # for digit 3
    [4, 6],        # for digit 4
    [5],           # for digit 5
    [6],           # for digit 6
    [7, 9, 3, 1],  # for digit 7
    [8, 4, 2, 6],  # for digit 8
    [9, 1]         # for digit 9
)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10
    cycle = pattern[a]
    index = (b-1)%len(cycle)
    print(cycle[index])