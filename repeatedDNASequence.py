class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        store = Counter()
        output = set()
        for i in range(len(s)):
            st = s[i:i+10]
            store[st] += 1
            if store[st] > 1:
                output.add(st)
        return list(output)
