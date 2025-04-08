# 시간 44ms
# 추가 메모리에 대한 공간을 최적화
# input 방식의 변조로 불필요한 순회를 줄임
# 0에 대한 일괄적인 처리 X
# b-1 로 순회를 한 단계 앞당겨 1, 2, 3, 4 순서의 딕셔너리 완성

import sys

pattern_dict = {
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

n = int(input().strip())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10

    if a:
        pattern = pattern_dict[a]
        print(pattern[(b-1) % len(pattern)])
    else:
        print(10)