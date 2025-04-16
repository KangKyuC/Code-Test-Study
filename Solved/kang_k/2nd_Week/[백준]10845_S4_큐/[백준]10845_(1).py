# 시간 초과 문제 발생
# 링크드리스트로 구현해서 > 내장 C 타입 형태가 아니라서 오버헤드가 다수 발생하는 것으로 보임.

import sys

class LinkedList:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def push(self, value):
        if self.head is not None:
             tmp = LinkedList(value, None, self.rear)
             self.rear.next = tmp
             self.rear = tmp
             self.length += 1
        else:
            self.head = LinkedList(value, None,None)
            self.rear = self.head
            self.length += 1

    def pop(self):
        if self.head is not None:
            num = self.head.value
            self.head = self.head.next
            self.length -= 1

            if self.head is None:
                self.rear = None
            return num
        else:
            return -1

    def size(self):
        return self.length

    def empty(self):
        if self.head is not None:
            return 0
        else:
            return 1

    def front(self):
        return self.head.value if self.head is not None else -1

    def back(self):
        return self.rear.value if self.rear is not None else -1


N = int(input())
queue = Queue()

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        queue.push(cmd[1])
    else:
        method = getattr(queue, cmd[0])
        print(method())