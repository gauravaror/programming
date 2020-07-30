class Solution:
    def __init__(self):
        self.cache = {}
        
    def wordBreak1(self, s: str) -> List[str]:
        #print(s, self.cache)
        if s in self.cache:
            return self.cache[s]
        final_output = []
        if s in self.wordDict:
            final_output = [s]
        for word in self.wordDict:
            if s.startswith(word):
                remainingword = s[len(word):]
                if remainingword in self.cache:
                    forward_sent = self.cache[remainingword]
                else:
                    forward_sent = self.wordBreak1(remainingword)
                if len(forward_sent) != 0:
                    for i in forward_sent:
                        if i:
                            final_output.append(word + ' ' + i)
        self.cache[s] = final_output
        return final_output
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        output = self.wordBreak1(s)
        output1 = []
        return output
