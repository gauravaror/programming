class Trie:
    def __init__(self):
        self.chars = {}
        self.finishing = False
        #self.wrd = word
    
    def add(self, word):
        if len(word) == 0:
            self.finishing = True
            return
        if word[0] not in self.chars:
            self.chars[word[0]] = Trie()
        self.chars[word[0]].add(word[1:])

from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            self.root.add(word[::-1])
        self.deque = deque()

    def query(self, letter: str) -> bool:
        self.deque.appendleft(letter)
        node = self.root
        for i in self.deque:
            if i in node.chars:
                node = node.chars[i]
                if node.finishing:
                    return True
            else:
                return False
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
