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
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()x``
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)