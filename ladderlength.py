class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def dist(a,b):
            mismatch = 0
            for i,j in zip(a,b):
                if i != j:
                    mismatch += 1
            return mismatch
        totallist = wordList + [beginWord]
        edgel = defaultdict(list)
        for i in range(len(totallist)):
            for j in range(i, len(totallist)):
                if dist(totallist[i],totallist[j]) == 1:
                    edgel[totallist[i]].append(totallist[j])
                    edgel[totallist[j]].append(totallist[i])
        #print(edgel)
        queue = [(beginWord,1)]
        seen = set()
        seen.add(beginWord)
        while len(queue) > 0:
            elem,path = queue.pop(0)
            if elem == endWord:
                return path
            if elem in edgel:
                for i in edgel[elem]:
                    if i not in seen:
                        seen.add(i)
                        queue.append((i, path+1))
        return 0
