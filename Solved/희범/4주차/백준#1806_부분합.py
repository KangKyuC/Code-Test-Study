"""
문제

https://www.acmicpc.net/problem/1806
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다.
둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며,\
10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

입출력 예시

10(길이 N 수열) 15(부분합 S)
5 1 3 5 10 7 4 9 2 8

2

어떻게 풀것인가?

1. 부분합을 구하는 함수를 만든다.
2. 부분합이 S 이상이 되는 것 중 가장 짧은 것의 길이를 구한다.
3. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력한다.

풀이 방안
(1) nCr로 부분합을 구하고 S 이상이 되는 것 중 가장 짧은 것의 길이를 구한다.
시간 복잡도 : O(N^2)

(2) 투포인터를 사용하여 부분합을 구하고 S 이상이 되는 것 중 가장 짧은 것의 길이를 구한다.
시간 복잡도 : O(N)

(3) 슬라이딩 윈도우를 사용하여 부분합을 구하고 S 이상이 되는 것 중 가장 짧은 것의 길이를 구한다.
시간 복잡도 : O(N) # 가장 쉬운 방법일듯하다 - 일단 채택

슬라이딩 윈도우 구현

input_list = (5,1,3,5,10,7,4,9,2,8)
s = 15

n = len(input_list)

for i in range(n-1):
    a = input_list[i:i+2]
    print(a)
    print(sum(a))

    if sum(a) >= s:
        print(len(a))
        break

n = 2 일 때의 슬라이딩 윈도우 결과는 구했고,
이제 슬라이딩 윈도우 크기가 늘어나는 로직을 어떻게
짜야할까?

10 15
5 1 3 5 10 7 4 9 2 8

10 30
5 1 3 5 10 7 4 9 2 8
"""

import sys  
input = sys.stdin.readline

length, num_sum = map(int, input().split())
input_list = list(map(int, input().split()))[:length]

n = 2
temp = []

while n <= length:
    for i in range(length-n+1):
        temp.append(sum(input_list[i:i+n]))
        size = max(temp)
        if size >= num_sum:
            break

    result= n
    temp = []

    if size >= num_sum:
        break

    n += 1
        
print(result)
