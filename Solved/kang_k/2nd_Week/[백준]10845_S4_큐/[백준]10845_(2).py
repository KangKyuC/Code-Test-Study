# 또 시간초과 발생
# I/O 처리로 인한 문제인 것으로 보고, 이를 수정해봄.

from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(0 if len(queue) else 1)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)
    else:
        queue.append(cmd[1])
