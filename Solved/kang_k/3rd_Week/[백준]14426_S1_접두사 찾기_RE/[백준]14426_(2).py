# 96 ms
# 직접 구현(슬라이싱 기반) 대신 startswith() 를 통한 내부 로직 이용
# 이름이 의미가 되도록 변수명 수정

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = sorted(set(input().rstrip() for _ in range(N)))
queries = sorted(input().rstrip() for _ in range(M))

count = 0
i = j = 0

while i < N and j < M:
    if words[i].startswith(queries[j]):
        count += 1
        j += 1
        continue
    elif words[i] > queries[j]:
        j += 1
        continue
    elif words[i] < queries[j]:
        i += 1

print(count)
