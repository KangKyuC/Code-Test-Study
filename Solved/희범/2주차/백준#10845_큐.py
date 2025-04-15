"""
https://www.acmicpc.net/problem/10845
Time: 44 ms, Memory: 33432 KB -BaekjoonHub

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
input = sys.stdin.readline


num = int(input())


class queue():
    def __init__(self):
        self.n = ''
        self.result = []

    def push(self, n):
        self.result.append(n)
    
    def pop(self):
        if len(self.result) == 0:
            return -1
        else :
            return self.result.pop(0)
    
    def size(self):
        return len(self.result)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.result[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.result[-1]

myQueue = queue()

output = []

for _ in range(num):
    input_list = [v for v in input().split()]
    if input_list[0] == "push":
        myQueue.push(input_list[1])
    elif input_list[0] == "pop":
        output.append(myQueue.pop())
    elif input_list[0] == "size":
        output.append(myQueue.size())
    elif input_list[0] == "empty":
        output.append(myQueue.empty())
    elif input_list[0] == "front":
        output.append(myQueue.front())
    elif input_list[0] == "back":
        output.append(myQueue.back())

for i in output:
    print(i)
