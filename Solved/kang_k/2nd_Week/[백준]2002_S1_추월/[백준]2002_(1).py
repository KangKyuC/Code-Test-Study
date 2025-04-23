from collections import deque

queue = deque()
N = int(input())

for _ in range(N):
    queue.append(input())

out_cars = set()

out_list = [input() for _ in range(N)]

for out_car in out_list:
    if queue[0] == out_car:
        # 큐의 맨 위가 나온 놈과 같음.
        # 아직 안 나온 놈이면 pop 하면 됨.
        # 나온 놈이면 안 나온 놈 나올 때 까지, pop 해줘야 함.
        queue.popleft()
        if not len(queue):
            break
        while (queue[0] in out_cars):
            # 나온 차이니, 큐의 탑과 다를 때 까지 빼버림.
            queue.popleft()
            if not len(queue):
                break
    else:
        # 큐의 맨 위와 현재 값이 다름.
        # 다르다는 것은 순서가 바뀌었음을 의미함.
        # Why? -> 항상 큐는 순서를 유지하고 있으니까.
        # 그러면 나온놈이라고 집합에 넣어서 알려줌.
        out_cars.add(out_car)

print(len(out_cars))