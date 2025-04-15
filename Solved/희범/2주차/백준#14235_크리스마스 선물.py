"""
https://www.acmicpc.net/problem/14235
메모리: 60648 KB, 시간: 172 ms

문제
크리스마스에는 산타가 착한 아이들에게 선물을 나눠준다. 올해도 산타는 선물을 나눠주기 위해 많은 노력을 하고 있는데, 전세계를 돌아댕기며 착한 아이들에게 선물을 나눠줄 것이다. 하지만 산타의 썰매는 그렇게 크지 않기 때문에, 세계 곳곳에 거점들을 세워 그 곳을 방문하며 선물을 충전해 나갈 것이다. 또한, 착한 아이들을 만날 때마다 자신이 들고있는 가장 가치가 큰 선물 하나를 선물해 줄 것이다.
이제 산타가 선물을 나눠줄 것이다. 차례대로 방문한 아이들과 거점지의 정보들이 주어졌을 때, 아이들이 준 선물들의 가치들을 출력하시오. 만약 아이들에게 줄 선물이 없다면 -1을 출력하시오.

입력
첫 번째 줄에서는 아이들과 거점지를 방문한 횟수 n이 주어진다.(1≤n≤5,000)
다음 n줄에는 a가 들어오고, 그 다음 a개의 숫자가 들어온다. 이는 거점지에서 a개의 선물을 충전하는 것이고, 그 숫자들이 선물의 가치이다. 만약 a가 0이라면 거점지가 아닌 아이들을 만난 것이다. 선물의 가치는 100,000보다 작은 양의 정수이다.(1≤a≤100)

5
0
2 3 2
0
0
0

출력
a가 0일 때마다, 아이들에게 준 선물의 가치를 출력하시오. 만약 줄 선물이 없다면 -1을 출력하라. 적어도 하나의 출력이 있음을 보장한다.

-1
3
2
-1

슈도 코드
for문으로
input list로 입력 받은 뒤
값이 0이면 append
그렇지 않으면 힙에서 인출
값이 0이 아니면
힙으로 변환
for문으로 출력값 리스트 표시

풀고난 뒤 한 마디 : 튜플이라는게 지울 수 있는거였어?!
"""

import heapq
import sys
input = sys.stdin.readline

num = int(input())
output = []
heap = []

for _ in range(num):
    input_list = [int(v) for v in input().split()]
    if input_list[0] == 0:
        if not heap:
            output.append(-1)
        else :
            output.append(heapq.heappop(heap)[1])

    else :
        for item in input_list[1:]:
            heapq.heappush(heap, (-item, item))
        
        
for i in output:
    print(i)
