import sys

class Queue:
    def __init__(self):
        self.Queue = []  

    def push(self, value):
        self.Queue.append(value)

    def pop(self):
        if self.empty() == 1:
            return -1
        result = self.Queue[0]
        self.Queue = self.Queue[1:] # 시간 초과
        return result

    def size(self):
        return len(self.Queue)
        
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.Queue[0]
    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.Queue[-1]

N = int(input())
queue = Queue()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        value = int(cmd[1])
        queue.push(value)
    else:
        method = getattr(queue,cmd[0])
        print(method())
