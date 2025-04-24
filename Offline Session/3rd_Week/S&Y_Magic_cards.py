# 미완

# 입력
# 14 4 6 4
# 1 9 7 11 3 5
# 2 10 3 6 7 11
# 4 5 6 7 6 12
# 8 11 10 9 12 9
# YYNY
# NNNY
# YNNN
# NNNN

# 출력
# 11
# 8
# 1
# 0

N, K, M, F = map(int, input().split())
cards_nums = []
answers = []
candidates = set()

for i in range(1,N+1):
    candidates.add(i)

for _ in range(K):
    temp = set(map(int, input().split()))
    cards_nums.append(temp)

for i in range(F):
    temp = input()
    arr_temp = []
    for j in range(len(temp)):
        arr_temp.append(temp[j])
    answers.append(arr_temp)

for i in range(len(answers)):
    for j in range(len(answers[i])):
        # print("answers",answers[i][j])
        if answers[i][j] == 'Y':
            candidates = candidates & cards_nums[i]
            print("cards_nums", cards_nums[i])
            print("Y일 때,",candidates)
        


            
