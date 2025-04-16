N = int(input())
input_list = list(map(int,input().split(' ')))
stack = []
parent_list = [-1] * len(set(input_list))
print(input_list)

for a in input_list:
    print("stack:", stack)
    print("parent_list:", parent_list)
    print("node number:", a)
    if stack:
        if a in stack:
            stack.pop()
        else:
            parent_list[a] = stack[-1]
            stack.append(a)
    else:
        stack.append(a)

