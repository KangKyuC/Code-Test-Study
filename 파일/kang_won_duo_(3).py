# 시간초과 문제 발생

input()
stack = []
input_list = list(map(int, input().split(' ')))
parent_list = [-1] * len(set(input_list))

for a in input_list:
    if stack:
        if a in stack:
            stack.pop()
        else:
            parent_list[a] = stack[-1]
            stack.append(a)
    else:
        stack.append(a)

print(len(parent_list))
print(*parent_list, end=" ")