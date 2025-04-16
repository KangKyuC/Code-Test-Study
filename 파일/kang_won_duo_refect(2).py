import sys

input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))

visited = set()
visited.add(input_list[0])
parent = [-1] * len(set(input_list))

for i in range(1, N):
    if input_list[i] not in visited:
        visited.add(input_list[i])
        parent[input_list[i]] = input_list[i - 1]

print(len(visited))
print(*parent[:len(visited)])
