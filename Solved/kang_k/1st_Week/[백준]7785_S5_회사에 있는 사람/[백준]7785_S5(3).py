# 시간 164 ms
# 반복적인 순회 및 비교를 통한 정렬 유지 vs sort 거의 비슷할 것으로 보임.
# 출력 부분에서 print 대신 sys.stdout.write 를 활용해보려 함.

import sys
input = sys.stdin.readline

current = set()

for _ in range(int(input())):
    name, action = input().split()
    if action == "enter":
        current.add(name)
    else:
        current.remove(name)

result = sorted(current, reverse=True)
sys.stdout.write('\n'.join(result) + '\n')