import sys
import heapq

input = sys.stdin.readline

n = int(input())
gift = []

for _ in range(n):
    a = input().strip()
    if a == "0":
        if not gift:
            print(-1)
        else:
            print(-heapq.heappop(gift))
    else:
        for num in map(int, a.split()[1:]):
            heapq.heappush(gift, -num)