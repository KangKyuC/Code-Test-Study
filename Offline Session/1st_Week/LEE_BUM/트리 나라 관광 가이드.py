int(input()) # 입력시행의 수
visit_list = list(map(int, input().split())) # 방문한 도시 순서
visited_set = set(visit_list) # 자식 도시 종류
k = len(visited_set) # 자식 도시의 수
index_list = [0]

# print(list_visit) # [0, 1, 2, 1, 3, 4, 3, 5, 3, 1, 6, 1, 0, 7, 8, 7, 9, 7, 0]
# print(visited) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(k) # 10


# parent = [-1]

# previous = []
# post = []

# for i in range(1, len(list_visit)-2):    
#     if list_visit[i] == list_visit[i+2]:
#         parent.append(list_visit[i])

# visited = [False] * k


# visited.add(list_visit[0])

# print(parent)
# print(list_visit)

# parent.append(list_visit[0]) = -1

# for i in list_visit[1:]:
#     current_city = list_visit[i]
#     if current_city != visited:
#         parent[current_city] = list_visit[i-1]

# print(parent) 
    
# print(len(visited))
