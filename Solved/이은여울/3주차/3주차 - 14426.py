# 검색용 트리 구조(Trie)
class TrieNode:
    def __init__(self):
        self.dictionary = {} # 노드에서 이어지는 알파벳을 저장할 딕셔너리

# 트라이 구조 정의
class Trie:    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):  # 문자열 삽입
        node = self.root # 처음엔 루트 노드에서 시작

        for char in word:
            if char not in node.dictionary: # 현재 노드에 해당 글자가 없으면 새로 만들기
                node.dictionary[char] = TrieNode()
        
            node = node.dictionary[char] # 해당 글자 노드로 이동
    
    def starts_with(self, prefix): # 검사 문자열이 S의 접두사로 쓰이는지 확인하는 로직
    # self.root부터 시작해서, 한 글자씩
        node = self.root
        for char in prefix:
            if char not in node.dictionary: # 현재 char가 딕셔너리의 key에 존재하지 않으면 True 반환
                return False
            node = node.dictionary[char] #다음 노드로 이동
        return True
    

# # 테스트
# trie = Trie()

# # 집합 S를 Trie에 insert
# S = ["codeplus", "codingsh", "startlink"]
# for word in S:
#     trie.insert(word)

# # 검사 문자열 리스트
# tests = ["cod", "code", "start", "plu", "star", "coding"]

# # 테스트 실행
# for test in tests:
#     result = trie.starts_with(test)
#     print(f"'{test}' is prefix of any S string?: {result}")

N, M = map(int, input().split())
S = []
prefixs = []
count = 0

for _ in range(N):
    temp = input()
    S.append(temp)

for _ in range(M):
    temp = input()
    prefixs.append(temp)

# print(S)
# print(prefixs)

trie = Trie()

for word in S:
    trie.insert(word)

for prefix in prefixs:
    result = trie.starts_with(prefix)
    if result:
        count += 1

print(count)