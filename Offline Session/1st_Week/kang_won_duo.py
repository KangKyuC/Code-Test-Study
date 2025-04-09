N = int(input())
input_list = list(map(int,input().split(' ')))
stack = []
parent_list = [-1] * len(set(input_list))

for idx in range(N):
    if stack:
        if input_list[idx] in stack:
            stack.pop()
        else:
            parent_list[input_list[idx]] = stack[-1]
            stack.append(input_list[idx])
    else:
        stack.append(input_list[idx])

print(len(parent_list))
for a in parent_list:
    print(a, end=" ")
