import heapq

N = int(input())
num_list = []
heap = []
count = 0 # 삽입 횟수 찾기

for i in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])