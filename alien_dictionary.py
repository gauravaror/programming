from collections import defaultdict
class Tries:
    def __init__(self):
        self.chars = {}
    
    def add(self, word, forw, back, any_new=False):
        #print(word, self.chars, forw, back)
        if len(word) == 0:
            return any_new or len(self.chars) == 0
        back[word[0]]
        if len(self.chars) > 0:
            for c in self.chars.keys():
                if c != word[0]:
                    back[word[0]].append(c)
                    forw[c].append(word[0])
        if not word[0] in self.chars.keys():
            self.chars[word[0]] = Tries()
            any_new = True
        return self.chars[word[0]].add(word[1:], forw, back, any_new)
        
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        forw = defaultdict(list)
        back = defaultdict(list)
        trieRoot = Tries()
        for i in words:
            if not trieRoot.add(i, forw, back, False):
                return ""
        stack = []
        for i in back.keys():
            if len(back[i]) == 0:
                stack.append(i)
        #if len(stack) != 1:
        #    return ""
        output = ""
        print(stack, forw, back)
        while len(stack) > 0:
            elem = stack.pop(0)
            output += elem
            if elem in forw:
                for dep in forw[elem]:
                    if  elem in back[dep]:
                        back[dep].remove(elem)
                        if len(back[dep]) == 0:
                            stack.append(dep)
                del forw[elem]
        print(back, forw)
        for i in back.keys():
            if len(back[i]) > 0:
                return ""
        return output

