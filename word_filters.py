class Trie:
    def __init__(self):
        self.chars = defaultdict(Trie)
        self.indexes = []
    
    def insert(self, word, index):
        self.indexes.append(index)
        if not word:
            return
        if word[0] not in self.chars:
            self.chars[word[0]] = Trie()
        self.chars[word[0]].insert(word[1:], index)
    
    def search(self, word):
        if not word:
            return self.indexes
        if word[0] in self.chars:
            return self.chars[word[0]].search(word[1:])
        return []
        
            
            
class WordFilter:

    def __init__(self, words: List[str]):
        self.all_words = Trie()
        for i in range(len(words)):
            word = words[i]
            inv = word[::-1]
            self.all_words.insert("#" + word, i)
            for j in range(len(word)):
                self.all_words.insert(inv[:j+1][::-1] + "#" + word, i)
            
                
    def f(self, p: str, s: str) -> int:
        search = s + '#' + p
        indexes = self.all_words.search(search)
        return indexes[-1] if indexes else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
