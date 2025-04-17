### 입출력 정리

#### 입력 정리
**두 개의 값**  
- n: 엔지니어 수
- k: 팀 인원 수

**리스트 입력(n개의 입력)**
- speed[len(n)]
- efficiency[len(n)]

**문제 풀이**
> **maxPerformance 함수에 작성 및 활용**    
> _별도의 input 부분 작성 필요 X_

#### 출력 정리
> **maximum performance 를 반환하기**    
> $performance = sum(speed) * min(efficiency)$
> *출력값은 $mod(10^9 + 7)$ 하여 반환

#### 브레인스토밍
인원에 대한 리스트로서 관리할 필요는 없음.    

즉, index 무관하게 사용하면 되는 부분    

그렇다면, sort 등 자유롭게 활용하되, efficiency와 speed index는 항상 일치 시켜줘야 함.  

둘의 각각의 원소를 하나의 튜플로 묶어 관리해도 좋을 것으로 보임.

> **문제의 핵심**
> speed 값이 큰 인원을 찾되, efficiency 가 작지 않은 사람 중심으로 k 명을 선발하기
> efficiency 값이 큰 인원으로 구성되어야 유리함.

여러가지 시간 복잡도를 고려,

sort + heapq 를 이용한다면 각 result를 계산하는 것을 O(log K)로 종료 가능  
N 회 반복하니 최종 시간 복잡도가 O(N log k)  
시간 내에 문제 풀이 가능  

> **풀이 핵심**
> 정렬 시 값을 뒤에서부터 정렬하지 말고, 큰 값부터 내림차순으로 정렬하는 것이 핵심임.
> 만약 오름차순으로 정렬할 경우 N^2으로 순회해야하는 문제 발생   
> **Why? :** heapq에 efficiency 값이 현재보다 작은 worker가 남아 있지 않다는 보장을 못함.

### 슈도 코드 (sudo)

```python
worker = [(a, b) for a, b in speed, efficiency]
worker.sort(key = lambda x: x.efficiency for x in worker, decresing)

spd_queue = [] # speed heapq 
performance = 0 # 각 상태별 퍼포먼스 값
result = 0 # 최종 Output 값

for spd, eff in worker:
    spd 에 대해 heapq k 개수 만큼 유지
    performance = sum(spd_queue) * eff    # worker가 내림차순 정렬이기에, 현재 순회하는 값의 eff가 최솟값
    result = max(performance, result)

return result % (10**9+7)
```