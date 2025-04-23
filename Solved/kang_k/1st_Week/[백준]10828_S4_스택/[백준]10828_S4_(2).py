# 런타임 오류 발생
# 오버헤드가 발생하는 문제로, 오버헤드를 최대한으로 줄일 수 있도록 수정
# 특히 stdout.write 방식으로 오버헤드 최소화
# Insight: Class와 Function의 오버헤드 발생 원인과 맥락 확인

import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

for _ in range(n):
    cmd = input().split()
    op = cmd[0]
    if op == "push":
        stack.append(int(cmd[1]))
    elif op == "pop":
        output.append(str(stack.pop()) if stack else "-1")
    elif op == "size":
        output.append(str(len(stack)))
    elif op == "empty":
        output.append("0" if stack else "1")
    elif op == "top":
        output.append(str(stack[-1]) if stack else "-1")

sys.stdout.write("\n".join(output))
