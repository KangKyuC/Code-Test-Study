import sys

input = sys.stdin.readline

a, b = input().split()

A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}

print(len(A ^ B))
