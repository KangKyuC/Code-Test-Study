import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.items = []
    
    # 맨 위에 데이터 E를 추가
    def push(self, item):
        self.items.append(item)
    
    # stack 가장 위에 있는 데이터 반환
    def pop(self):
        if self.empty():
            return -1
        return self.items.pop()
    
    # 비어있다면 True, 아니라면 False 반환
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    # 현재 stack에 들어있는 데이터 수 반환
    def size(self):
        return len(self.items)
    
    # 현재 stack 맨 위에 있는 데이터 확인
    def top(self):
        if self.empty():
            return -1
        return self.items[-1]

stack = Stack()
N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        value = int(cmd[1])
        stack.push(value)
    else:
        method = getattr(stack,cmd[0])
        print(method())