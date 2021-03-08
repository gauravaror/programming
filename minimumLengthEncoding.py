class Node:
    def __init__(self):
        self.chars = {}
        self.fin = False

    def add(self, word):
        if len(word) == 0:
            return True
        if word[0] not in self.chars:
            self.chars[word[0]] = Node()
        x = self.chars[word[0]].add(word[1:])
        self.fin = self.fin or x


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Node()
        for word in words:
            root.add(word[::-1])

        def get_len(n, level):
            if len(n.chars) == 0:
                return level + 1
            ans = 0
            for c in n.chars.values():
                ans += get_len(c, level + 1)
            return ans

        return get_len(root, 0)
