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
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.tre = Trie()
        for i in wordDict:
            self.tre.insert(i)
        self.ans = []
        def sentenceSearch(word, tri, output):
            #print(tri, word, output)
            if len(word) == 0:
                if tri.leaf:
                    self.ans.append(output)
                    return True
                else:
                    return False
            if word[0] not in tri.child:
                return False
            cc = tri.child[word[0]]
            if cc.leaf and len(word) > 1:
                sentenceSearch(word[1:], self.tre, output + word[0] + ' ')
            sentenceSearch(word[1:], cc, output+word[0])
        sentenceSearch(s, self.tre, "")
        return self.ans
