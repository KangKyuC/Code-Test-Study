# https://www.acmicpc.net/status?user_id=dachou16&problem_id=1269&from_mine=1
# 메모리: 88232 KB, 시간: 256 ms

import sys

input = sys.stdin.readline # input 속도 최적화

set_size = list(map(int, input().split())) # input 형태 3 5

a_set = set([a for a in input().split()][:set_size[0]]) # A의 원소 input은 set_size[0]개로 제한
b_set = set([b for b in input().split()][:set_size[1]]) # B의 원소 input은 set_size[1]개로 제한

print(len(a_set - b_set) + len(b_set - a_set)) # A와 B의 차집합
