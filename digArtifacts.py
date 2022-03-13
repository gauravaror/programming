class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ats = defaultdict(set)
        for idx, i in enumerate(artifacts):
            for r in range(i[0], i[2]+1):
                for c in range(i[1], i[3]+1):
                    ats[idx].add((r,c))
        digged_elems = set()
        for i in dig:
            digged_elems.add((i[0],i[1]))
        output = 0
        for i in ats.keys():
            all_dig = True
            for elem in ats[i]:
                if elem not in digged_elems:
                    all_dig = False
            if all_dig:
                output += 1
        return output
        
        
