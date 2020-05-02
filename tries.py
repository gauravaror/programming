class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.thischar = ''
        self.child = {}
        self.leaf = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            self.leaf = True
            return
        fc = word[0]
        rw = word[1:]
        if word[0] in self.child:
            tr = self.child[fc]
        else:
            tr = Trie()
            tr.thischar = fc
            self.child[fc] = tr
        tr.insert(rw)
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return True if self.leaf else False
        fc = word[0]
        if fc in self.child:
            return self.child[fc].search(word[1:])
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return True
        fc = prefix[0]
        if fc in self.child:
            return self.child[fc].startsWith(prefix[1:])
        else:
            return False
