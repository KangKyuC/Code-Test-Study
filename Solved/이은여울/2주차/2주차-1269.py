a_n, b_n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = (A-B)|(B-A) # union(|) 합집합 연산자

print(len(result))