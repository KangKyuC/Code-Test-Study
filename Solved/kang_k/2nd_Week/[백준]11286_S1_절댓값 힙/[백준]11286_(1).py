# 시간: 120ms

import sys
import heapq

input = sys.stdin.readline

heap = []
result = []

for _ in range(int(input())):
    cmd = int(input())

    if cmd:
        heapq.heappush(heap, (abs(cmd), cmd))
    else:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)

print(*result, sep = "\n")