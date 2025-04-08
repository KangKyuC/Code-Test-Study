# 시간 164 ms
# 로그가 순차적으로 제공된다는 점에 주목하여 문제 풀이
# 딕셔너리 대신, 단일 집합으로 관리
# 집합이기에, 중복이 관리되고, 빠른 비교 연산이 가능
# 최종 sorted에서 시간이 소요되는 것이 문제로 추정됨.
# 추가 시간이 없었다면 문제를 제대로 풀이하지 못했을 것임.

import sys
input = sys.stdin.readline

current = set()

for _ in range(int(input())):
    name, action = input().split()
    if action == "enter":
        current.add(name)
    else:
        current.remove(name)

print(*sorted(current, reverse=True), sep='\n')