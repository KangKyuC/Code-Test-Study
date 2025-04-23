# 40ms
# 딕셔너리 기반 풀이로 수정

import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

ops = {
    "push": lambda arg: stack.append(int(arg)),
    "pop":  lambda _: output.append(str(stack.pop()) if stack else "-1"),
    "size": lambda _: output.append(str(len(stack))),
    "empty":lambda _: output.append("0" if stack else "1"),
    "top":  lambda _: output.append(str(stack[-1]) if stack else "-1"),
}

for _ in range(n):
    cmd = input().split()
    ops[cmd[0]](cmd[1] if len(cmd) > 1 else None)

sys.stdout.write("\n".join(output))
