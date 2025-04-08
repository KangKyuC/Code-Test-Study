# 코딩 중에 object is not subscriptable 문제 발생
# https://jimmy-ai.tistory.com/193
#

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            return print(-1)
    def size(self):
        return print(len(self.stack))
    def empty(self):
        return print(1) if self.stack else print(0)
    def top(self):
        return print(self.stack[-1]) if self.stack else print(-1)

def activate_method(stack, input_var):
    print(input_var)
    method = input_var.split()[0]

    if method == "push":
        print("push activated:", int(input_var.split()[1]))
        stack.push(int(input_var.split()[1]))
    elif method == "pop":
        print("pop activated \n")
        stack.pop()
    elif method == "size":
        print("size activated \n")
        stack.size()
    elif method == "empty":
        print("empty activated \n")
        stack.empty()
    elif method == "top":
        print("top activated \n")
        stack.top()
    else:
        print("There is no Method that you input")

if __name__ == '__main__':
    stack = Stack()
    for _ in range(int(input())):
        activate_method(stack, input())