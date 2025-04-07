1차시 - 시간초과
---
num = int(input())

result = []

def power(a, b):
    result.append(a ** b % 10)

for i in range(num):
    a, b = [int(v) for v in input().split()]
    power(a, b)

for i in result:
    print(i)
---

ChatGPT 힌트
✅ 현재 코드의 성능 분석
a ** b % 10 연산 자체는 보통 Python에서 빠르게 처리되지만, b가 매우 크면 a ** b가 커져서 시간이 걸릴 수 있습니다.

특히, a와 b의 범위가 클 경우 a ** b를 직접 계산하는 건 비효율적입니다.

하지만 우리는 결과를 10으로 나눈 나머지만 원하기 때문에, **반복되는 패턴(cycle)**을 이용해 속도를 대폭 향상시킬 수 있습니다.
---
2차시 - 실패

num = int(input())

result = []

pow_dic = {
    0 : [0],
    1 : [1],
    2 : [2,4,8,6],
    3 : [3,9,7,1],
    4 : [4,6],
    5 : [5],
    6 : [6],
    7 : [7,9,3,1],
    8 : [8,4,2,6],
    9 : [9,1],
}

def power(a, b):
    if b == 0:
        result.append(1)
        return
    rest_a = a % 10
    cycle = pow_dic[rest_a]
    easy_b = (b-1) % len(cycle)
    result.append(cycle[easy_b])

for i in range(num):
    a, b = [int(v) for v in input().split()]
    power(a, b)

for i in result:
    print(i)
---
예외처리를 재검토해보니, 10번째 컴퓨터 번호에 대한 예외처리가 안되었던 것 같음.
---
3차시 성공
---
num = int(input())

result = [] # 결과값을 담을 빈 리스트

pow_dic = { # a ** b 의 1자리 수 패턴
    0 : [0],
    1 : [1],
    2 : [2,4,8,6],
    3 : [3,9,7,1],
    4 : [4,6],
    5 : [5],
    6 : [6],
    7 : [7,9,3,1],
    8 : [8,4,2,6],
    9 : [9,1],
}

def power(a, b): # 컴퓨터 번호 배정해주는 함수
    if b == 0: # b가 0일 때 
        result.append(1) # a의 0승인 1 추가
        return
    rest_a = a % 10 # a를 10으로 나눈 나머지
    cycle = pow_dic[rest_a] # a의 1자리수 패턴
    easy_b = (b-1) % len(cycle) # b-1을 패턴의 길이로 나눈 나머지
    result.append(cycle[easy_b]) # 패턴의 easy_b번째 추가
    
for i in range(num): # 입력
    a, b = [int(v) for v in input().split()]
    power(a, b)
    
for i in result:
    print(10 if i==0 else i)
