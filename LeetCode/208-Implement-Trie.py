class Trie:

    def __init__(self, word_list=[]):
        self.word_list = word_list

    def insert(self, word: str) -> None:
        self.word_list = self.word_list + [word]
        return None
        
    def search(self, word: str) -> bool:
        if word in self.word_list:
            return True
        return None

    def startsWith(self, prefix: str) -> bool:
        for word in self.word_list:
            if prefix == word[:len(prefix)]:
                return True
        return False
                
        
"""
트라이 구현

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.word = False
        self.root = collections.defaultdict(TrieNode())

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children: return False
            node = node.children[char]
        return True

"""

# Your Trie object will be instantiated and called as such:
# obj = Trie()x``
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)