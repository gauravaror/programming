from collections import defaultdict
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        ndegree = defaultdict(int)
        edgelist = defaultdict(list)
        elems  = set()
        for seq in seqs:
            for i in range(len(seq)):
                for j in range(i+1, len(seq)):
                    ndegree[seq[j]] += 1
                    edgelist[seq[i]].append(seq[j])
                    elems.add(seq[j])
                elems.add(seq[i])
        stack = []
        for i in elems:
            if ndegree[i] == 0:
                stack.append(i)
        #print(stack, ndegree)
        if len(stack) > 1:
            return False
        output = []
        while len(stack) > 0:
            item = stack.pop(0)
            output.append(item)
            for i in edgelist[item]:
                ndegree[i] -= 1
                if ndegree[i] == 0:
                    stack.append(i)
            if len(stack) > 1:
                return False
        if output == org:
            return True
        return False
