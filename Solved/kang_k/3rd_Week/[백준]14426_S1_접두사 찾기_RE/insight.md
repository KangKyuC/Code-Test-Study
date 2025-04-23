## in 연산 시간복잡도

### 자료구조마다 시간복잡도가 다르다
> 사실상 최적화된 순회로 보는 편이 좋을 듯.

**list, tuple**
- Average: O(n)
- 하나씩 순회

**set, dictionary**
- Average: O(1), Worst: O(n)
- hash를 통해 조회하며, 충돌에 따라 성능이 떨어지는 경우 O(n)

