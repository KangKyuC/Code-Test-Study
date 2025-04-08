# 시간 40ms
# 하드코딩 방식으로 직접 연산, 거듭제곱을 활용하게 되어 일부 연산 시간 발생으로 보여짐
# 0에 대한 일괄적인 처리가 되지 않음.

import sys

n = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(n)]

for ep in arr:
    if ep[1] % 4:
        result = ((ep[0] % 10) ** (ep[1] % 4)) % 10
    else:
        result = ((ep[0] % 10) ** 4) % 10
    if result:
        print(result)
    else:
        print(10)
