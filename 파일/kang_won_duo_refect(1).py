# 아니 도대체 어디서 병목이 발생하는거여
# 후보 1) input -> 공백 처리 strip으로 인해 input으로 받는 편이 나음
# 후보 2) print -> 문제 풀이 자체에 큰 영향을 주진 않기에 패스
# 후보 3) parent_list -> 리스트 조회가 필요 -> index 기반으로 탐색하기에 O(1)
# 후보 4) print 방식 -> sys.stdout.write 도 가능한데, 큰 영향을 주진 않기에 패스
# 후보 5) 도저히 모르겠다..

input()
stack = []
input_list = list(map(int, input().split(' ')))
parent_list = [-1] * len(set(input_list))

for a in input_list:
    if stack:
        for number in stack:
            if number == a:
                stack.pop()
                break
        else:
            parent_list[a] = stack[-1]
            stack.append(a)
    else:
        stack.append(a)

print(len(parent_list))
print(*parent_list, end=" ")