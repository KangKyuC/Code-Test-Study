"""

https://www.acmicpc.net/problem/1149
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이
1번 집부터 한 줄에 하나씩 주어진다. 
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

규칙
1. 집의 색은 입접한 이웃의 색과 같지 않아야 한다.
2. 칠할 집의 수는 N개이다.
3. 칠할 수 있는 색은 빨/초/파이며, 각각의 색의 비용은 주어진다.
4. 출력 값은 모든 집을 칠하는 비용의 최솟값이다.

예상풀이
1. 첫 번째 리스트에서 min값을 선정
2. min값을 선정한 인덱스 추출
3. 다음 리스트에서 추출한 인덱스 제거 후, min값 선정
4. 그 리스트에서 인덱스 추출
5. 이 과정을 N번 반복하고 추출된 값을 Sum

예제 입출력
3
26 40 83
49 60 57
13 89 99

96 # R에 최솟값이 2개이므로 R 26 + G 57 + R 13 = 96

3
1 100 100
100 1 100
100 100 1

3 # RGB로 번갈아가며 칠하는게 제일 저렵하므로, R 1 + G 1 + R 1 = 3

3
1 100 100
100 100 100
1 100 100

102

6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91

208

8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19

253
"""

# for i in range(input_num):
#     if prev_index is None:
#         result += min(input_list[i])
#         prev_index = input_list[i].index(min(input_list[i]))
#         print(input_list[i], result, prev_index)
#     elif prev_index == input_list[i].index(min(input_list[i])):
#         del input_list[i][prev_index+1] 
#         result += min(input_list[i])
#         prev_index = input_list[i].index(min(input_list[i]))
#         print(input_list[i], result, prev_index)
#     else:
#         del input_list[i][prev_index+1] 
#         result += min(input_list[i])
#         prev_index = input_list[i].index(min(input_list[i]))
#         print(input_list[i], result, prev_index)

# print(result)

"""
현재 8이상에서 문제가 발생해서 풀이 일시 중지 중
"""

input_num = int(input())
input_list = [list(map(int, input().split())) for _ in range(input_num)]

prev_list = []
prev_index = None


for i in input_list:
    if prev_index is None:
        prev_index = i.index(min(i))
        result += min(i)
        print(i, prev_index, min(i))

    else:
        i[prev_index] = float("inf")
        prev_index = i.index(min(i))
        result += min(i)

        print(i, prev_index, min(i))

print(result)
