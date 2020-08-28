class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        def perform_operation(word, start):
            idx = 0
            for i in range(start, start+len(word)):
                if i >= len(S):
                    return False
                print(S[i], word[idx])
                if S[i] != word[idx]:
                    return False
                idx += 1
            return True
        
        for idx in range(len(indexes)):
            if not perform_operation(sources[idx], indexes[idx]):
                indexes[idx]  = -1
        print(indexes)
        prev = 0
        output = ""
        ltuple = list(zip(indexes,sources,targets))
        ltuple = sorted(ltuple, key=lambda x: x[0])
        for i in range(len(indexes)):
            if ltuple[i][0] != -1:
                output += S[prev:ltuple[i][0]]
                output += ltuple[i][2]
                prev = ltuple[i][0] + len(ltuple[i][1])
        output += S[prev:]
        return output
