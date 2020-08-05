class Trie:
    def __init__(self):
        self.childrens = {}
        self.val = None
        self.ending = False
        
    def add(self, word):
        if len(word) == 0:
            self.ending = True
            return
        if word[0] in self.childrens:
            self.childrens[word[0]].add(word[1:])
        else:
            self.childrens[word[0]] = Trie()
            self.childrens[word[0]].add(word[1:])
    
    def search(self, word):
        #print(word, self.childrens)
        if len(word) == 0:
            return True if self.ending else False
        if word[0] == '.':
            return any([ i.search(word[1:]) for i in self.childrens.values()])
        elif word[0] in self.childrens:
            return self.childrens[word[0]].search(word[1:])
        else:
            return False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
