# 검색용 트리 구조(Trie) 참고
class TrieNode:
    def __init__(self):
        self.dictionary = {} # 노드에서 이어지는 알파벳을 저장할 딕셔너리
        self.is_end = False # 단어의 끝일 경우 True로 표시
    
class Trie:    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):  # 문자열 삽입
        node = self.root # 루트 노드에서 시작

        for char in word:
            if char not in node.dictionary: # 현재 노드에 해당 글자가 없으면 새로 만들기
                node.dictionary[char] = TrieNode()
        
            node = node.dictionary[char] # 해당 글자 노드로 이동
        
        node.is_end = True # 마지막 글자까지 다 넣으면 is_end를 True로 수정

trie = Trie()
trie.insert("code")
trie.insert("codex")
trie.insert("coin")
