# 112 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
compare_list = sorted(set(input().rstrip() for _ in range(N)))
prefix_list = sorted(input().rstrip() for _ in range(M))

count = 0
i = j = 0

while i < N and j < M:
    if compare_list[i][:len(prefix_list[j])] == prefix_list[j]:
        count += 1
        j += 1
        continue
    elif compare_list[i] > prefix_list[j]:
        j += 1
        continue
    elif compare_list[i] < prefix_list[j]:
        i += 1

print(count)
