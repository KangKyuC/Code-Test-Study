import sys

input = sys.stdin.readline

input_num = list(map(int, input().split()))
word_list = [input().strip() for _ in range(input_num[0])] # ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh'] 확인
prefix_list = [input().strip() for _ in range(input_num[1])] # ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus'] 확인
word_list = set(word_list)


result = []


for word in word_list:
    for prefix in prefix_list:
        if word == prefix:
            continue
        elif word.startswith(prefix):
            result.append(prefix)
            word = word.replace(prefix, "")

print(len(result))
