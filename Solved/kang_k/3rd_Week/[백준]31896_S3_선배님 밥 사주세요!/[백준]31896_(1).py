# 32ms
# 0명에 대한 예외처리

import sys

input = sys.stdin.readline

N = int(input())
senior_dict = dict()
avail_senior = set()


for _ in range(N):
    S, W, D, P = input().split()
    senior_dict[S] = list(map(int, (W, D, P)))

for _ in range(N):
    S, M = input().split()
    if senior_dict[S][2] <= int(M):
        avail_senior.add(senior_dict[S][0] * 7 + senior_dict[S][1])

avail_senior = sorted(list(avail_senior))
if len(avail_senior) > 0:
    maxim = curr = 1

    for prev, now in zip(avail_senior, avail_senior[1:]):
        if now == (prev + 1):
            curr += 1
        else:
            curr = 1
        maxim = max(curr, maxim)
    print(maxim)
else:
    print(0)