class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        pchar = ''
        startIndex = None
        count = 0
        output = []
        for idx,i in enumerate(S):
            if i == pchar:
                count += 1
            else:
                if count >= 3:
                    output.append((startIndex, idx-1))
                pchar = i
                count = 1
                startIndex = idx
        if count >=3:
            output.append((startIndex, len(S)-1))
        return output
