# 64m
# I/O 처리 문제를 output_list를 생성해 한 번에 일괄적으로 처리함.

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
output_lines = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "pop":
        if len(queue):
            output_lines.append(queue.popleft())
        else:
            output_lines.append(-1)
    elif cmd[0] == "size":
        output_lines.append(len(queue))
    elif cmd[0] == "empty":
        output_lines.append(0 if len(queue) else 1)
    elif cmd[0] == "front":
        output_lines.append(queue[0] if queue else -1)
    elif cmd[0] == "back":
        output_lines.append(queue[-1] if queue else -1)
    else:
        queue.append(cmd[1])

print(*output_lines, sep = "\n")