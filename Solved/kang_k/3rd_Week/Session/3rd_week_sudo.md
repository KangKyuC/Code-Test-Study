## 문제 분석

카드 속에 숫자가 있니?       
K 개의 마법 카드      
정수 M ($1 \le M \le N$)
F 친구에게 yes/no seuquences 를 받음.

### 입력값

**N, K, M, F-> INT**
- N: 마법 카드 속 숫자 범위              
- K: 마법카드 개수              
- M: 마법카드 속 숫자 개수             
- F: 친구에게 답변 받은 Yes/No sequeuences        

### 출력값

F 개수만큼 출력       
단, i 번째 줄에는 i 번째 sequence에 대한 답변        

이때, 숫자가 특정되지 않으면 0 출력

## 브레인스토밍

3초의 시간 소요       
2048MB 메모리      

입력값에 대해 2차원 리스트를 만들고
YN Sequence에 대해 교집합을 하면 되지 않을까?         
YES -> 교집합
NO -> 차집합

### 수도코드

```python

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

```

### 시간복잡도 역산

> O(F * K * O(min(N, M))) = **O(F * K * N)**      

주어진 문제에서 최악의 경우     
50,000 * 100 * 500,000 = $25 * 10^ {11}$

시간초과 발생확률이 높음.      

> 파이썬은 초당 $10^7 ~ 5*10^7$ 처리한다고 함.
