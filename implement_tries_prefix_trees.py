class Trie:

    def __init__(self):
        self.chars = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        #print("insee", self.chars, word)
        if len(word) == 0:
            self.end = True
            return
        char = word[0]
        if char in self.chars:
            next_ = self.chars[char]
        else:
            next_ = Trie()
            self.chars[char] = next_
        next_.insert(word[1:])        
        #print("inserted,", self.chars)

    def search(self, word: str) -> bool:
        #print(self.chars, word)
        if len(word) == 0:
            return self.end
        char = word[0]
        if char not in self.chars:
            return False
        next_ = self.chars[char]
        return next_.search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        char = prefix[0]
        if char not in self.chars:
            return False
        next_ = self.chars[char]
        return next_.startsWith(prefix[1:])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
