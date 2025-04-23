import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        heap_sum = 0
        result = 0
        heap_lst = []

        lst = sorted(zip(efficiency, speed), reverse=True)
        # print(lst)

        for eff, spd in lst:
            heapq.heappush(heap_lst, spd)
            heap_sum += spd
            # print(f"heap_lst is  {heap_lst}")
            # print(f"heap_sum is  {heap_sum}")

            if k < len(heap_lst):
                heap_sum -= heapq.heappop(heap_lst)

            per_val = eff * heap_sum
            # print(f"per_val is  {per_val}")

            result = max(result, per_val)

        return result % MOD

