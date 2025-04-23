
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n: int):
        self.stack.append(n)
    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            return print(-1)
    def size(self):
        return print(len(self.stack))
    def empty(self):
        return print(0) if self.stack else print(1)
    def top(self):
        return print(self.stack[-1]) if self.stack else print(-1)

def activate_method(stack, input_var):
    parts = input_var.split()
    method = parts[0]

    if method == "push":
        stack.push(int(parts[1]))
    elif method == "pop":
        stack.pop()
    elif method == "size":
        stack.size()
    elif method == "empty":
        stack.empty()
    elif method == "top":
        stack.top()

stack = Stack()
for _ in range(int(input())):
    activate_method(stack, input())