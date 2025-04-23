import sys
input = sys.stdin.readline

N, K, M, F = map(int, input().split())
numbers = []
thinking_num = []

for _ in range(K):
    numbers.append(set(map(int, input().split())))

for _ in range(F):
    answer_numbers = set(i for i in range(1, N + 1))
    answer = input().rstrip()
    for i in range(K):
        if "Y" == answer[i]:
            answer_numbers = answer_numbers & numbers[i]
        else:
            answer_numbers = answer_numbers - numbers[i]

    if len(answer_numbers) == 1:
        thinking_num.append(list(answer_numbers)[0])
    else:
        thinking_num.append(0)

print(*thinking_num, sep = "\n")