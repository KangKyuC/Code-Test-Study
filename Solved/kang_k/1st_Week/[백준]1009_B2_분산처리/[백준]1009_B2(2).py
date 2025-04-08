# 시간 44ms
# 딕셔너리를 통한 연산 개선 -> 추가 메모리
# 직관적이나, 인덱스름 맞춰주기 위해 4, 1, 2, 3 순서로 진행
# 0에 대한 일괄적인 처리 X

import sys

n = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(n)]

pattern_dict = {
    1: [1, 1, 1, 1],
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4, 6, 4],
    5: [5, 5, 5, 5],
    6: [6, 6, 6, 6],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9, 1, 9]
}

for ep in arr:
    if ep[0]%10:
        print(pattern_dict[ep[0]%10][ep[1]%4])
    else:
        print(10)