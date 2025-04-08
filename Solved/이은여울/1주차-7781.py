import sys
input = sys.stdin.readline

n = int(input())
members = set()
for _ in range(n):
    name, act = input().split()
    if act == 'enter':
        members.add(name)
    else:
        members.remove(name)

for name in sorted(members, reverse=True):
    print(name)
