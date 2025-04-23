# 메모리 문제로 인해 데이터 전부를 올리는게 불가함.
# 일반 sort가 nlogn이라 해당 부분을 우려해 block 한 것으로 보임.

import heapq
import sys

input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    nums = list(map(int, input().split()))
    num_list.append(nums)

heap = [(-num_list[N-1][i], N-1, i) for i in range(N)]
# heapq에 마지막 줄 모든 원소를 삽입 이때 (-value, row, col)로 저장

for _ in range(N):
    value, row, col = heapq.heappop(heap)
    if row > 0:
        heapq.heappush(heap, (-num_list[row-1][col], row-1, col))

print(-value)